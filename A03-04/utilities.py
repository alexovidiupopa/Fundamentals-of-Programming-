import datetime

'''
Getters and setters
'''
def getDay(listing):
    return listing["day"]

def setDay(listing,day):
    listing["day"]=day
    return

def getAmount(listing):
    return listing["amount"]

def setAmount(listing,value):
    listing["amount"]=value
    return

def getType(listing):
    return listing["type"]

def setType(listing,type):
    listing["type"]=type
    return
    
def getDescription(listing):
    return listing["description"]

def setDescription(listing,description):
    listing["description"]=description
    return 
def getCurrentDay():
    return datetime.datetime.today().day-1

def createEntry(day,amount,type,description):
    return {"day":day,"amount":amount,"type":type,"description":description}

'''
Some data validation functions
'''

def tryAmount(value):
    '''
    Checks if the input value for the amount respects the parameters (requirements (greater than or equal to 0, and it must be an integer), returning it if it's in order and returning -1 otherwise.
    '''
    integerValue = -1
    try :
        integerValue = int(value)
    except ValueError:
        return -1
    if integerValue<0:
        return -1
    return integerValue
    
def tryDay(value):
    '''
    Checks if the input value for the day respects the requirements (integer between in [0,30]), returning it if it's in order and returning -1 otherwise.
    '''
    integerValue = -1
    try :
        integerValue = int(value)
    except ValueError:
        return -1
    if integerValue<0 or integerValue>30:
        return -1
    return integerValue

def tryType(value):
    '''
    Checks if the input value for the type respects the requirements (must be "in" or "out"), returning it if it's in order and returning -1 otherwise.
    '''
    if value!="in" and value!="out":
        return -1
    return value
