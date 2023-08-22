from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import CART_PAGE

def click_checkout(context):
    # checkout_type = CART_PAGE['checkout']['type']
    # checkout_string = CART_PAGE['checkout']['locator']
    webcommon.click(context, CART_PAGE['checkout']['type'], CART_PAGE['checkout']['locator'])


def click_continue(context):
    # continue_type = CART_PAGE['continue_shopping']['type']
    # continue_string = CART_PAGE['continue_shopping']['locator']
    webcommon.click(context, CART_PAGE['continue_shopping']['type'], CART_PAGE['continue_shopping']['locator'])


def click_remove_backpack(context):
    # remove_backpack_type = CART_PAGE['remove_backpack']['type']
    # remove_backpack_string = CART_PAGE['remove_backpack']['locator']
    webcommon.click(context, CART_PAGE['remove_backpack']['type'], CART_PAGE['remove_backpack']['locator'])


def navigate_to_backpack_detail(context):
    # backpack_detail_type = CART_PAGE['sauce_Llabs_backpack']['type']
    # backpack_detail_string = CART_PAGE['sauce_Llabs_backpack']['locator']
    webcommon.click(context, CART_PAGE['sauce_Llabs_backpack']['type'], CART_PAGE['sauce_Llabs_backpack']['locator'])

