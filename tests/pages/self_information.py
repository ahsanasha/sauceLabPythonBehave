from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import SELF_INFORMATION_PAGE

def fill_first_name(context, first_name):
    webcommon.type_into_element(context, first_name, SELF_INFORMATION_PAGE['first_name']['type'], SELF_INFORMATION_PAGE['first_name']['locator'])


def fill_last_name(context, last_name):
    webcommon.type_into_element(context, last_name, SELF_INFORMATION_PAGE['last_name']['type'], SELF_INFORMATION_PAGE['last_name']['locator'])


def fill_postal_code(context, postal_code):
    webcommon.type_into_element(context, postal_code, SELF_INFORMATION_PAGE['postal_code']['type'], SELF_INFORMATION_PAGE['postal_code']['locator'])

def click_continue(context):
    webcommon.click(context, SELF_INFORMATION_PAGE['continue']['type'], SELF_INFORMATION_PAGE['continue']['locator'])

def click_cancel(context):
    webcommon.click(context, SELF_INFORMATION_PAGE['cancel']['type'], SELF_INFORMATION_PAGE['cancel']['locator'])
