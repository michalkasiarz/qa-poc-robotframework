*** Settings ***
Resource    ../../resources/keywords/api_keywords.robot

*** Test Cases ***
Get Single User Should Return 200
    User Should Exist    1

Create New Dummy User Should Return 201
    Create Dummy User
