from errors.errors import RepoError
from model.iterablestructure import IterableStructure
class RepoGrades(object):
    '''
    Class for the grades repository
    '''
    def __init__(self):
        '''
        class init for the repository
        '''
        self.__grades = IterableStructure()
    
    def __len__(self):
        '''
        returns the length (number of grades) of grades
        '''
        return len(self.__grades)
    
    def add(self,element):
        '''
        class function for adding an element into the repository
        in - element - element to be added
        out: - 
        raises: RepoError if the element already exists
        '''
        if element in self.__grades:
            raise RepoError("Element already exists!")
        self.__grades.append(element)

    
    def search(self,element):
        '''
        class function to search for an element in grades
        in - element - element which is being searched 
        out: element if it's found 
        raises: RepoError otherwise, if the element doesn't exist
        '''
        if element not in self.__grades:
            raise RepoError("Element doesn't exist!")
        for grades in self.__grades:
            if element == grades:
                return element

    
    def update(self,element):
        '''
        class function to update an element in grades
        in: element- element which is being updated
        out: NoneType if that happens
        raises: RepoError otherwise, if it doesn't exist
        '''
        if element not in self.__grades:
            raise RepoError("Element doesn't exist!")
        for i in range(len(self.__grades)):
            if self.__grades[i]==element:
                self.__grades[i]=element
                return
    
    def remove(self,element):
        '''
        class function to remove an element from grades
        in : element- element which is being deleted
        out- NoneType if that happens
        raises: RepoError otherwise, if it doesn't exist
        '''
        if element not in self.__grades:
            raise RepoError("Element doesn't exist!")
        for i in range(len(self.__grades)):
            if self.__grades[i] == element:
                del self.__grades[i]
                return

    def removeStudentID(self,studentID):
        '''
        Class function to remove the element with the student id = studentID from the grades repository
        '''
        for i in range(len(self.__grades)):
            if self.__grades[i].getStudentID() == studentID:
                del self.__grades[i]
                return
            
    def removeAssignmentID(self,assignmentID):
        '''
        Class function to remove the element with the assignment id = assignmentID from the grades repository
        '''
        for i in range(len(self.__grades)): 
            if self.__grades[i].getAssignmentID() == assignmentID: 
                del self.__grades[i]
                return
            
    def getAll(self):
        '''
        class function to get all the grades
        '''
        returnList = []
        for i in range(0,len(self.__grades)):
            returnList.append(self.__grades[i])
        return returnList[:]



