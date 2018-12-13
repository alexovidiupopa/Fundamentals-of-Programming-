from utilities import *
from userInterface import *

def add_listing(account,command,oldAccount):
    '''
    Input: account- the list of all listings, command- the command from the keyboard,oldAccount- the account who keeps track of all the previous accounts
    Output-none
    The function will add at the current day a new listing, with the specifications from the keyboard
    '''
    try:
        listing = UI_add_listing(command)
        oldAccount.append(list(account))
        account.insert(getCurrentDay()+1,listing)
        return True
    except ValueError:
        invalidCommand()
        return False

def insert_listing(account,command,oldAccount):
    '''
    Input: account- the list of all listings, command- the command from the keyboard,oldAccount- the account who keeps track of all the previous accounts
    Output-none
    The function will insert at the position from the command the listing from the command
    '''
    try:
        listing = UI_insert_listing(command)
        oldAccount.append(list(account))
        account.insert(getDay(listing)+1,listing)
        return True
    except ValueError:
        invalidCommand()
        return False

def remove_listing(account,command,oldAccount):
    '''
    Input: account- the list of all the listings, command- the input command, oldAccount- the account who keeps track of all the previous accounts
    Output: True if a modification was made, false if the command entered was invalid
    Remarks: - oldAccount will always append with the last status of account
    '''
    
    try:
        typeOfTask = UI_remove_listing(account, command)
        copyOfAccount = account[:]
        checkExistence = False
        #oldAccount.append(list(account))
        indexesToBeRemoved = []
        if len(typeOfTask)==1:
            indexesToBeRemoved = remove_listings_of(account, typeOfTask[0])
            for index in range(len(indexesToBeRemoved)-1,-1,-1):
                checkExistence = True
                del account[indexesToBeRemoved[index]]
                
        else: 
            indexesToBeRemoved = remove_listings_from(account, typeOfTask[0], typeOfTask[1])
            for index in range(len(indexesToBeRemoved)-1,-1,-1):
                checkExistence = True
                del account[indexesToBeRemoved[index]]
        if checkExistence == True:
            oldAccount.append(copyOfAccount)  
        return True
    except ValueError:
        invalidCommand()
        return False

def remove_listings_of(account,type):
    '''
    Input: account- the list of all the listings, type-in/out, oldAccount- the account who keeps track of all the previous accounts
    Output: indexesToBeRemoved - a list containing all the indexes from -account- whose elements need to be removed, in this case, the 
    ones of type -type-    
    '''
    
    indexesToBeRemoved = []
    for index in range(0,len(account)):
        if getType(account[index])==type:
            indexesToBeRemoved.append(index)
    return indexesToBeRemoved

def remove_listings_from(account,dayStart,dayEnd):
    '''   
    Input: account- the list of all the listing; dayStart- the day from which we want to start removing, dayEnd-the day after which we stop removing listing
    Output: indexesToBeRemoved - a list containing all the indexes from -account- whose elements need to be removed, in this case, the 
    ones from dayStart to dayEnd
    '''
    indexesToBeRemoved = []
    for index in range(0,len(account)):
        if getDay(account[index])>=dayStart and getDay(account[index])<=dayEnd:
            indexesToBeRemoved.append(index)
    return indexesToBeRemoved

def replace_listing(account,command,oldAccount):
    '''
    Input: account- the list of all the listing; listing- a specific listing of the given structure (day,amount,type,description), 
    Output: result- the new list of listings, where the old amount with the same specifications like "listing" is replaced with the new amount from said "listing"
    Remarks: a new list must be created and returned because lists are not transmitted by reference in python.
    '''
    try:
        listing = UI_replace_listing(account, command)
        copyOfAccount = account[:]
        checkExistence = False
        #oldAccount.append(list(account))
        result = []
        for allListings in account:
            amount = getAmount(allListings)
            if (int(getDay(allListings))==int(getDay(listing))) and (str(getType(allListings))==str(getType(listing))) and getAmount(allListings)!=getAmount(listing) and (str(getDescription(allListings))==str(getDescription(listing))):
                amount = getAmount(listing)
                checkExistence = True
            result.append(createEntry(getDay(allListings), amount, getType(allListings), getDescription(allListings)))
        if checkExistence == True:
            oldAccount.append(list(copyOfAccount))
        return result
    except ValueError:
        invalidCommand()
        return account


