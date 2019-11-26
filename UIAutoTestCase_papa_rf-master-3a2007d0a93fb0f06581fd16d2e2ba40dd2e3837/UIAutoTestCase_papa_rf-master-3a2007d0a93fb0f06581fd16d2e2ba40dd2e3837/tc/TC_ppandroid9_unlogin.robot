*** Settings ***
Library  ../pylib/TC_ppandroid9_unlogin.py


*** Test Cases ***
进行退出登录-001
    test_loginout
    quit
