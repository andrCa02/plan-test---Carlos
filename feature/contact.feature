Feature: contact us feature
    Scenario: page test sucess
    Given current page is homepage
    When I click contact button
    And I fill fields with correct data
    And I click on submit button
    Then A sucess message should appear on page

    Scenario: failure test
    Given current page is homepage
    When I click contact button
    When I click on submit button
    Then A failure messagem should appear
