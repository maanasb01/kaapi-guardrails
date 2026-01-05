import logging
logging.getLogger("presidio-analyzer").setLevel(logging.ERROR)
import os
os.environ["GUARDRAILS_RUNNER"] = "sync"
import re

from functools import lru_cache
from guardrails import Guard
from sklearn.metrics import classification_report, confusion_matrix
from typing import get_args
from app.models.guardrail_config import GuardrailInputRequest, ValidatorConfigItem
import pandas as pd

def build_guard(validator_items):
    validators = [v_item.build() for v_item in validator_items]
    return Guard().use_many(*validators)

def get_validator_config_models():
    annotated_args = get_args(ValidatorConfigItem)
    union_type = annotated_args[0]
    return get_args(union_type)

def run_input_guardrails(payload: GuardrailInputRequest):
    try:
        guard = build_guard(payload.validators)
        result = guard.validate(payload.input)

        return result.validated_output

    except Exception as e:
        return str(e)

@lru_cache(maxsize=8)
def get_guard(guardrail_name: str):
    config = GuardrailInputRequest(
        input="",
        validators=[{"type": guardrail_name}]
    )
    return build_guard(config.validators)

def apply_guardrails(input_text, guardrail_name):
    guard = get_guard(guardrail_name)
    result = guard.validate(input_text)
    return result.validated_output


#--------------PII Removal Evaluation Utils ----------------#

import re

def normalize(text):
    text = re.sub(r"\[[A-Z_]+\]", "MASK", text)
    text = re.sub(r"<[A-Z_]+>", "MASK", text)
    return text

def tokenize(text):
    return text.split()

def compute_metrics(df, pred_col):
    TP = FP = FN = 0

    for _, row in df.iterrows():
        gold = tokenize(normalize(row["target_text"]))
        pred = tokenize(normalize(row[pred_col]))

        for g, p in zip(gold, pred):
            if g == "MASK" and p == "MASK":
                TP += 1
            elif g != "MASK" and p == "MASK":
                FP += 1
            elif g == "MASK" and p != "MASK":
                FN += 1

    precision = TP / (TP + FP) if TP + FP else 0
    recall = TP / (TP + FN) if TP + FN else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "TP": TP,
        "FP": FP,
        "FN": FN
    }

PII_PATTERN = re.compile(r"<[^>]+>")

def predicted_label(predicted_text):
    """
    Returns 'pii' if the predicted_text contains any PII placeholder like <PHONE_NUMBER>.
    Otherwise returns 'no_pii'.
    """
    if predicted_text is None:
        return "no_pii"

    return "pii" if PII_PATTERN.search(predicted_text) else "no_pii"

def run_pii_on_huggingface_dataset():
    custom_gname_output = 'custom_gname_output'
    hub_gname_output = 'hub_gname_output'
    eng_text = 'source_text'
    custom_gname = "pii_remover"
    hub_gname = "guardrails_pii"
    
    df = pd.read_csv('/Users/kritikarupauliha/downloads/output-200.csv')
    df[custom_gname_output] = df[eng_text].apply(lambda x: apply_guardrails(x, custom_gname))
    df[hub_gname_output] = df[eng_text].apply(lambda x: apply_guardrails(x, hub_gname))
    df.to_csv('/Users/kritikarupauliha/downloads/guardrail_comparison_output.csv', index=False)
    custom_metrics = compute_metrics(df, custom_gname_output)
    hub_metrics = compute_metrics(df, hub_gname_output)
    print("Custom:", custom_metrics)
    print("Hub:", hub_metrics)

def run_pii_on_hindi_synthetic_data():
    text_col = 'message'
    custom_gname = "pii_remover"
    hub_gname = "guardrails_pii"
    custom_gname_output = 'custom_gname_output'
    hub_gname_output = 'hub_gname_output'

    df = pd.read_csv('/Users/kritikarupauliha/downloads/hindi_synthetic_pii_data.csv')
    df[custom_gname_output] = df[text_col].apply(lambda x: apply_guardrails(x, custom_gname))
    df[hub_gname_output] = df[text_col].apply(lambda x: apply_guardrails(x, hub_gname))
    df['custom_gname_label'] = df[custom_gname_output].apply(predicted_label)
    df['hub_gname_label'] = df[hub_gname_output].apply(predicted_label)
    df.to_csv('/Users/kritikarupauliha/downloads/hindi_synthetic_pii_data-output.csv', index=False)

    print("Custom gname performance:")
    print(confusion_matrix(df['label'], df['custom_gname_label']))
    print(classification_report(df['label'], df['custom_gname_label']))

    print("\n\n\n")
    print("Hub gname performance:")
    print(confusion_matrix(df['label'], df['hub_gname_label']))
    print(classification_report(df['label'], df['hub_gname_label']))





#--------------Slur detector Evaluation Utils ----------------#
def run_slur_detection_on_kaggle_dataset():
    df = pd.read_csv('/Users/kritikarupauliha/downloads/slur-detection-eval-dataset-5000.csv')
    slur_gname = "uli_slur_match"
    custom_gname_output = 'custom_gname_output'

    df[custom_gname_output] = df['commentText'].apply(lambda x: apply_guardrails(x, slur_gname))
    df.to_csv('/Users/kritikarupauliha/downloads/slur_detection_output.csv', index=False)

if __name__ == "__main__":
    # run_pii_on_huggingface_dataset()
    # run_pii_on_hindi_synthetic_data()
    run_slur_detection_on_kaggle_dataset()