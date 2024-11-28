Feature: Saucedemo cart remove

  Background:
    Given the home page is opened
    Given the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login':login button is clicked
    And the 'Sauce Labs Backpack' cart button is clicked
    And the 'Sauce Labs Onesie' cart button is clicked
    And the 'Sauce Labs Bolt T-Shirt' cart button is clicked  
  Scenario Outline: Remove items from the cart
    And the '<item1>' removed button is clicked
    And the '<item2>' removed button is clicked
    Then the 'Cart_count'  is '<number>'. Reset state
    Examples:
      | item1                       |item2                     | number    | 
      | Sauce Labs Backpack         | Sauce Labs Onesie        | 1         |
      | Sauce Labs Backpack         | [blank]                  | 2         |
      | Sauce Labs Backpack         | Sauce Labs Bolt T-Shirt  | 1         |
      | Sauce Labs Bolt T-Shirt     | Sauce Labs Onesie        | 1         |
      | Sauce Labs Onesie           | [blank]                  | 2         |
      | Sauce Labs Bolt T-Shirt     | [blank]                  | 2         |

