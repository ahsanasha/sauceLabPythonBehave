from behave import when, then
from tests.pages import home_page, login_page


@when("user enters the username")
def enter_user_name(context):
    login_page.enter_username(context)


@when("user enters the password")
def enter_password(context):
    login_page.enter_password(context)


@when(u'user clicks login button')
def click_login_button(context):
    login_page.click_login_button(context)


@then(u'user should be navigated to the dashboard')
def should_be_navigated_to_dashboard(context):
    home_page.should_be_navigated_to_dashboard(context)


@when(u'user enters the invalid username')
def enter_invalid_user(context):
    login_page.enter_invalid_user(context)


@when(u'user enters the invalid password')
def enter_wrong_pass(context):
    login_page.enter_wrong_pass(context)


@then("user will get the error message")
def user_receive_error_message(context):
    login_page.user_receive_error_message(context)


