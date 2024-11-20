Feature: Saucedemo cart count

  Background:
    Given the home page is opened
    

    Scenario Outline: Add items to the cart
      Given the 'Username' field is filled with 'standard_user'
      And the 'Password' field is filled with 'secret_sauce'
      And the 'Login':login button is clicked
      And the '<item1>' cart button is clicked
      And the '<item2>' cart button is clicked
      Then the 'Cart_count'  is '<number>'. Remove '<item1>' and '<item2>'
      Examples:
        | item1                       |item2                     | number    | 
        | Sauce Labs Backpack         | Sauce Labs Bike Light    | 2         |
        | [blank]                     | Sauce Labs Bike Light    | 1         |
        | Sauce Labs Onesie           | [blank]                  | 1         |
        | Sauce Labs Fleece Jacket    | [blank]                  | 1         |
        | Sauce Labs Bolt T-Shirt     | Sauce Labs Bike Light    | 2         |
        | [blank]                     | [blank]                  | 0         |
