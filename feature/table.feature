Feature: table feature 
    Scenario Outline: table test 
    Given current page is homepage
    When open table page
    And get <text> from <field>
    Examples:
        | text | field | 
        | first_name  | text_table  | 