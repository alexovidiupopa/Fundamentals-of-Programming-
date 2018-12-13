from utilities import *
'''    
UI Functions
'''
def readCommand():
    '''
    Reads the command, splitting it into words, each word now being stored inside an array on one position.
    '''
    print(">")
    command = input()
    newCommand = command.lower().split(' ')
    return newCommand

def UI_add_listing(command):
    '''
    Input: command - keyboard input
    Output: a new entry of the specified type (day-amount-type-description)
    Raises: ValueError for incorrect input
    Remarks: in this function, the "day" from the created listing is the current day, as it needs to add a listing to the current day. 
    '''
    type = ""
    description =""
    amount = -1
    if len(command)!=4:
        raise ValueError
    amount = tryAmount(command[1])
    if amount == -1: 
        raise ValueError
    type = tryType(command[2])
    if type==-1:
        raise ValueError
    description = command[3]
    day = getCurrentDay()
    return createEntry(day, amount, type, description)

def UI_insert_listing(command):
    '''
    Input: command - keyboard input
    Output: a new entry of the specified type (day-amount-type-description)
    Raises: ValueError for incorrect input
    '''
    type = ""
    description =""
    amount = -1
    day = -1 
    if len(command)!=5:
        raise ValueError
    day = tryDay(command[1])
    if day == -1:
        raise ValueError
    amount = tryAmount(command[2])
    if amount == -1: 
        raise ValueError
    type = tryType(command[3])
    if type==-1:
        raise ValueError
    description = command[4]
    return createEntry(day, amount, type, description)

def UI_remove_listing(account,command):
    '''
    Input:account- the list of all the listings; command - the input given by the user.
    Output: the new list formed in the respective function, depending on what the command is (remove a type, remove a day, remove from a day to another)
    Raises: ValueError for incorrect input
    '''
    
    if len(command)>4 or len(command)==3 or len(command)==1:
        raise ValueError
    if len(command)==2:
        type = tryType(command[1])
        if type == -1: 
            day = tryDay(command[1])
            if day == -1: 
                raise ValueError
            else: 
                return [day,day]
        else: 
            return [type]
    if len(command) == 4:
        dayStart = tryDay(command[1])
        if dayStart == -1: 
                raise ValueError
        if command[2]!="to":
            raise ValueError
        dayEnd = tryDay(command[3])
        if dayEnd == -1:
            raise ValueError
        if dayStart>dayEnd:
            raise ValueError
        return [dayStart,dayEnd]
    
def UI_replace_listing(account,command):
    '''
    Input: account- the list of all the listings; command - the input given by the user. 
    Output: result- the new list, with its necessary modifications, more specifically, the old amount of the day and type specified in the command is replaced with the new amount from the command
    Remarks: -in this case, the command is automatically incorrect if its length is not 6.
             -the program will never access this function unless the first command word is "replace", so it's not necessary to check the first word from the command
    Raises: ValueError for incorrect input
    '''
    if len(command)!=6:
        raise ValueError
    day = tryDay(command[1])
    if day == -1: 
        raise ValueError
    type = tryType(command[2])
    if type == -1: 
        raise ValueError
    description = command[3]
    if command[4]!="with":
        raise ValueError
    newAmount = tryAmount(command[5])
    if newAmount == -1:
        raise ValueError
    return createEntry(day,newAmount,type,description)
    

def UI_list(account,command):
    '''
    Input: account- the list of all the listings; command - the input given by the user. 
    Output: executes the necessary task, depending on what the input is.
    Remarks: -in this case, the command is automatically incorrect if its length is greater than 3.
             -the program will never access this function unless the first command word is "list", and if it is the only one, it simply prints out all the listings
    '''
    length = len(command)
    if length>3:
        invalidCommand()
        return 
    if length == 1: 
        printAccount(account)
        return
    if length == 2:
        type = tryType(command[1])
        if type == -1:
            invalidCommand()
            return 
        printAccountOfType(account,type)
    if length == 3:
        if command[1]=="<" or command[1]==">" or command[1]=="=":
            amount = tryAmount(command[2])
            if amount == -1:
                invalidCommand()
                return
            printAccountWithOperator(account,command[1],amount)
        elif command[1]=="balance":
            day = tryDay(command[2])
            if day == -1:
                invalidCommand()
                return
            printBalanceAtGivenDay(account,day)
        else:
            invalidCommand()
            return

def UI_sum(account,command):
    '''
    Input:account- the list of all the listings; command - the input given by the user
    Output: type if the input is correct
    Raises: ValueError if the input is incorrect
    '''
    if len(command)!=2:
        raise ValueError
    type = tryType(command[1])
    if type == -1: 
        raise ValueError
    return type

