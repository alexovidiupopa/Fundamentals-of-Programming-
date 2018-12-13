import unittest

class IterableStructure:
    '''
    Class for the iterable structure required for A9
    '''
    def __init__(self):
        self.__index = 0
        self.__list = []
        
    def __iter__(self):
        '''
        structure iterator
        '''
        return iter(self.__list)
    
    def __next__(self):
        '''
        structure method to get the next element from itself
        '''
        if self.__index > len(self.__list) - 1: 
            raise StopIteration 
        else: 
            self.__index += 1 
        return self.__list[self.__index]
    
    def __len__(self):
        return len(self.__list)
    
    def __getitem__(self,index):
        '''
        gets the item from the list at the positon index
        '''
        return self.__list[index]
    
    def __setitem__(self,index,value):
        '''
        sets the item from the list at the position index to value
        '''
        self.__list[index] = value
        
    def __delitem__(self,index):
        '''
        deletes the item at position index
        '''
        del self.__list[index]
        
    def append(self,element):
        '''
        appends an element into the list
        '''
        self.__list.append(element)  
    
    def getList(self):
        return self.__list[:]
    
def gnomeSort(list,function):
    '''
    The method simply sorts a list using gnome sort, and the sorting will be done using the function transmitted as a parameter to check whether 2 elements are in order
    '''
    index = 0 
    length = len(list)
    if length == 1 or length == 0:
        return
    while index < length: 
        if index == 0:
            index+=1
        if function(list[index],list[index-1])==True: #if the elements are in order.
            index+=1
        else: 
            list[index],list[index-1] = list[index-1],list[index]
            index-=1

def filter(list,criteria):
    '''
    The method simply filters the elements of a list by a given criteria passed as a parameter. This is done by creating a new list and returning it.
    '''
    newList = []
    for index in range(len(list)):
        if criteria(list[index]) == True: 
            newList.append(list[index])
    return newList[:]

class testStructure(unittest.TestCase):
    '''
    Unit tests for the iterable structure
    '''
    def setUp(self):
        self.structure = IterableStructure()
        
    def testIt(self):
        self.structure.append(1)
        self.assertEqual(self.structure[0],1)
        self.structure[0] = 0
        self.assertEqual(self.structure[0],0)
        del self.structure[0]
        self.assertEqual(self.structure.getList(),[])
        self.structure.append(1)
        self.structure.append(1)
        self.structure.append(1)
        self.structure.append(1)
        for index in range(len(self.structure)):
            self.assertEqual(self.structure[index],1)
        
class testSortFilter(unittest.TestCase):
    '''
    Unit tests for the gnome sort and filter methods
    '''
    def setUp(self):
        self.list = [1,2,3,4,5]
        
    def greaterThan(self,number1,number2):
        return number1<number2
    
    def testSort(self):
        gnomeSort(self.list,self.greaterThan)
        self.assertEqual(self.list,[5,4,3,2,1])
        
    def filterCriteria(self,number):
        return number != 4
    
    def testFilter(self):
        list = filter(self.list,self.filterCriteria)
        self.assertEqual(list,[1,2,3,5])
        