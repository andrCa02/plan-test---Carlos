Feature: autocomplete feature 
    Scenario Outline: food item test 
    Given current page is homepage
    When open autocomplete page
    And when i write <word>
    Then I compare <field> with <expectation>
    Examples:
        | word | expectation |field |
        | ap  | auto_complete | input_autocomplete |