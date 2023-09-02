@smokeTest
Feature: Logout
  As a user, I want to able to logout

  Background:
    Given user already on home page

  @tcId015
  Scenario: Logout when user in product page
    When user clicks on menu icon
    And user clicks on logout submenu
    Then user should be navigated to the login page

  @tcId016
  Scenario: Logout when user in cart page
    When user selects backpack
    And user opens cart
    And user clicks on menu icon
    And user clicks on logout submenu
    Then user should be navigated to the login page
