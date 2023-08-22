from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import CHECKOUT_OVERVIEW_PAGE
from BDD_common.common_configs.locators_config import COMPLETE_PAGE
def click_finish(context):
    # finish_type = CHECKOUT_OVERVIEW_PAGE['finish']['type']
    # finish_string = CHECKOUT_OVERVIEW_PAGE['finish']['locator']
    webcommon.click(context, CHECKOUT_OVERVIEW_PAGE['finish']['type'], CHECKOUT_OVERVIEW_PAGE['finish']['locator'])


def item_ordered(context):
    # back_home_type = COMPLETE_PAGE['back_to_products']['type']
    # back_home_string = COMPLETE_PAGE['back_to_products']['locator']
    webcommon.assert_element_visible(context, COMPLETE_PAGE['back_to_products']['type'], COMPLETE_PAGE['back_to_products']['locator'])


def back_home(context):
    # back_home_type = COMPLETE_PAGE['back_to_products']['type']
    # back_home_string = COMPLETE_PAGE['back_to_products']['locator']
    webcommon.click(context, COMPLETE_PAGE['back_to_products']['type'], COMPLETE_PAGE['back_to_products']['locator'])
