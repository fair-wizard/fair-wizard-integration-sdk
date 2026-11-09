OpenID
======

Interface
---------

For OpenID automations, it is possible to define a custom function for handling the user logged in event. This function will be called when the user logs in using OpenID.

User Logged In
~~~~~~~~~~~~~~

You can implement your own *handle* function to handle the "User Logged In" event for OpenID. By default the following function is used:

.. autofunction:: fair_wizard.automation.openid.handle_openid_user_logged_in

Your *handle* function must have the same signature, i.e. accept :py:class:`OpenIdUserLoggedInEvent` as the argument and return :py:type:`UserLoginResponse`.

For example, your function can look like this:

.. code-block:: python

    from fair_wizard.automation.common import AuthorizedUserResponse, ErrorResponse, UserLoginResponse, UserWorkspace
    from fair_wizard.automation.openid.model import OpenIdUserLoggedInEvent

    def handle_openid_user_logged_in(openid_event: OpenIdUserLoggedInEvent) -> UserLoginResponse:
        try:
            email = retrieve_email_from_orcid(openid_event)
        except Exception:
            return ErrorResponse(
                message='Failed to retrieve email from ORCID (cannot log in)',
            )
        return AuthorizedUserResponse(
            first_name=openid_event.id_token.other_claims['given_name'],
            last_name=openid_event.id_token.other_claims['family_name'],
            image_url=None,
            affiliation=None,
            email=email,
            external_id=openid_event.id_token.sub,
            external_label=email,
            workspaces=[
                UserWorkspace(
                    workspace_uuid='3c0b1e6a-5b7e-4d0e-9a51-2f3c4d5e6f70',
                    user_group_uuids=['7df586cc-e7ad-47b1-bc24-fbe132fbd391'],
                ),
            ],
        )


Notice that :py:type:`UserLoginResponse` is actually just a type alias for union of :py:class:`AuthorizedUserResponse`, :py:class:`ErrorResponse`, and :py:class:`ForbiddenResponse`.

:py:class:`AuthorizedUserResponse` can also set the user's tenant role (``tenant_role_uuid``) and the workspaces the user becomes a member of (``workspaces``), each with an optional workspace role and the user groups of that workspace. Leaving ``tenant_role_uuid`` empty keeps the current role, and memberships the response does not list stay as they are.

Model
-----

.. automodule:: fair_wizard.automation.openid.model
    :members:

