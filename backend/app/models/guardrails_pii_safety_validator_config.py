from guardrails.hub import GuardrailsPII
from typing import List, Literal, Optional

from app.models.base_validator_config import BaseValidatorConfig

ENTITIES_LIST = [
    "CREDIT_CARD",
    "CRYPTO",
    "DATE_TIME",
    "EMAIL_ADDRESS",
    "IBAN_CODE",
    "IP_ADDRESS",
    "NRP",
    "LOCATION",
    "PERSON",
    "PHONE_NUMBER",
    "MEDICAL_LICENSE",
    "URL",
    "US_BANK_NUMBER",
    "US_DRIVER_LICENSE",
    "US_ITIN",
    "US_PASSPORT",
    "US_SSN",
    "UK_NHS",
    "ES_NIF",
    "ES_NIE",
    "IT_FISCAL_CODE",
    "IT_DRIVER_LICENSE",
    "IT_VAT_CODE",
    "IT_PASSPORT",
    "IT_IDENTITY_CARD",
    "PL_PESEL",
    "SG_NRIC_FIN",
    "SG_UEN",
    "AU_ABN",
    "AU_ACN",
    "AU_TFN",
    "AU_MEDICARE",
    "IN_PAN",
    "IN_AADHAAR",
    "IN_VEHICLE_REGISTRATION",
    "IN_VOTER",
    "IN_PASSPORT",
    "FI_PERSONAL_IDENTITY_CODE"
]

class GuardrailsPIISafetyValidatorConfig(BaseValidatorConfig):
    type: Literal[f"guardrails_pii"]
    entities: Optional[List[str]] = None   # 👈 THIS LINE FIXES EVERYTHING

    def build(self):
        entities = self.entities or ENTITIES_LIST
        return GuardrailsPII(
            entities=entities,
            on_fail=self.resolve_on_fail(),
        )