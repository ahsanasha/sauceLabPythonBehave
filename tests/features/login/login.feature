#Scenario Background
@smokeTest
Feature: Login
  As a user, I want to able to sign in
  SO that I can access all features

  Background:
      Given user go to login page

  @tcId001
  Scenario: Login with valid credential
    When user enters the username
    And user enters the password
    And user clicks login button
    Then user should be navigated to the dashboard

  @tcId002
  Scenario: Login with invalid credential
    When user enters the invalid username
    And user enters the invalid password
    And user clicks login button
    Then user will get the error message
