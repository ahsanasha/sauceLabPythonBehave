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
      | Matt       | Shadow    | 78433       |
      | Monkey     | D Luffy   | 80451       |
      | Garth      | Brooks    | 78433       |


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
      | Mickey     | Rourke    | 79954       |
      | Bruce      | Willis    | 89562       |
      | Chuck      | Norris    | 02137       |


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
      | Dakota     | Fanning   | 40911       | 1   |
      | Audrey     | Hepburn   | 12456       | 2   |
      | Naomi      | Judd      | 79954       | 3   |
      | River      | Phoenix   | 21354       | 4   |
      | Demi       | Moore     | 78433       | 5   |