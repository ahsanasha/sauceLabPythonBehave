from BDD_common.common_funcs import webcommon

LOGIN_PAGE = {
    'username': {'type': 'id', 'locator': 'user-name'},
    'password': {'type': 'id', 'locator': 'password'},
    'login_button': {'type': 'id', 'locator': 'login-button'},
    'error_message': {'type': 'css selector', 'locator': 'h3[data-test="error"]'}
}

HOME_PAGE = {
    'shopping_cart': {'type': 'id', 'locator': 'shopping_cart_container'},
    'backpack': {'type': 'id', 'locator': 'add-to-cart-sauce-labs-backpack'},
    'red_shirt': {'type': 'id', 'locator': 'add-to-cart-test.allthethings()-t-shirt-(red)'},
    'cart': {'type': 'id', 'locator': 'shopping_cart_container'},
    'cart_badge': {'type': 'class name', 'locator': 'shopping_cart_badge'},
    'remove': {'type': 'id', 'locator': 'remove-sauce-labs-backpack'},
    'add_to_cart': {'type': 'css selector', 'locator': 'button[data-test*=add-to-cart-sauce]'}
}

CART_PAGE = {
    'checkout': {'type': 'id', 'locator': 'checkout'},
    'remove_backpack': {'type': 'id', 'locator': 'remove-sauce-labs-backpack'},
    'continue_shopping': {'type': 'id', 'locator': 'continue-shopping'},
    'sauce_Llabs_backpack': {'type': 'id', 'locator': 'item_4_title_link'}
}

SELF_INFORMATION_PAGE = {
    'first_name': {'type': 'id', 'locator': 'first-name'},
    'last_name': {'type': 'id', 'locator': 'last-name'},
    'postal_code': {'type': 'id', 'locator': 'postal-code'},
    'continue': {'type': 'id', 'locator': 'continue'},
    'cancel': {'type': 'id', 'locator': 'cancel'},
    'error_message': {'type': 'css selector', 'locator': 'h3[data-test="error"]'}
}

CHECKOUT_OVERVIEW_PAGE = {
    'sauce_Llabs_backpack': {'type': 'id', 'locator': 'item_4_title_link'},
    'first_name': {'type': 'id', 'locator': 'first-name'},
    'last_name': {'type': 'id', 'locator': 'last-name'},
    'postal_code': {'type': 'id', 'locator': 'postal-code'},
    'finish': {'type': 'id', 'locator': 'finish'},
    'cancel': {'type': 'id', 'locator': 'cancel'},
    'error_message': {'type': 'css selector', 'locator': 'h3[data-test="error"]'},

}

COMPLETE_PAGE = {
    'back_to_products': {'type': 'id', 'locator': 'back-to-products'}
}

