Feature: Saucedemo sort order

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
  Scenario: Check sorting by 'lohi' option
    When the 'lohi' option is clicked
    Then the 'Sauce Labs Onesie' is top