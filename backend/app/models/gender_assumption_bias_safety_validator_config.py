from typing import ClassVar, List, Literal, Optional
from app.models.base_validator_config import BaseValidatorConfig
from app.core.validators.gender_assumption_bias import BiasCategories, GenderAssumptionBias

class GenderAssumptionBiasSafetyValidatorConfig(BaseValidatorConfig):
    type: Literal["gender_assumption_bias"]
    categories: Optional[List[BiasCategories]] = [BiasCategories.All]
    validator_cls: ClassVar = GenderAssumptionBias