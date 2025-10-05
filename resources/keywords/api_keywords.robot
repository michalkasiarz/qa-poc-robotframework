*** Settings ***
Library    ../../libs/user_api.py    WITH NAME    UserAPI
Library    Collections

*** Keywords ***
User Should Exist
    [Arguments]    ${user_id}
    ${response}=    Get User By Id    ${user_id}
    Should Be Equal As Integers    ${response.status_code}    200
    ${json}=    Get User Json By Id    ${user_id}
    Dictionary Should Contain Key    ${json}    id

Create Dummy User
    ${payload}=    Create Dictionary    name=QA Test    username=qaqa    email=qa@example.com
    ${response}=    Create User    ${payload}
    Should Be Equal As Integers    ${response.status_code}    201
