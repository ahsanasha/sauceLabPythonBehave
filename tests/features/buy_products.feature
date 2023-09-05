Feature: Product purchases

  @tcId005
  Scenario: Add item to cart
    Given user already on home page
    When user selects backpack
    Then item successfully picked

  @tcId006
  Scenario: Remove item from cart
    Given user already on home page
    When user clicks remove
    Then item will be removed

  @tcId007
  Scenario Outline: Checkout single item
    Given user already on home page
    When user selects backpack
    And user opens cart
    And user clicks checkout button
    And user enters the first name <first_name>
    And user enters the last name <last_name>
    And user enters postal code <postal_code>
    And user clicks continue button
    And user clicks finish button
    Then item successfully ordered

    Examples:
      | first_name | last_name | postal_code |
      | Hayley     | Hayley    | 40911       |
      | John       | Lennon    | 80451       |
      | Marsh      | Mellow    | 09213       |

  @tcId008
  Scenario Outline: Checkout multiple item
    Given user already on home page
    When user selects backpack
    And user selects red shirt
    And user opens cart
    And user clicks checkout button
    And user enters the first name <first_name>
    And user enters the last name <last_name>
    And user enters postal code <postal_code>
    And user clicks continue button
    And user clicks finish button
    Then item successfully ordered

    Examples:
      | first_name | last_name | postal_code |
      | Billie     | Joe       | 46052       |
      | Adam       | Levine    | 12456       |
      | Budy       | Dalton    | 24563       |


  @tcId009
  Scenario Outline: Checkout random item
    Given user already on home page
    When user selects <qty> random items
    And user opens cart
    And user clicks checkout button
    And user enters the first name <first_name>
    And user enters the last name <last_name>
    And user enters postal code <postal_code>
    And user clicks continue button
    And user clicks finish button
    Then item successfully ordered

    Examples:
      | first_name | last_name | postal_code | qty |
      | Audrey     | Hepburn   | 12456       | 2   |
      | Naomi      | Judd      | 79954       | 3   |
      | River      | Phoenix   | 21354       | 4   |
