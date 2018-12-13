import pickle
from model.assignment import Assignment
from errors.errors import PickleRepoError

class PickleRepoAssignments:
    '''
    Class for the repoAssignments, in .pickle form
    '''
    def __init__(self,fileName):
        self.__fileName = fileName
        #self.initializeEntity()
        
    def __loadAssignments(self):
        '''
        Class method to read the assignments from the .pickle file
        and return a list of elements of their type.
        '''
        file = open (self.__fileName, "rb")
        try : 
            readList = pickle.load(file)
        except EOFError:
            readList = []
        file.close()
        return readList[:]
    
    def __storeAssignments(self,readList):
        '''
        Class method to store the assignments from the parameter <readList> 
        into the .pickle file.
        '''
        file = open(self.__fileName,"wb")
        pickle.dump(readList,file)
        file.close()
    
    def add(self,element):
        '''
        Class method to add an assignment to the assignments repo.
        Raises PickleRepoError if the assignment already exists.
        '''
        assignments = self.__loadAssignments()
        if element in assignments: 
            raise PickleRepoError("Element already exists!")
        assignments.append(element)
        self.__storeAssignments(assignments)
    
    def remove(self,element):
        '''
        Class method to remove an assignment from the assignment repo
        Raises PickleRepoError if the assignment doesnt exist.
        '''
        assignments = self.__loadAssignments()
        if element not in assignments: 
            raise PickleRepoError("Element doesn't exist!")
        for i in range(len(assignments)):
            if assignments[i] == element:
                del assignments[i]
                break 
        self.__storeAssignments(assignments)
        
    def update(self,element):
        '''
        Class method to update an assignment from the assignment repo
        Raises PickleRepoError if the assignment doesnt exist.
        '''
        assignments = self.__loadAssignments()
        if element not in assignments: 
            raise PickleRepoError("Element doesn't exist!")
        for i in range(len(assignments)):
            if assignments[i] == element:
                assignments[i] = element
                break 
        self.__storeAssignments(assignments)
    
    def searchByID(self,id):
        '''
        Class method that searches for an assignment with the id <id> in the repo
        Returns the assignment if it exists, raises PickleRepoError otherwise
        '''
        assignments = self.__loadAssignments()
        for assignment in assignments:
            if assignment.getID() == id:
                return assignment 
        raise PickleRepoError("ELement doesnt exist!")
        
    def initializeEntity(self):
        self.__storeAssignments([Assignment(1,"lab1","11/11/2018"),Assignment(2,"lab2","18/11/2018")])
            
    def getAll(self):
        '''
        Class method that gets all the assignments
        '''
        assignments = self.__loadAssignments()
        return assignments[:]