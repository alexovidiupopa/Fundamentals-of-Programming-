from errors.errors import RepoError
from model.iterablestructure import IterableStructure
class RepoAssignments(object):
    '''
    Class for the assignments repository
    '''
    def __init__(self):
        '''
        class init for the repository
        '''
        self.__assignments = IterableStructure()
    
    def __len__(self):
        '''
        returns the length (number of assignments) of assignments
        '''
        return len(self.__assignments)
    
    def add(self,element):
        '''
        class function for adding an element into the repository
        in - element - element to be added
        out: - 
        raises: RepoError if the element already exists
        '''
        if element in self.__assignments:
            raise RepoError("Element already exists!")
        self.__assignments.append(element)

    
    def searchByID(self,id):
        '''
        class function to search for an element in assignments
        in - element - element which is being searched 
        out: element if it's found 
        raises: RepoError otherwise, if the element doesn't exist
        '''
        for assignments in self.__assignments:
            if assignments.getID() == id:
                return assignments
        raise RepoError("Element doesn't exist!")
    
    def update(self,element):
        '''
        class function to update an element in assignments
        in: element- element which is being updated
        out: NoneType if that happens
        raises: RepoError otherwise, if it doesn't exist
        '''
        if element not in self.__assignments:
            raise RepoError("Element doesn't exist!")
        for i in range(len(self.__assignments)):
            if self.__assignments[i]==element:
                self.__assignments[i]=element
                return
    
    def remove(self,element):
        '''
        class function to remove an element from assignments
        in : element- element which is being deleted
        out- NoneType if that happens
        raises: RepoError otherwise, if it doesn't exist
        '''
        if element not in self.__assignments:
            raise RepoError("Element doesn't exist!")
        for i in range(len(self.__assignments)):
            if self.__assignments[i] == element:
                del self.__assignments[i]
                return

    
    def getAll(self):
        '''
        class function to get all the assignments
        '''
        returnList = []
        for i in range(0,len(self.__assignments)):
            returnList.append(self.__assignments[i])
        return returnList[:]



