Feature: The All items button on the Menu

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
    And the 'Cart' link is clicked
    And the 'Menu' button is clicked
  Scenario: Access to inventory.html
    When the 'All items' button is clicked
    Then the 'inventory.html' page is shown
    