from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import CART_PAGE

def click_checkout(context):
    webcommon.click(context, CART_PAGE['checkout']['type'], CART_PAGE['checkout']['locator'])
    webcommon.assert_url_contains(context, '/checkout-step-one.html')

def click_continue(context):
    webcommon.click(context, CART_PAGE['continue_shopping']['type'], CART_PAGE['continue_shopping']['locator'])
    webcommon.assert_url_contains(context, '/checkout-step-two.html')

def click_remove_backpack(context):
    webcommon.click(context, CART_PAGE['remove_backpack']['type'], CART_PAGE['remove_backpack']['locator'])


def navigate_to_backpack_detail(context):
    webcommon.click(context, CART_PAGE['sauce_Llabs_backpack']['type'], CART_PAGE['sauce_Llabs_backpack']['locator'])
    webcommon.assert_url_contains(context, '/inventory-item.html?id=4')
