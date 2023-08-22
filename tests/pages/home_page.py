from BDD_common.common_funcs import webcommon
from BDD_common.common_configs.locators_config import HOME_PAGE


def should_be_navigated_to_dashboard(context):
    # shopping_cart_type = HOME_PAGE['shopping_cart']['type']
    # shopping_cart_string = HOME_PAGE['shopping_cart']['locator']
    webcommon.assert_element_visible(context, HOME_PAGE['shopping_cart']['type'], HOME_PAGE['shopping_cart']['locator'])


def user_pick_backpack(context):
    # bag_type = HOME_PAGE['backpack']['type']
    # bag_string = HOME_PAGE['backpack']['locator']
    webcommon.click(context, HOME_PAGE['backpack']['type'], HOME_PAGE['backpack']['locator'])


def user_pick_redshirt(context):
    # red_shirt_type = HOME_PAGE['red_shirt']['type']
    # red_shirt_string = HOME_PAGE['red_shirt']['locator']
    webcommon.click(context, HOME_PAGE['red_shirt']['type'], HOME_PAGE['red_shirt']['locator'])


def verify_add_item(context):
    #   cart_type = HOME_PAGE['cart_badge']['type']
    #   cart_string = HOME_PAGE['cart_badge']['locator']
    webcommon.assert_element_contains_text(context, '1', HOME_PAGE['cart_badge']['type'],
                                           HOME_PAGE['cart_badge']['locator'])


def remove_item(context):
    # remove_type = HOME_PAGE['remove']['type']
    # remove_string = HOME_PAGE['remove']['locator']
    webcommon.click(context, HOME_PAGE['remove']['type'], HOME_PAGE['remove']['locator'])


def verify_remove_item(context):
    # cart_type = HOME_PAGE['cart_badge']['type']
    # cart_string = HOME_PAGE['cart_badge']['locator']
    try:
        if webcommon.is_element_visible(
                webcommon.find_element(context, HOME_PAGE['cart_badge']['type'], HOME_PAGE['cart_badge']['locator'])):
            print("Test Failed")

        else:
            print("Test Success")

    except:
        print('Element not found')


def click_checkout_icon(context):
    # cart_type = HOME_PAGE['cart']['type']
    # cart_string = HOME_PAGE['cart']['locator']
    webcommon.click(context, HOME_PAGE['cart']['type'], HOME_PAGE['cart']['locator'])
