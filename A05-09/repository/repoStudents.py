from errors.errors import RepoError
from model.iterablestructure import IterableStructure
class RepoStudents(object):
    '''
    Class for the student repository
    '''
    def __init__(self):
        '''
        class init for the repository
        '''
        self.__students = IterableStructure()
    
    def __len__(self):
        '''
        returns the length (number of students) of students
        '''
        return len(self.__students)
    
    def add(self,element):
        '''
        class function for adding an element into the repository
        in - element - element to be added
        out: - 
        raises: RepoError if the element already exists
        '''
        if element in self.__students:
            raise RepoError("Element already exists!")
        self.__students.append(element)

    
    def searchByID(self,id):
        '''
        class function to search for an element in students
        in - element - element which is being searched 
        out: element if it's found 
        raises: RepoError otherwise, if the element doesn't exist
        '''
        for students in self.__students:
            if students.getID() == id:
                return students 
        raise RepoError("ELement doesnt exist!")
    
    def update(self,element):
        '''
        class function to update an element in students
        in: element- element which is being updated
        out: NoneType if that happens
        raises: RepoError otherwise, if it doesn't exist
        '''
        if element not in self.__students:
            raise RepoError("Element doesn't exist!")
        for i in range(len(self.__students)):
            if self.__students[i]==element:
                self.__students[i]=element
                return
    
    def remove(self,element):
        '''
        class function to remove an element from students
        in : element- element which is being deleted
        out- NoneType if that happens
        raises: RepoError otherwise, if it doesn't exist
        '''
        if element not in self.__students:
            raise RepoError("Element doesn't exist!")
        for i in range(len(self.__students)):
            if self.__students[i] == element:
                del self.__students[i]
                return

    
    def getAll(self):
        '''
        class function to get all the students
        '''
        returnList = []
        for i in range(0,len(self.__students)):
            returnList.append(self.__students[i])
        return returnList[:]



