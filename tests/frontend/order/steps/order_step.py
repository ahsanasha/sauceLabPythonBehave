import time

from behave import when, then
from tests.pages import home_page
from tests.pages import cart
from tests.pages import self_information
from tests.pages import checkout_overview

@when("user pick backpack")
def pick_item(context):
    home_page.user_pick_backpack(context)

@when("user pick red shirt")
def pick_redshirt(context):
    home_page.user_pick_redshirt(context)

@when("user pick {qty} random items")
def pick_redshirt(context, qty):
    home_page.user_pick_random_items(context, qty)

    
@then("item successfully picked")
def item_successfully_picked(context):
    home_page.verify_add_item(context)

@when("user click remove")
def remove_item(context):
    pick_item(context)
    time.sleep(1)
    home_page.remove_item(context)

@then("item will be removed")
def item_removed(context):
    home_page.verify_remove_item(context)

@when("user open cart")
def open_cart(context):
    home_page.click_checkout_icon(context)

@when("user click checkout button")
def click_checkout_button(context):
    cart.click_checkout(context)

@when("user fill the first name {first_name}")
def fill_first_name(context, first_name):
    self_information.fill_first_name(context, first_name)

@when("user fill the last name {last_name}")
def fill_last_name(context, last_name):
    self_information.fill_last_name(context, last_name)

@when("user fill postal code {postal_code}")
def fill_postal_code(context, postal_code):
    self_information.fill_postal_code(context, postal_code)

@when("user click continue button")
def click_continue(context):
    self_information.click_continue(context)

@when("user click finish button")
def click_finish(context):
    checkout_overview.click_finish(context)

@then("item successfully ordered")
def assert_item_ordered(context):
    checkout_overview.item_ordered(context)
