Feature: to do list feature
    Scenario: add new todo
    Given current page is homepage
    When I click on to do button
    And write something and submit
    And check

    Scenario: delete one task
    Given current page is homepage
    When I click on to do button
    And I click on delete button

    Scenario: check task
    Given current page is homepage
    When I click on to do button
    And I finished a task