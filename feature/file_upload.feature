Feature: file upload feature 
    Scenario Outline: upload test 
    Given current page is homepage
    When open file upload page
    And I choose my <file>
    And I click on submit button - file upload
    Then the messenge appeared
    Examples:
        | file | 
        | C:\Users\andrca02\PycharmProjects\Projetc1\feature\steps\fileUpload.txt | 