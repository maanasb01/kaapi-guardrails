import emoji
import ftfy
import pandas as pd
import re
import string
import unicodedata

def normalize_text(text):
    # Fix mojibake, weird encodings, etc.
    text = ftfy.fix_text(text)
    # Normalize to NFKC form — converts fancy fonts to plain
    text = unicodedata.normalize("NFKC", text)
    return text

def remove_emojis(text):
    return emoji.replace_emoji(text, replace='')

def clean_text(text):
    text = normalize_text(text)
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

def remove_nos(text):
    text = re.sub(r'\d+', '', text)
    return text

if __name__ == "__main__":
    df = pd.read_csv(
        '/Users/kritikarupauliha/downloads/ShareChat-IndoML-Datathon-NSFW-CommentChallenge_Train-cleaned.csv',
    )
    df_sampled = df.sample(n=5000, random_state=42)
    # df = df[df['language'].isin(['Hindi', 'English'])]
    # df['commentText'] = df['commentText'].apply(remove_emojis)
    # df['commentText'] = df['commentText'].apply(remove_nos)
    # df['commentText'] = df['commentText'].apply(clean_text)
    df_sampled.to_csv('/Users/kritikarupauliha/downloads/slur-detection-eval-dataset-5000.csv', index=False)