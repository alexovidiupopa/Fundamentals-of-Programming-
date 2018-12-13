from errors.errors import FileRepoError
from model.student import Student
from model.iterablestructure import IterableStructure

class FileRepoStudents:
    '''
    Class for the repoStudents in normal file form
    '''
    def __init__(self,fileName):
        self.__fileName = fileName
        
    def __len__(self):
        return len(self.__readStudents())
    
    def __readStudents(self):
        '''
        Class method to read the students from a file. 
        This method will form a list of objects of type Student and return it.
        '''
        file = open(self.__fileName,"r")
        content = file.readlines()
        students = IterableStructure()
        for line in content:
            line.strip()
            line = line.replace('\n','')
            line = line.split(';')
            students.append(Student(int(line[0]),line[1],line[2]))
        file.close()
        return students
    
    def __writeStudents(self,students):
        '''
        Class method to write the students list <students> into the file.
        '''
        file = open(self.__fileName,"w")
        for student in students: 
            file.write(str(student.getID()) + ";" + student.getName() + ";" + str(student.getGroup())+"\n")
        file.close()
    def add(self,element):
        '''
        Class method to add a student into the student repo
        Raises FileRepoError in case it already exists
        '''
        students = self.__readStudents()
        if element in students:
            raise FileRepoError("Element already exists!")
        students.append(element)
        self.__writeStudents(students)
    
    def remove(self,element):
        '''
        Class method to remove a student from the student repo
        Raises FileRepoError if the student doesnt exist.
        '''
        students = self.__readStudents()
        if element not in students:
            raise FileRepoError("Element doesn't exist!")
        for i in range(len(students)):
            if students[i] == element:
                del students[i]
                break 
        self.__writeStudents(students)
        
    def update(self,element):
        '''
        Class method to update a student from the student repo
        Raises FileRepoError if the student doesnt exist.
        '''
        students = self.__readStudents()
        if element not in students:
            raise FileRepoError("Element doesn't exist!")
        for i in range(len(students)):
            if students[i] == element:
                students[i] = element
                break 
        self.__writeStudents(students)
    def searchByID(self,id):
        '''
        Class method that searches for a student with the id <id> and returns it
        Raises FileRepoError if it doesnt exist.
        '''
        students = self.__readStudents()
        for student in students:
            if student.getID() == id:
                return student 
        raise FileRepoError("ELement doesnt exist!")   
    
    def getAll(self):
        '''
        Class method to get all the students from the file.
        '''
        students = self.__readStudents()
        returnList = []
        for i in range(0,len(students)):
            returnList.append(students[i])
        return returnList[:]