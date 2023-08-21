from behave import given, step
from BDD_common.common_funcs import webcommon
from frontend.LoginPage.steps import login_step


# @given(u'user go to login page')
# # @given("user go to login")
# def go_to_url(context):
#     webcommon.go_to(context)
#
#
# @given("user already on dashboard page")
# def do_login(context):
#     go_to_url(context)
#     login_step.enter_user_name(context)
#     login_step.enter_password(context)
#     login_step.click_login_button(context)
#
