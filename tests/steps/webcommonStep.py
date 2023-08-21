from behave import given, step
from BDD_common.common_funcs import webcommon
from tests.pages import login_page


@step("user go to login page")
@given("user open web")
def go_to_url(context):
    webcommon.go_to(context)


@given("user already on home page")
def do_login(context):
    go_to_url(context)
    login_page.enter_username(context)
    login_page.enter_password(context)
    login_page.click_login_button(context)


