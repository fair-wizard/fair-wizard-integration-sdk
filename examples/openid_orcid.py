import json
import urllib.request

from fair_wizard.automation.common import AuthorizedUserResponse, UserLoginResponse, ErrorResponse
from fair_wizard.automation.openid import OpenIdUserLoggedInEvent


def openid_user_logged_in_function(openid_event: OpenIdUserLoggedInEvent) -> UserLoginResponse:
    try:
        email = retrieve_email_from_orcid_if_present(openid_event)
    except Exception:
        return ErrorResponse(
            message=f'Failed to retrieve email from ORCID',
        )
    return AuthorizedUserResponse(
        first_name=openid_event.id_token.other_claims['given_name'],
        last_name=openid_event.id_token.other_claims['family_name'],
        image_url=None,
        affiliation=None,
        email=email,
        user_group_uuids=[],
    )


def retrieve_email_from_orcid_if_present(request: OpenIdUserLoggedInEvent) -> str:
    orcid = request.id_token.sub
    url = f'https://pub.orcid.org/v3.0/{orcid}/email'
    headers = {
        'Authorization': f'Bearer {request.access_token}',
        'Accept': 'application/json',
    }
    print(f"Calling ${url}")
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as response:
        raw_data = response.read().decode('utf-8')
        print(raw_data)
        json_data = json.loads(raw_data)
        if len(json_data['email']) == 1:
            return json_data['email'][0]
        else:
            return f'{orcid}@orcid.org'


if __name__ == '__main__':
    from fair_wizard.automation.common.model import HandlerContext
    from fair_wizard.automation.openid.wrappers import make_openid_user_logged_in_handler

    orcid_handler = make_openid_user_logged_in_handler(openid_user_logged_in_function)
    result = orcid_handler(
        event={
            'accessToken': 'baf71f0f-0d91-4d4a-96ab-bbac1b42a6c3',
            'expiresIn': 631138518,
            'idToken': {
                'aud': ['APP-STIPW2WK430U8QYM'],
                'exp': 1726131990,
                'iat': 1726045590,
                'iss': 'https://orcid.org',
                'sub': '0000-0000-0000-0000',
                'otherClaims': {
                    'at_hash': '5EFNCiiH0bIxdBF_KV8M0g',
                    'aud': 'APP-STIPW2WK430U8QYM',
                    'auth_time': 1726045311,
                    'exp': 1726131990,
                    'family_name': 'John',
                    'given_name': 'Doe',
                    'iat': 1726045590,
                    'iss': 'https://orcid.org',
                    'jti': '14db11cb-488c-4ef4-957d-7821b6076073',
                    'nonce': 'NQXY4NqcrzK3ayySZRTr6MW3n4KBQwYUCWeYsfYj',
                    'sub': '0000-0000-0000-0000',
                },
            },
            'idTokenJwt': '...',
            'refreshToken': '309de4ce-928c-4778-b79d-439bd4c8f81f',
            'tokenType': 'bearer',
        },
        context=HandlerContext(),
    )
    print(json.dumps(result, indent=2))
