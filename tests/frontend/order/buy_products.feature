Feature: Product purchases

  @tcId005
  Scenario: Add item to cart
    Given user already on home page
    When user pick backpack
    Then item successfully picked

  @tcId006
  Scenario: Remove item from cart
    Given user already on home page
    When user click remove
    Then item will be removed

  @tcId007
  Scenario Outline: Checkout single item
    Given user already on home page
    When user pick backpack
    And user open cart
    And user click checkout button
    And user fill the first name <first_name>
    And user fill the last name <last_name>
    And user fill postal code <postal_code>
    And user click continue button
    And user click finish button
    Then item successfully ordered

    Examples:
      | first_name | last_name  | postal_code |
      | Ahsan      | Khuluk     | 40911       |
      | Zaelani    | Zulkarnaen | 80451       |


  @tcId008
  Scenario Outline: Checkout multiple item
    Given user already on home page
    When user pick backpack
    And user pick red shirt
    And user open cart
    And user click checkout button
    And user fill the first name <first_name>
    And user fill the last name <last_name>
    And user fill postal code <postal_code>
    And user click continue button
    And user click finish button
    Then item successfully ordered

    Examples:
      | first_name | last_name | postal_code |
      | Ferdy      | Ciputra   | 46052       |
      | Maryo      | Osan      | 12456       |
      | ulfa       | Dwi       | 79954       |


  @tcId009
  Scenario Outline: Checkout random item
    Given user already on home page
    When user pick <qty> random items
    And user open cart
    And user click checkout button
    And user fill the first name <first_name>
    And user fill the last name <last_name>
    And user fill postal code <postal_code>
    And user click continue button
    And user click finish button
    Then item successfully ordered

    Examples:
      | first_name | last_name  | postal_code | qty |
      | Ahsan      | Khuluk     | 40911       | 5   |