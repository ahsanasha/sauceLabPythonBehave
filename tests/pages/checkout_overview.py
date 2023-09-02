from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import CHECKOUT_OVERVIEW_PAGE
from BDD_common.common_configs.locators_config import COMPLETE_PAGE

def click_finish(context):
    webcommon.click(context, CHECKOUT_OVERVIEW_PAGE['finish']['type'], CHECKOUT_OVERVIEW_PAGE['finish']['locator'])


def item_ordered(context):
    webcommon.assert_element_visible(context, COMPLETE_PAGE['back_to_products']['type'], COMPLETE_PAGE['back_to_products']['locator'])


def back_home(context):
    webcommon.click(context, COMPLETE_PAGE['back_to_products']['type'], COMPLETE_PAGE['back_to_products']['locator'])
