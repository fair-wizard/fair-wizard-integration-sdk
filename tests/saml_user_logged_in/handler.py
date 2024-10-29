from fair_wizard.automation.saml.wrappers import make_saml_user_logged_in_handler
from fair_wizard.automation.common.wrappers import make_error_handler

try:
    from func import handle_saml_user_logged_in
    handler = make_saml_user_logged_in_handler(handle_saml_user_logged_in)
except Exception as e:
    handler = make_error_handler(e)
