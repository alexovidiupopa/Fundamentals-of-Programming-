from validators import *
from model import *
from business import *

def printPhones(phones):
    if not phones:
        print("Empty list!")
        return
    for phone in phones:
        print("Manuf:" + getManufacturer(phone) + "  Model:" + getModel(phone) + "  Price:" + str(getPrice(phone)))

def uiAdd(phones):
    print("You have chosen to add a phone! Please enter its manufacturer: ")
    manufacturer = input()
    print("Enter its model:")
    model = input()
    print("Enter its price")
    price = int(input())
    if validateAdd(manufacturer, model, price) == False: 
        print("Error! One of your fields has a length smaller than 3. The phone cannot be added.")
        return 
    newPhone = createPhone(manufacturer, model, price)
    addPhone(phones, newPhone)

def uiRemove(phones):
    print("You have chosen to remove a phone! Please enter its manufacturer: ")
    manufacturer = input()
    print("Enter its model:")
    model = input()
    if removePhone(phones, manufacturer, model) == False: 
        print("There is no such phone to be removed! ")
        return 

def uiIncrease(phones):
    print("You have chosen to increase the price of a certain phone! Please enter the manufacturer:")
    manufacturer = input()
    print("Enter its model:")
    model = input()
    print("PLease enter the amount you want it to be increased with:")
    amount = int(input())
    if increaseAmount(phones,manufacturer,model,amount) == False:
        print("No such phone exists!")
        return
    
def uiList(phones):
    print("You have chosen to print all the phones in increasing order by their price. Here goes: ")
    phones.sort(key = getPrice)
    printPhones(phones)
      
def console(phones):
    print("Welcome!")
    commands = {"1":uiAdd,"2":uiRemove,"3":uiIncrease,"4":uiList}
    while True: 
        print(">>")
        userInput = input()
        if userInput == "exit":
            print("Goodbye!")
            return
        elif userInput in commands:
            commands[userInput](phones)
        else: 
            print("No such command!")


