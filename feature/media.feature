Feature: social media on footer

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario Outline: show social media on different pages
    When the '<item>' item button is clicked
    Then the '<media>' icon is shown
    Examples:
      | item                      | media   |
      | Sauce Labs Backpack       | Twitter |
      | Sauce Labs Backpack       | Facebook|
      | Sauce Labs Backpack       | LinkedIn|
      | Sauce Labs Bolt T-Shirt   | Twitter |
      | Sauce Labs Onesie         | Twitter |
