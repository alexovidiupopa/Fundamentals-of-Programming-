from business import *

def testAccount(account):
    '''
    Tests it the createEntry function does its job, while appending some elements to the initial account.
    '''
    account.append(createEntry(0,100, "in", "pizza"))
    account.append(createEntry(1,235, "out", "test"))
    account.append(createEntry(2, 20 , "out", "medicine"))
    account.append(createEntry(3,5000, "in", "salary"))
    account.append(createEntry(4,90, "out", "food"))
    account.append(createEntry(13,164,"out", "cigars"))
    account.append(createEntry(12,76, "out", "burgers"))
    account.append(createEntry(16,1500,"out","gaming_rig"))

def testAdd(account):
    '''
    Tests if the add_listing does its job while also denying wrong user input.
    '''
    oldAccount = []
    assert(add_listing(account,["add","50","in","barber_shop"],oldAccount))==True
    assert(add_listing(account,["add","75","out","bread"],oldAccount))==True
    assert(add_listing(account,["add","2","out","test"],oldAccount))==True
    assert(add_listing(account,["add","2d","out","test"],oldAccount))==False
    assert(add_listing(account,["add","2","outz","test"],oldAccount))==False
    assert(add_listing(account,["add","2","out"],oldAccount))==False
    
def testInsert(account):
    '''
    Tests if the insert_listing function does its job while also denying wrong user input.
    '''
    oldAccount = []
    assert(insert_listing(account,["insert","5","100","in","life"],oldAccount)==True)
    assert(insert_listing(account,["insert","3","1001","out","taxes"],oldAccount)==True)
    assert(insert_listing(account,["insert","4","1301","in","hello"],oldAccount)==True)
    assert(insert_listing(account,["insert","6","758","out","clothes"],oldAccount)==True)
    assert(insert_listing(account,["insert","7","96","out","taxes"],oldAccount)==True)
    assert(insert_listing(account,["insert","8","333","in","films"],oldAccount)==True)
    assert(insert_listing(account, ["insert","40","100","out","pizza"],oldAccount)==False)
    assert(insert_listing(account, ["insert","20","100d","out","pizza"],oldAccount)==False)
    assert(insert_listing(account, ["insert","10","100","outz","pizza"],oldAccount)==False)
    assert(insert_listing(account, ["insert","11","100","out"],oldAccount)==False)

def testRemove(account):
    '''
    Tests if the remove_listing function does its job while also denying wrong user input.
    '''
    oldAccount=[]
    #assert (remove_listing(account,["remove","in"] , oldAccount)==True)
    assert (remove_listing(account,["remove","1"] , oldAccount)==True) 
    assert (remove_listing(account,["remove","2","to","3"] , oldAccount)==True)
    assert (remove_listing(account,["remove","inz"] , oldAccount)==False)
    assert (remove_listing(account,["remove","31"] , oldAccount)==False)
    assert (remove_listing(account,["remove","1","tos","4"] , oldAccount)==False)
    assert (remove_listing(account,["remove","-1","to","4"] , oldAccount)==False)
    assert (remove_listing(account,["remove","1","to","32"] , oldAccount)==False)
    
def testReplace(account):
    '''
    Tests the replace_listing function.
    '''
    oldAccount=[]
    account = replace_listing(account, ["replace","0","in","barber_shop","with","123"], oldAccount)
    assert getAmount(account[3])==123
       
def runTests(account):
    '''
    Runs all the tests in one function
    '''
    testAccount(account)
    testAdd(account)
    testInsert(account)
    testRemove(account)
    testReplace(account)
    print("END OF TESTS")