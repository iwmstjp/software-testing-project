Feature: Saucedemo continue shopping button

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario: check continue shopping button works
    Given the 'Cart' link is clicked
    When the 'ContinueShopping' button is clicked
    Then the 'inventory.html' page is shown
