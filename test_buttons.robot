*** Settings ***
Library    SeleniumLibrary
Library    click_buttons.ClickButtons
Library    BuiltIn

*** Keywords ***
Open Browser Page
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

*** Variables ***
${url}    https://demoqa.com/buttons
# ${button_value}    Click Me
${browser}    chrome

*** Test Cases ***
TestButtons
    Open Browser Page
    Click Selected Button    Click Me
    Click Selected Button    Double Click Me
    Click Selected Button    Right Click Me
    Sleep   3
    Close Browser