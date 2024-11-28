Feature: Saucedemo checkout

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
    And the 'Cart' link is clicked
    And the 'Checkout' button is clicked
    And the 'firstname' field is filled with 'first'
    And the 'lastname' field is filled with 'last'
    And the 'zip' field is filled with '4028'
    And the 'Continue' button is clicked
  Scenario: Complete checkout
    When the 'Finish' button is clicked
    Then the 'checkout-complete.html' page is shown
    