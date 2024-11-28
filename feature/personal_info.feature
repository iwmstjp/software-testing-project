Feature: Saucedemo personal info check

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
    And the 'Cart' link is clicked
    And the 'Checkout' button is clicked

    Scenario Outline: Incorrect personal info input
      Given the 'firstname' field is filled with '<firstname>'
      And the 'lastname' field is filled with '<lastname>'
      And the 'zip' field is filled with '<zip>'
      When the 'Continue' button is clicked
      Then the '<errorMessage>' message(Checkout) is shown
      Examples:
        | firstname    | lastname    | zip       |errorMessage                                                         |
        | [blank]      | [blank]     | [blank]   |Error: First Name is required                                        |
        | First        | [blank]     | [blank]   |Error: Last Name is required                                         |
        | First        | Last        | [blank]   |Error: Postal Code is required                                       |
        | [blank]      | [blank]     | 4028      |Error: First Name is required                                        |
        | First        | [blank]     | 4028      |Error: Last Name is required                                         |