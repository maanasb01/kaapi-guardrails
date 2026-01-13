# English PII text
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Rahul Mehta recently moved to Bengaluru, Karnataka, and can be contacted at +91-98765-43210 or via email at rahul.mehta92@example.com. His Aadhaar number is 470821987760, PAN is BQTPM7421K, voter ID is DL/05/123/456789, and passport number is K8239471. He owns a car registered as KA03MN4587 and runs a small business registered under GSTIN 29BQTPM7421K1Z5. Rahul recently paid a hospital bill using his credit card 4539 1488 0343 6467 and consulted a doctor holding medical license MH/MC/2021/778899. During an online consultation from IP address 192.168.1.42, he accessed the clinic’s website at https://www.healthcare-consult.in. For an international transfer, he shared his IBAN DE89 3704 0044 0532 0130 00 and later uploaded a notarized document with registration number NRP-IND-2024-556782.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "all"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        },
        {
            "type": "pii_remover",
            "language": "hi"
        }
    ]
}

# Hindi PII text
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "राहुल मेहता हाल ही में बेंगलुरु, कर्नाटक चले गए हैं, और उनसे +91-98765-43210 पर या ईमेल rahul.mehta92@example.com के माध्यम से संपर्क किया जा सकता है। उनका आधार नंबर 470821987760 है, पैन नंबर BQTPM7421K है, मतदाता पहचान पत्र संख्या DL/05/123/456789 है, और पासपोर्ट नंबर K8239471 है। उनके पास KA03MN4587 नंबर की एक कार पंजीकृत है और वे GSTIN 29BQTPM7421K1Z5 के अंतर्गत पंजीकृत एक छोटा व्यवसाय चलाते हैं। राहुल ने हाल ही में अपने क्रेडिट कार्ड 4539 1488 0343 6467 का उपयोग करके एक अस्पताल का बिल चुकाया और MH/MC/2021/778899 मेडिकल लाइसेंस वाले एक डॉक्टर से परामर्श लिया। एक ऑनलाइन परामर्श के दौरान, IP पता 192.168.1.42 से उन्होंने क्लिनिक की वेबसाइट https://www.healthcare-consult.in एक्सेस की। एक अंतरराष्ट्रीय ट्रांसफर के लिए उन्होंने अपना IBAN DE89 3704 0044 0532 0130 00 साझा किया और बाद में NRP-IND-2024-556782 पंजीकरण संख्या वाला एक नोटरीकृत दस्तावेज़ अपलोड किया।",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "all"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        },
        {
            "type": "pii_remover",
            "language": "hi"
        }
    ]
}

# Romanized Hindi PII text
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Rahul Mehta recently Bengaluru, Karnataka shift hue hain, aur unse +91-98765-43210 par ya email rahul.mehta92@example.com ke through contact kiya ja sakta hai. Unka Aadhaar number 470821987760 hai, PAN BQTPM7421K hai, voter ID DL/05/123/456789 hai, aur passport number K8239471 hai. Unke naam par KA03MN4587 number ki ek car registered hai aur woh GSTIN 29BQTPM7421K1Z5 ke under registered ek chhota business bhi chalate hain. Rahul ne recently apne credit card 4539 1488 0343 6467 ka use karke ek hospital bill pay kiya aur MH/MC/2021/778899 medical license wale ek doctor se consultation li. Online consultation ke dauran, IP address 192.168.1.42 se unhone clinic ki website https://www.healthcare-consult.in access ki. Ek international transfer ke liye unhone apna IBAN DE89 3704 0044 0532 0130 00 share kiya aur baad mein NRP-IND-2024-556782 registration number wala ek notarized document upload kiya.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "all"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        },
        {
            "type": "pii_remover",
            "language": "hi"
        }
    ]
}

