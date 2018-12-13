def getManufacturer(phone):
    '''
    gets the manufacturer of a phone
    '''
    return phone["manufacturer"]

def getModel(phone):
    '''
    gets the model of a phone
    '''
    return phone["model"]

def getPrice(phone):
    '''
    gets the price of a phone
    '''
    return phone["price"]

def setManufacturer(phone,newManuf):
    '''
    sets the manufacturer of a phone to <newManuf>
    '''
    phone["manufacturer"] = newManuf
    return

def setModel(phone,newModel):
    '''
    sets the model of a phone to <newModel>
    '''
    phone["model"] = newModel
    return

def setPrice(phone,newPrice):
    '''
    sets the price of a phone to <newPrice>
    '''
    phone["price"] = newPrice
    return

def createPhone(manufacturer,model,price):
    '''
    creates a new phone with the given parameters, in the form of a dictionary.
    '''
    return {"manufacturer":manufacturer,"model":model,"price":price}