import time

from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import HOME_PAGE
import random


def should_be_navigated_to_dashboard(context):
    webcommon.assert_element_visible(context, HOME_PAGE['shopping_cart']['type'], HOME_PAGE['shopping_cart']['locator'])
    webcommon.assert_url_contains(context,  '/inventory.html')

def user_pick_backpack(context):
    webcommon.click(context, HOME_PAGE['backpack']['type'], HOME_PAGE['backpack']['locator'])


def user_pick_redshirt(context):
    webcommon.click(context, HOME_PAGE['red_shirt']['type'], HOME_PAGE['red_shirt']['locator'])


def user_pick_random_items(context, qty):
    cart_btn = HOME_PAGE['add_to_cart']
    cart_btn_type = cart_btn['type']
    cart_btn_text = cart_btn['locator']

    cart_btn = webcommon.find_elements(context, cart_btn_type, cart_btn_text)
    random_button = random.sample(cart_btn, int(qty))

    for i in random_button:
        webcommon.click(context, cart_btn_type, cart_btn_text)
        time.sleep(1)

def verify_add_item(context):
    webcommon.assert_element_contains_text(context, '1', HOME_PAGE['cart_badge']['type'],
                                           HOME_PAGE['cart_badge']['locator'])


def remove_item(context):
    webcommon.click(context, HOME_PAGE['remove']['type'], HOME_PAGE['remove']['locator'])


def verify_remove_item(context):
    try:
        if webcommon.is_element_visible(
                webcommon.find_element(context, HOME_PAGE['cart_badge']['type'], HOME_PAGE['cart_badge']['locator'])):
            print("Test Failed")

        else:
            print("Test Success")

    except:
        print('Element not found')


def click_checkout_icon(context):
    webcommon.click(context, HOME_PAGE['cart']['type'], HOME_PAGE['cart']['locator'])

    webcommon.assert_url_contains(context, '/cart.html')
