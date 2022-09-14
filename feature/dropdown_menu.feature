Feature: text appear feature 
    Scenario: open text box
    Given current page is homepage
    When open dropown menu page
    And click on dropdown menu/linguages
    And click on second dropdown menu
    And click on the third dropdown menu

    Scenario: checkbox test
    Given current page is homepage
    When open dropown menu page
    And I click on the checkbox options

    Scenario: radio test
    Given current page is homepage
    When open dropown menu page
    And I click on each radio options