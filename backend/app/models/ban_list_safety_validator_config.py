from guardrails.hub import BanList
from typing import ClassVar, List, Literal

from app.models.base_validator_config import BaseValidatorConfig
from app.core.constants import BAN_LIST
# from app.safety.validators.hub_loader import load_hub_validator_class, ensure_hub_validator_installed

class BanListSafetyValidatorConfig(BaseValidatorConfig):
    type: Literal[f"{BAN_LIST}"]
    banned_words: List[str]
    validator_cls: ClassVar = BanList