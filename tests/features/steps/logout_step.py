from behave import when, then
from tests.pages import home_page, login_page


@when(u'user clicks on menu icon')
def go_to_menu(context):
    home_page.open_menu(context)

@when(u'user clicks on logout submenu')
def logout(context):
    home_page.click_logout(context)

@then(u'user should be navigated to the login page')
def navigated_to_login(context):
    login_page.verify_login_page(context)