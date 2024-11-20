Feature: Saucedemo logout

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
    And the 'Menu' button is clicked
  Scenario: Logout
    When the 'Logout' button is clicked
    Then the 'https://www.saucedemo.com/' is shown