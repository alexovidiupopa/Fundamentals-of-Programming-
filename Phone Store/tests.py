from model import *
from business import *
from validators import *

def testModel():
    '''
    Testing the model and validation
    '''
    phone = createPhone("Samsung", "G104", 1234)
    assert getModel(phone) == "G104"
    assert getPrice(phone) == 1234
    assert getManufacturer(phone) == "Samsung" 
    assert validateAdd("abcd", "fghj", 167) == True
    assert validateAdd("abcd", "12", 1234 ) == False
    assert validateAdd("abcd", "hj", 167) == False
    assert validateAdd("a","sadad",1231) == False 
    print("Model and validation tests passed!")
    
def testAdd(phones):
    '''
    Testing functionality 1
    '''
    addPhone(phones, createPhone("apple", "A123", 1234))
    assert getModel(phones[0]) == "A123"
    addPhone(phones, createPhone("nokia", "N978", 124))
    assert getPrice(phones[1]) == 124
    print("Add tests passed!")
    '''
    Hardcoding some phones:
    '''
    addPhone(phones, createPhone("motorola", "H123", 823))
    addPhone(phones, createPhone("google", "oneplus", 1000))
    addPhone(phones, createPhone("samsung", "B33",987))
    addPhone(phones,createPhone("android","xyz",657))
    
def testRemove(phones):
    '''
    Testing functionality 2
    '''
    removePhone(phones, "nokia", "N978")
    assert getManufacturer(phones[1]) == "motorola"
    print("Remove tests passed!")

def runTests(phones):
    '''
    All the tests in one place
    '''
    testModel()
    testAdd(phones)
    testRemove(phones)
    