def sumOfType(account,command):
    '''
    Input: account- the list of all the listings, command- the input command
    Output: no output
    The function will compute and print out the sum of the amounts of the listings of the type specified in the command, or print 
    invalid command if the command was invalid
    '''
    try: 
        type = UI_sum(account,command)
        sum = 0 
        for listing in account: 
            if getType(listing) == type: 
                sum += getAmount(listing)
        print(sum)
    except ValueError: 
        invalidCommand()
        return 
    
def max_type_day(account,command):
    '''
    Input: account- the list of all the listings, command- the input command
    Output: no output
    The function will compute the maximum amount of the specified type and on the specified day (they are specified in the command,unless the 
    command is invalid), and will print it out. In case there are no transactions of said type on said day, it will print out the message
    accordingly. 
    '''
    try: 
        dayAndType = UI_max(account,command)
        day = dayAndType[1]
        type = dayAndType[0]
        max = -1 
        for listing in account:
            if getDay(listing) == day and getType(listing) == type and getAmount(listing)>max:
                max = getAmount(listing)
        if max==-1:
            print("There are no transactions of type ",type," in the day ",day,".")
            return
        print("The maximum ",type," transaction in the day ",day," is",max)
    except ValueError:
        invalidCommand()
        return

def filter_listings_less_than(account,type,amount):
    '''
    Input: account- the list of all listings, type-the specified type, amount- the specified amount
    Output:indexesToBeFiltered- a list which contains the indexes from -account- who are not of type -type- OR are not smaller than 
    the amount -amount-
    '''
    indexesToBeFiltered=[]
    for index in range (0,len(account)):
        if getType(account[index])!=type or getAmount(account[index])>=amount:
            indexesToBeFiltered.append(index)
    return indexesToBeFiltered
        
def filter_listings(account,command,oldAccount):
    '''
    Input: account- the list of all listings, type-the specified type, amount- the specified amount
    Output: True if the command was correct, the account now being modified, and the unchanged account otherwise (if the command was incorrect)
    '''
    try:
        typeAndAmount = UI_filter(account, command)
        copyOfAccount = account[:]
        checkExistence = False
        #oldAccount.append(list(account))
        type=""
        amount = -1
        indexesToBeRemoved = []
        if len(typeAndAmount)==1:
            if command[1]=="in":
                type="out"
            else:
                type="in"
            indexesToBeRemoved = remove_listings_of(account, type)
            for index in range(len(indexesToBeRemoved)-1,-1,-1):
                checkExistence = True
                del account[indexesToBeRemoved[index]]
            if checkExistence == True:
                oldAccount.append(copyOfAccount)
            return True
        type = command[1]
        amount = int(command[2])
        indexesToBeRemoved = filter_listings_less_than(account, type, amount)
        for index in range(len(indexesToBeRemoved)-1,-1,-1):
            checkExistence = True
            del account[indexesToBeRemoved[index]]
        if checkExistence == True:
            oldAccount.append(copyOfAccount)
        return True
    except ValueError:
        invalidCommand()
        return account
        
def mainUndo(account,oldAccount,command):
    '''
    Input:  account- the list of all the listings, command- the input command, 
    oldAccount- the account who keeps track of all the previous accounts
    Output: the original account if the undo command is invalid or the account before the latest modification, which is kept on the 
    last position of -oldAccount- 
    '''
    try:
        verifyUndo = UI_undo(command, oldAccount)
        return oldAccount.pop()
    except ValueError: 
        return account