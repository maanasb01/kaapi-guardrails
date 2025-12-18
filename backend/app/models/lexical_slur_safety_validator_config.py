from typing import ClassVar, List, Literal
from app.core.validators.lexical_slur import LexicalSlur
from app.models.base_validator_config import BaseValidatorConfig

class LexicalSlurSafetyValidatorConfig(BaseValidatorConfig):
    type: Literal["uli_slur_match"]
    languages: List[str] = ["en", "hi"]
    severity: Literal["low", "medium", "high", "all"] = "all"
    validator_cls: ClassVar = LexicalSlur