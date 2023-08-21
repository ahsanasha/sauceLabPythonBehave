from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import HOME_PAGE


def should_be_navigated_to_dashboard(context):
    shopping_cart_type = HOME_PAGE['shopping_cart']['type']
    shopping_cart_string = HOME_PAGE['shopping_cart']['locator']
    webcommon.assert_element_visible(context, shopping_cart_type, shopping_cart_string)


def user_pick_item(context):
    bag_type = HOME_PAGE['backpack']['type']
    bag_string = HOME_PAGE['backpack']['locator']
    webcommon.click(context, bag_type, bag_string)


def verify_add_item(context):
    cart_type = HOME_PAGE['cart_badge']['type']
    cart_string = HOME_PAGE['cart_badge']['locator']
    webcommon.assert_element_contains_text(context, '1', cart_type, cart_string)


def remove_item(context):
    remove_type = HOME_PAGE['remove']['type']
    remove_string = HOME_PAGE['remove']['locator']
    webcommon.click(context, remove_type, remove_string)


def verify_remove_item(context):
    cart_type = HOME_PAGE['cart_badge']['type']
    cart_string = HOME_PAGE['cart_badge']['locator']
    try:
        if webcommon.is_element_visible(webcommon.find_element(context, cart_type, cart_string)):
            print("Test Failed")

        else:
            print("Test Success")

    except:
        print('Element not found')


def click_checkout_icon(context):
    cart_type = HOME_PAGE['cart']['type']
    cart_string = HOME_PAGE['cart']['locator']
    webcommon.click(context, cart_type, cart_string)