from model import getManufacturer,getModel,getPrice,setPrice

def addPhone(phones,phoneToAdd):
    '''
    in - phones - list of all phones
        phoneToAdd - a new phone which we want to add to the list
    out - none
    The function appends the phone <phoneToAdd> to the list <phones>
    '''
    phones.append(phoneToAdd)
    
def removePhone(phones,manufacturer,model):
    '''
    in - phones- list of all phones
        manufacturer - the manufacturer of the phone we want to be removed
        model - the model of the phone we want to be removed
    out - True if it removed said phone
         False if said phone doesnt exist
    '''
    for index in range (0,len(phones)):
        if getManufacturer(phones[index]) == manufacturer and getModel(phones[index]) == model: 
            del phones[index]
            return True
    return False

def increaseAmount(phones,manufacturer,model,amount):
    '''
    in - phones- list of all phones
        manufacturer - the manufacturer of the phone we want to be removed
        model - the model of the phone we want to be removed
        amount - the price amount we want to add to the phone <manufacturer,model>
    out - True if the modification was made
          False otherwise, if no such phone exists
    '''
    for index in range (0,len(phones)):
        if getManufacturer(phones[index]) == manufacturer and getModel(phones[index]) == model:
            oldPrice = getPrice(phones[index])
            setPrice(phones[index],oldPrice+amount)
            return True
    return False