def UI_max(account,command):
    '''
    Input:account- the list of all the listings; command - the input given by the user
    Output: an array of the format [type,day] if the input is correct
    Raises: ValueError if the input is incorrect
    '''
    if len(command)!=3:
        raise ValueError
    type = tryType(command[1])
    if type == -1: 
        raise ValueError
    day = tryDay(command[2])
    if day == -1: 
        raise ValueError
    return [type,day]

def UI_filter(account,command):
    '''
    Input:account- the list of all the listings; command - the input given by the user
    Output: an array of the format [type] or [type,day] if the input is correct, depending on the input
    Raises: ValueError if the input is incorrect
    '''
    if len(command)>3 or len(command)==1:
        raise ValueError
    type = tryType(command[1])
    if type == -1:
        raise ValueError
    if len(command)==2: 
        return [type]
    amount = tryAmount(command[2])
    if amount == -1:
        raise ValueError
    return [type,amount]

def UI_undo(command,oldAccount):
    '''
    Input: command- the input given by the user, oldAccount- the account who keeps track of all the previous accounts
    Output: True if one can still undo
    Raises: ValueError otherwise
    '''
    if len(command)!=1:
        invalidCommand()
        raise ValueError
    if not oldAccount:
        print("You cannot undo anymore because you are at the starting point!")
        raise ValueError
    return True
'''
Print functions
'''


def printHello():
    print("Hello, welcome to the Bank Account application.")
    return 

def printHelp():
    print("Here is the list of all the commands you can use.")
    print("add <value> <type> <description> - adds a transaction to the current <day>")
    print("insert <day> <value> <type> <description> - adds a transaction to the specified <day>")
    print("remove <day> - remove all transactions from the specified <day>")
    print("remove <start day> to <end day> - remove all transactions between <start day> and <end day>")
    print("remove <type> - remove all transactions of a specified <type> from the current month")
    print("replace <day> <type> <description> with <amount> - replace the <amount> of a transaction")
    print("list - display the entire list of transactions")
    print("list <type> - display all the transactions of a specified <type>")
    print("list [ <|=|> ] <amount> - display the transactions that have the specified amount of money")
    print("list balance <day> - display the account's balance on a specified <day>")
    print("sum <type> - display the total amount of a specified <type> of transaction")
    print("max <type> <day> - display the maximum transaction of a specified <type> from a specified <day>")
    print("filter <type> - only keep the transactions of the type <type>")
    print("filter <type> <amount> - only keep the transactions of the type <type>, which have their amount smaller than <amount>")
    #print ("undo - undo the last operation" )
    print("exit - exits the application")
    return 

def printListing(listing):
    print("Day:",getDay(listing)," ","Amount:",getAmount(listing)," ","Type:",getType(listing)," ","Description:",getDescription(listing))
    
def printAccount(account):
    '''
    Prints all the listings, if there are any.
    '''
    if not account:
        print("There are no listings.")
        return
    print("---------------")
    account.sort(key=getDay)
    for listing in account: 
        printListing(listing)
    print("---------------")
    return

def printAccountOfType(account,type):
    '''
    Prints all the listings of type type
    '''
    if account == []:
        print("There are no listings.")
        return
    print("All the listings of type ",type,"are:")
    checkExistence = 0 
    for listing in account:
        if getType(listing) == type:
            printListing(listing)
            checkExistence = 1 
    if not checkExistence: 
        print("There are no such listings!")


def printAccountWithOperator(account,operator,amount):
    '''
    Prints all the listings which have their amount (operator) than the parameter amount
    '''
    if account == []:
        print("There are no listings.")
        return
    print("All the listings with their amount ",operator,amount," are:")
    checkExistence = 0 
    for listing in account:
        if operator == "<":
            if  getAmount(listing)<amount:
                printListing(listing)
                checkExistence= 1 
        elif operator=="=":
            if getAmount(listing) == amount:
                printListing(listing)
                checkExistence = 1 
        else:
            if getAmount(listing)>amount:
                printListing(listing)
                checkExistence = 1 
    if not checkExistence: 
        print("There are no such listings!")

def printBalanceAtGivenDay(account,day):
    '''
    Input: account- the list of all listings ; day - the day up to which we want to compute the balance
    Output: the function won't return anything, printing instead the balance locally
    Remarks:-if the type of transaction is 'in', the balance will increase with the amount of said transaction, and if the type is 'out', it will decrease the same way
            -
    '''
    balance = 0 
    for listing in account: 
        if getDay(listing)>day:
            break
        if  getType(listing)=="in":
            balance+=getAmount(listing)
        else:
            balance-=getAmount(listing)
    print("The balance on day ",day," is:",balance)
          
def invalidCommand():
    print("Invalid command! Please try again. Hint: the command is invalid if you add more than one space between words!")
    return