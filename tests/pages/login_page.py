from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import LOGIN_PAGE


def enter_username(context):
    webcommon.type_into_element(context, webcommon.get_user_name(context), LOGIN_PAGE['username']['type'], LOGIN_PAGE['username']['locator'])


def enter_password(context):
    webcommon.type_into_element(context, webcommon.get_password(context), LOGIN_PAGE['password']['type'], LOGIN_PAGE['password']['locator'])

def click_login_button(context):
    webcommon.click(context, LOGIN_PAGE['login_button']['type'], LOGIN_PAGE['login_button']['locator'])


def enter_invalid_user(context):
    webcommon.type_into_element(context, 'userNotFound', LOGIN_PAGE['username']['type'], LOGIN_PAGE['username']['locator'])


def enter_wrong_pass(context):
    webcommon.type_into_element(context, 'qwerty', LOGIN_PAGE['password']['type'], LOGIN_PAGE['password']['locator'])


def user_receive_error_message(context):
    webcommon.assert_element_visible(context, LOGIN_PAGE['error_message']['type'], LOGIN_PAGE['error_message']['locator'])


def verify_login_page(context):
    webcommon.assert_element_visible(context, LOGIN_PAGE['login_container']['type'],LOGIN_PAGE['login_container']['locator'])