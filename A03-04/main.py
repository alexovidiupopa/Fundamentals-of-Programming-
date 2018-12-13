'''
Assignment 03-04 - Problem 4 - Bank Account
'''

from business import *
from userInterface import printAccount,UI_list,readCommand
from tests import runTests

def start():
    account = []
    commands = {"list":UI_list,"sum":sumOfType,"max":max_type_day}
    modifiers={"add":add_listing,"insert":insert_listing,"remove":remove_listing,"filter":filter_listings}
    runTests(account)
    oldAccount=[]
    printAccount(account)
    printHello()
    while True:
        command = readCommand()
        if command[0] == "exit":
            print("The application is now closed.")
            return
        elif command[0]=="help":
            printHelp()
            continue
        elif command[0] in commands:
            commands[command[0]](account,command)
            continue
        elif command[0]=="replace":
            account = replace_listing(account, command, oldAccount)
            printAccount(account)
            continue
        elif command[0] in modifiers:
            modifiers[command[0]](account,command,oldAccount)
            printAccount(account)
            continue
        elif command[0] == "undo":
            account = mainUndo(account,oldAccount,command)
            printAccount(account)
            continue
        else: 
            invalidCommand()
            continue

start()