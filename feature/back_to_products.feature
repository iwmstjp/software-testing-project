Feature: back to products button

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
  Scenario Outline: On each items pages, the button works
    Given the '<item>' item button is clicked
    When the 'Back to products' button is clicked
    Then the 'inventory.html' page is shown
    Examples:
      | item                        | 
      | Sauce Labs Backpack         |
      | Sauce Labs Bike Light       |
      | Sauce Labs Bolt T-Shirt     |
      | Sauce Labs Fleece Jacket    |
      | Sauce Labs Onesie           |
