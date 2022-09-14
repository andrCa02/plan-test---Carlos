Feature: action feature 
    Scenario: drop here test 
    Given current page is homepage
    When open action page
    When I drag to my target

    Scenario: double click test
    Given current page is homepage
    When open action page
    When I double click

    Scenario: holding test
    Given current page is homepage
    When open action page
    When I hold the button
    