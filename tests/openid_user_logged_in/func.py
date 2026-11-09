from fair_wizard.automation.common import AuthorizedUserResponse, UserLoginResponse, UserWorkspace
from fair_wizard.automation.openid.model import OpenIdUserLoggedInEvent


def handle_openid_user_logged_in(openid_event: OpenIdUserLoggedInEvent) -> UserLoginResponse:
    return AuthorizedUserResponse(
        first_name=openid_event.id_token.other_claims.get('given_name'),
        last_name=openid_event.id_token.other_claims.get('family_name'),
        image_url=None,
        affiliation=None,
        email=openid_event.id_token.other_claims.get('email'),
        external_id=openid_event.id_token.sub,
        external_label=openid_event.id_token.other_claims.get('email'),
        tenant_role_uuid='e5a1a0c8-4ab1-4b8a-8b1c-0d4f3c8b7d21',
        workspaces=[
            UserWorkspace(
                workspace_uuid='3c0b1e6a-5b7e-4d0e-9a51-2f3c4d5e6f70',
                role_uuid=None,
                user_group_uuids=['7df586cc-e7ad-47b1-bc24-fbe132fbd391'],
            ),
        ],
    )
