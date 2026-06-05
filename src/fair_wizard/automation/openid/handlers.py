from fair_wizard.automation.common import AuthorizedUserResponse, UserLoginResponse
from fair_wizard.automation.openid.model import OpenIdUserLoggedInEvent


def handle_openid_user_logged_in(openid_event: OpenIdUserLoggedInEvent) -> UserLoginResponse:
    """
    Default *handle* function for "OpenID User Logged In" event.

    :param openid_event: incoming :py:class:`OpenIdUserLoggedInEvent` event
    :return: resulting :py:type:`UserLoginResponse` response
    """
    return AuthorizedUserResponse(
        first_name=openid_event.id_token.other_claims.get('given_name'),
        last_name=openid_event.id_token.other_claims.get('family_name'),
        image_url=None,
        affiliation=None,
        email=openid_event.id_token.other_claims.get('email'),
        external_id=openid_event.id_token.sub,
        external_label=openid_event.id_token.other_claims.get('email'),
        user_group_uuids=[],
    )
