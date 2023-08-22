from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import LOGIN_PAGE


def enter_username(context):
    # user_name_type = LOGIN_PAGE['username']['type']
    # user_name_string = LOGIN_PAGE['username']['locator']
    webcommon.type_into_element(context, webcommon.get_user_name(context), LOGIN_PAGE['username']['type'], LOGIN_PAGE['username']['locator'])


def enter_password(context):
    # password_type = LOGIN_PAGE['password']['type']
    # password_string = LOGIN_PAGE['password']['locator']
    webcommon.type_into_element(context, webcommon.get_password(context), LOGIN_PAGE['password']['type'], LOGIN_PAGE['password']['locator'])

def click_login_button(context):
    # button_type = LOGIN_PAGE['login_button']['type']
    # button_string = LOGIN_PAGE['login_button']['locator']
    webcommon.click(context, LOGIN_PAGE['login_button']['type'], LOGIN_PAGE['login_button']['locator'])


def enter_invalid_user(context):
    # user_name_type = LOGIN_PAGE['username']['type']
    # user_name_string = LOGIN_PAGE['username']['locator']
    webcommon.type_into_element(context, 'userNotFound', LOGIN_PAGE['username']['type'], LOGIN_PAGE['username']['locator'])


def enter_wrong_pass(context):
    # password_type = LOGIN_PAGE['password']['type']
    # password_string = LOGIN_PAGE['password']['locator']
    webcommon.type_into_element(context, 'qwerty', LOGIN_PAGE['password']['type'], LOGIN_PAGE['password']['locator'])


def user_receive_error_message(context):
    # error_type = LOGIN_PAGE['error_message']['type']
    # error_string = LOGIN_PAGE['error_message']['locator']
    webcommon.assert_element_visible(context, LOGIN_PAGE['error_message']['type'], LOGIN_PAGE['error_message']['locator'])
