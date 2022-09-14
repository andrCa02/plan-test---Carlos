Feature: Login page feature
    Scenario: login successfully
    Given current page is loginPage
    When I click login button
    When I fill fields with any data
    And I click on login button
    Then A failture message should appear on page

    Scenario: blanks fields
    Given current page is loginPage
    When I click on login button
    Then A failture message should appear on page