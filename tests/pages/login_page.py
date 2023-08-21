from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import LOGIN_PAGE


def enter_username(context):
    user_name_type = LOGIN_PAGE['username']['type']
    user_name_string = LOGIN_PAGE['username']['locator']
    webcommon.type_into_element(context, webcommon.get_user_name(context), user_name_type, user_name_string)


def enter_password(context):
    password_type = LOGIN_PAGE['password']['type']
    password_string = LOGIN_PAGE['password']['locator']
    webcommon.type_into_element(context, webcommon.get_password(context), password_type, password_string)

def click_login_button(context):
    button_type = LOGIN_PAGE['login_button']['type']
    button_string = LOGIN_PAGE['login_button']['locator']
    webcommon.click(context, button_type, button_string)


def enter_invalid_user(context):
    user_name_type = LOGIN_PAGE['username']['type']
    user_name_string = LOGIN_PAGE['username']['locator']
    webcommon.type_into_element(context, 'userNotFound', user_name_type, user_name_string)


def enter_wrong_pass(context):
    password_type = LOGIN_PAGE['password']['type']
    password_string = LOGIN_PAGE['password']['locator']
    webcommon.type_into_element(context, 'qwerty', password_type, password_string)


def user_receive_error_message(context):
    error_type = LOGIN_PAGE['error_message']['type']
    error_string = LOGIN_PAGE['error_message']['locator']
    webcommon.assert_element_visible(context, error_type, error_string)
