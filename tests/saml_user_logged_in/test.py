import json

from fair_wizard.automation.common.model import HandlerContext
from handler import handler

result = handler(
    event={
        "assertion": {
            "assertionAttributeStatement": [
                {
                    "attributeFriendlyName": "email",
                    "attributeName": "urn:oid:1.2.840.113549.1.9.1",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "vojtech.knaisl@example.com"
                },
                {
                    "attributeFriendlyName": "givenName",
                    "attributeName": "urn:oid:2.5.4.42",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "Vojtech"
                },
                {
                    "attributeFriendlyName": "surname",
                    "attributeName": "urn:oid:2.5.4.4",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "Knaisl"
                },
                {
                    "attributeFriendlyName": None,
                    "attributeName": "Role",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "offline_access"
                },
                {
                    "attributeFriendlyName": None,
                    "attributeName": "Role",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "uma_authorization"
                },
                {
                    "attributeFriendlyName": None,
                    "attributeName": "Role",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "manage-account"
                },
                {
                    "attributeFriendlyName": None,
                    "attributeName": "Role",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "manage-account-links"
                },
                {
                    "attributeFriendlyName": None,
                    "attributeName": "Role",
                    "attributeNameFormat": "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
                    "attributeValue": "view-profile"
                }
            ],
            "assertionAuthnStatement": {
                "authnStatementInstant": "2024-09-13T13:11:42.817Z",
                "authnStatementLocality": "",
                "authnStatementSessionIndex": "e43055ce-bed8-4b70-8190-eb77b8706a6b::a47fb8ac-f331-4eb3-812b-3babca9c0780"
            },
            "assertionConditions": {
                "conditionsAudienceRestrictions": [
                    {
                        "audienceRestrictionAudience": [
                            "http://localhost:3002/admin-api/saml-service-providers/02bfcc16-98a6-4f64-9742-440caca0adb2"
                        ]
                    }
                ],
                "conditionsNotBefore": "2024-09-13T13:11:40.817Z",
                "conditionsNotOnOrAfter": "2024-09-13T13:12:40.817Z"
            },
            "assertionId": "ID_051b5eeb-0523-4cc5-bdd8-8e094abb369e",
            "assertionIssued": "2024-09-13T13:11:42.817Z",
            "assertionIssuer": "https://keycloak.dev.ds-wizard.org/auth/realms/vojta",
            "assertionSubject": {
                "subjectConfirmations": [
                    {
                        "subjectConfirmationAddress": "",
                        "subjectConfirmationMethod": "Bearer",
                        "subjectConfirmationNotOnOrAfter": "2024-09-13T13:16:40.817Z",
                        "subjectConfirmationRecipient": "http://localhost:3002/admin-api/saml-service-providers/02bfcc16-98a6-4f64-9742-440caca0adb2/response"
                    }
                ],
                "subjectNameID": {
                    "nameIDFormat": "Transient",
                    "nameIDQualifier": None,
                    "nameIDSPNameQualifier": None,
                    "nameIDSPProvidedID": None,
                    "nameIDValue": "G-c1c4b07e-b0ea-468f-9804-fa2b8582f2dd"
                }
            }
        }
    },
    context=HandlerContext(),
)

print(json.dumps(result, indent=2))
