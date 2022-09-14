Feature: button click feature
    Scenario: carousel test 
    Given current page is homepage
    When I click page object button
    And test caousel    
    And check images

    Scenario: buttons test
    Given current page is homepage
    When I click page object button
    And I click on buttons and check

    Scenario: boxes test
    Given current page is homepage
    When I click page object button
    And check if the boxes loaded