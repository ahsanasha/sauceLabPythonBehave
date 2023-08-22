from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import SELF_INFORMATION_PAGE

def fill_first_name(context, first_name):
    # first_name_type = SELF_INFORMATION_PAGE ['first_name']['type']
    # first_name_string = SELF_INFORMATION_PAGE['first_name']['locator']
    webcommon.type_into_element(context, first_name, SELF_INFORMATION_PAGE['first_name']['type'], SELF_INFORMATION_PAGE['first_name']['locator'])


def fill_last_name(context, last_name):
    # last_name_type = SELF_INFORMATION_PAGE['last_name']['type']
    # last_name_string = SELF_INFORMATION_PAGE['last_name']['locator']
    webcommon.type_into_element(context, last_name, SELF_INFORMATION_PAGE['last_name']['type'], SELF_INFORMATION_PAGE['last_name']['locator'])


def fill_postal_code(context, postal_code):
    # postal_code_type = SELF_INFORMATION_PAGE['postal_code']['type']
    # postal_code_string = SELF_INFORMATION_PAGE['postal_code']['locator']
    webcommon.type_into_element(context, postal_code, SELF_INFORMATION_PAGE['postal_code']['type'], SELF_INFORMATION_PAGE['postal_code']['locator'])

def click_continue(context):
    # continue_type = SELF_INFORMATION_PAGE['continue']['type']
    # continue_string = SELF_INFORMATION_PAGE['continue']['locator']
    webcommon.click(context, SELF_INFORMATION_PAGE['continue']['type'], SELF_INFORMATION_PAGE['continue']['locator'])

def click_cancel(context):
    # cancel_type = SELF_INFORMATION_PAGE['cancel']['type']
    # cancel_string = SELF_INFORMATION_PAGE['cancel']['locator']
    webcommon.click(context, SELF_INFORMATION_PAGE['cancel']['type'], SELF_INFORMATION_PAGE['cancel']['locator'])
