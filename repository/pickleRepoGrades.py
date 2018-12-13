import pickle
from model.grade import Grade
from errors.errors import PickleRepoError

class PickleRepoGrades:
    '''
    Class to handle the grades repo from .pickle file
    '''
    def __init__(self,fileName):
        self.__fileName = fileName
       
    def __loadGrades(self):
        '''
        Class method to read the grades from the .pickle file
        and return a list of elements of their type.
        '''
        file = open (self.__fileName, "rb")
        try : 
            readList = pickle.load(file)
        except EOFError:
            readList = []
        file.close()
        return readList[:]
    
    def __storeGrades(self,readList):
        '''
        Class method to store the assignments from the parameter <readList> 
        into the .pickle file.
        '''
        file = open(self.__fileName,"wb")
        pickle.dump(readList,file)
        file.close()
    
    def add(self,element):
        '''
        Class method to add a grade to the grades repo.
        Raises PickleRepoError if the grade already exists.
        '''
        grades = self.__loadGrades()
        if element in grades: 
            raise PickleRepoError("Element already exists!")
        grades.append(element)
        self.__storeGrades(grades)
        
    def remove(self,element):
        '''
        Class method to remove a grade from the grades repo
        Raises PickleRepoError if the grades doesnt exist.
        '''
        grades = self.__loadGrades()
        if element not in grades:
            raise PickleRepoError("Element doesnt exist!")
        for i in range(len(grades)):
            if grades[i] == element: 
                del grades[i]
                break 
        self.__storeGrades(grades)
        
    def update(self,element):
        '''
        Class method to update a grade from the grades repo
        Raises PickleRepoError if the grade doesnt exist.
        '''
        grades = self.__loadGrades()
        if element not in grades:
            raise PickleRepoError("Element doesnt exist!")
        for i in range(len(grades)):
            if grades[i] == element: 
                grades[i] = element
                break 
        self.__storeGrades(grades)
        
    def removeStudentID(self,studentID):
        '''
        Class method that removes the grade with student id <studentID>
        '''
        grades = self.__loadGrades()
        for i in range(len(grades)):
            if grades[i].getStudentID() == studentID:
                del grades[i]
                break
        self.__storeGrades(grades)

    def removeAssignmentID(self,assignmentID):
        '''
        Class method that removes the grade with assignment id <assignmentID>
        '''
        grades = self.__loadGrades()
        for i in range(len(grades)):
            if grades[i].getAssignmentID() == assignmentID:
                del grades[i]
                break
        self.__storeGrades(grades) 

    def getAll(self):
        '''
        Class method that returns all the grades from the repo.
        '''
        grades = self.__loadGrades()
        return grades[:]