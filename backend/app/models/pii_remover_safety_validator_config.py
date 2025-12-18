from __future__ import annotations
from typing import ClassVar, List, Literal, Optional

from app.core.validators.utils.language_detector import LanguageDetector
from app.models.base_validator_config import BaseValidatorConfig
from app.core.validators.pii_remover import PIIRemover

class PIIRemoverSafetyValidatorConfig(BaseValidatorConfig):
    type: Literal["pii_remover"]
    entity_types: Optional[List[str]] = None
    threshold: float = 0.5
    language: str = "en"
    language_detector: Optional[LanguageDetector] = None
    validator_cls: ClassVar = PIIRemover