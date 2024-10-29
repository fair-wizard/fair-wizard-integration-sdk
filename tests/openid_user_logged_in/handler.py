from fair_wizard.automation.openid.wrappers import make_openid_user_logged_in_handler
from fair_wizard.automation.common.wrappers import make_error_handler

try:
    from func import handle_openid_user_logged_in
    handler = make_openid_user_logged_in_handler(handle_openid_user_logged_in)
except Exception as e:
    handler = make_error_handler(e)
