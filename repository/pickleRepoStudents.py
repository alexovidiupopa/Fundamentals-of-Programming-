import pickle 
from model.student import Student
from errors.errors import PickleRepoError

class PickleRepoStudents:
    '''
    Class for the repoStudents in .pickle format
    '''
    def __init__(self,fileName):
        self.__fileName = fileName
        #self.initializeEntity()
    def __loadStudents(self):
        '''
        class method to load the students from the .pickle file into a list 
        in: - 
        out: readList = list containing the students
        in case of error when opening the file, the list is returned empty.
        '''
        file = open (self.__fileName, "rb")
        try : 
            readList = pickle.load(file)
        except EOFError:
            readList = []
        file.close()
        return readList[:]
    
    def __storeStudents(self,readList):
        '''
        Class method to store students into the .pickle file
        in: readList, the list to be stored. 
        out:-
        '''
        file = open(self.__fileName,"wb")
        pickle.dump(readList,file)
        file.close()
        
    def add(self,element):
        '''
        class function for adding an element into the students repo
        in - element - element to be added
        out: - 
        raises: PickleRepoError if the element already exists
        '''
        students = self.__loadStudents()
        if element in students:
            raise PickleRepoError("Element already exists!")
        students.append(element)
        self.__storeStudents(students)
        
    def remove(self,element):
        '''
        class function to remove an element from students
        in : element- element which is being deleted
        out- 
        raises: PickleRepoError otherwise, if it doesn't exist
        '''
        students = self.__loadStudents()
        if element not in students: 
            raise PickleRepoError("Element doesn't exist!")
        for i in range(len(students)):
            if students[i] == element:
                del students[i]
                break 
        self.__storeStudents(students)
        
    def update(self,element):
        '''
        class function to update an element in students
        in: element- element which is being updated
        out: -
        raises: PickleRepoError otherwise, if it doesn't exist
        '''
        students = self.__loadStudents()
        if element not in students: 
            raise PickleRepoError("Element doesn't exist!")
        for i in range(len(students)):
            if students[i] == element:
                students[i] = element
                break 
        self.__storeStudents(students)
        
    def searchByID(self,id):
        '''
        class function to search for an student in students
        in - id - the student's id which is being searched 
        out: student if it's found 
        raises: PickleRepoError otherwise, if the element doesn't exist
        '''
        students = self.__loadStudents()
        for student in students:
            if student.getID() == id:
                return student 
        raise PickleRepoError("ELement doesnt exist!")
    
    def initializeEntity(self):
        self.__storeStudents([Student(1,"alex","123"),Student(2,"abc","125"),Student(3,"alin",127)])
        
    def getAll(self):
        '''
        Class method to get all the students from the file
        
        '''
        students = self.__loadStudents()
        return students[:]