Feature: date picker feature 
    Scenario: calendar past test 
    Given current page is homepage
    When open date picker page
    And I choose the date in the past

    Scenario: calendar future test 
    Given current page is homepage
    When open date picker page
    And I choose the date in the future