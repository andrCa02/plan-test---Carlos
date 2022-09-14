Feature: hidden feature 
    Scenario: buttons test 
    Given current page is homepage
    When open hidden page
    And click on Not Displayed button
    #And click on visibility hidden button
    And click on zero opacity button
    
    Scenario Outline: not displayed button test
    Given current page is homepage
    When open hidden page
    And click on Not Displayed button
    Then the messenge that appeared is <message> on <field>
    Examples:
        | message | field |
        | not_displayed  | Not_displayed_message |

    Scenario Outline: visibility test
    Given current page is homepage
    When open hidden page
    And click on visibility hidden button
    Then the messenge that appeared is <message> on <field>
    Examples:
        | message | field |
        | visibility_hidden  | visibility_hidden_message |

    Scenario Outline: zero opacity test
    Given current page is homepage
    When open hidden page
    And click on zero opacity button
    Then the messenge that appeared is <message> on <field>
    Examples:
        | message | field |
        | zero_opacity  | zero_opacity_message |



