import pytest

pytestmark = pytest.mark.integration

@pytest.mark.integration
def test_input_guardrails_with_real_banlist(integration_client):
    response = integration_client.post(
        "/api/v1/guardrails/input/",
        json={
            "input": "this contains badword",
            "validators": [
                {
                    "type": "ban_list",
                    "banned_words": ["badword"]
                }
            ],
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True
    assert body["data"]["safe_input"] == "this contains b"

@pytest.mark.integration
def test_input_guardrails_passes_clean_text(integration_client):
    response = integration_client.post(
        "/api/v1/guardrails/input/",
        json={
            "input": "this is clean",
            "validators": [
                {
                    "type": "ban_list",
                    "banned_words": ["badword"]
                }
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()

    assert body["success"] is True
    assert body["data"]["safe_input"] == "this is clean"

def test_input_guardrails_with_lexical_slur(integration_client):
    response = integration_client.post(
        "/api/v1/guardrails/input/",
        json={
            "input": "This sentence contains chakki.",
            "validators": [
                {
                    "type": "uli_slur_match",
                    "severity": "all",
                }
            ],
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True
    assert body["data"]["safe_input"] == "this sentence contains [REDACTED_SLUR]"


def test_input_guardrails_with_lexical_slur_clean_text(integration_client):
    response = integration_client.post(
        "/api/v1/guardrails/input/",
        json={
            "input": "This is a completely safe sentence",
            "validators": [
                {
                    "type": "uli_slur_match",
                    "severity": "all",                
                }
            ],
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True
    assert body["data"]["safe_input"] == "This is a completely safe sentence"