# Romanized Hindi PII text with entity types
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Rahul Mehta recently Bengaluru, Karnataka shift hue hain, aur unse +91-98765-43210 par ya email rahul.mehta92@example.com ke through contact kiya ja sakta hai. Unka Aadhaar number 470821987760 hai, PAN BQTPM7421K hai, voter ID DL/05/123/456789 hai, aur passport number K8239471 hai. Unke naam par KA03MN4587 number ki ek car registered hai aur woh GSTIN 29BQTPM7421K1Z5 ke under registered ek chhota business bhi chalate hain. Rahul ne recently apne credit card 4539 1488 0343 6467 ka use karke ek hospital bill pay kiya aur MH/MC/2021/778899 medical license wale ek doctor se consultation li. Online consultation ke dauran, IP address 192.168.1.42 se unhone clinic ki website https://www.healthcare-consult.in access ki. Ek international transfer ke liye unhone apna IBAN DE89 3704 0044 0532 0130 00 share kiya aur baad mein NRP-IND-2024-556782 registration number wala ek notarized document upload kiya.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "all"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        },
        {
            "type": "pii_remover",
            "entity_types": [
                "MEDICAL_LICENSE",
                "PHONE_NUMBER",
                "URL",
                "IN_AADHAAR", 
                "IN_PAN", 
                "IN_PASSPORT",
                "IN_VEHICLE_REGISTRATION",
                "IN_VOTER"
            ]
        }
    ]
}

# Lexical slur text with all matches
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Jidhar jao sirf chapris hi dikhte hai. Mann karta hai unka pichwada maar maarke laal kar du. Bacche ki sonography karane jaana tha lekin mood kharab ho gaya.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "all"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        }
    ]
}

# Lexical slur text with high severity only
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Jidhar jao sirf chapris hi dikhte hai. Mann karta hai unka pichwada maar maarke laal kar du. Bacche ki sonography karane jaana tha lekin mood kharab ho gaya.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "high"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        }
    ]
}

# Lexical slur text with high severity and exception on fail
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Jidhar jao sirf chapris hi dikhte hai. Mann karta hai unka pichwada maar maarke laal kar du. Bacche ki sonography karane jaana tha lekin mood kharab ho gaya.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "high",
            "on_fail": "exception"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        }
    ]
}

# Incorrect validator
{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "hello",
    "validators": [
        {
            "type": "uli_slur_matchx",
            "severity": "high",
            "on_fail": "noop"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        },
        {
            "type": "pii_remover",
            "entity_types": [
                "PHONE_NUMBER",
                "URL",
                "IN_AADHAAR", 
                "IN_PAN", 
                "IN_PASSPORT",
                "IN_VEHICLE_REGISTRATION",
                "IN_VOTER"
            ]
        }
    ]
}

{
    "request_id": "3f6a9d2e-8c47-4b8a-9f3c-1d2a6e7f4c91",
    "input": "Rahul Mehta recently moved to Bengaluru, Karnataka, and can be contacted at +91-98765-43210 or via email at rahul.mehta92@example.com. His Aadhaar number is 470821987760, PAN is BQTPM7421K, voter ID is DL/05/123/456789, and passport number is K8239471. He owns a car registered as KA03MN4587 and runs a small business registered under GSTIN 29BQTPM7421K1Z5. Rahul recently paid a hospital bill using his credit card 4539 1488 0343 6467 and consulted a doctor holding medical license MH/MC/2021/778899. During an online consultation from IP address 192.168.1.42, he accessed the clinic’s website at https://www.healthcare-consult.in. For an international transfer, he shared his IBAN DE89 3704 0044 0532 0130 00 and later uploaded a notarized document with registration number NRP-IND-2024-556782.",
    "validators": [
        {
            "type": "uli_slur_match",
            "severity": "all"
        },
        {
            "type": "ban_list",
            "banned_words": [
                "sonography"
            ]
        },
        {
            "type": "pii_remover",
            "entity_types": [
                "PHONE_NUMBER",
                "URL",
                "IN_AADHAAR", 
                "IN_PAN", 
                "IN_PASSPORT",
                "IN_VEHICLE_REGISTRATION",
                "IN_VOTER"
            ]
        }
    ]
}