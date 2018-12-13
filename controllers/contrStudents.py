from model.student import Student
from errors.errors import RepoError
class contrStudents(object):
    '''
    Class that controls the students
    '''
    def __init__(self,repoStudents,validatorStudents): 
        '''
        class init for the students controller
        '''
        self.__repoStudents = repoStudents
        self.__validatorStudents = validatorStudents
        
    def addStudent(self,id,name,group):
        '''
        class function for adding a student
        in - id - student id 
             name - student name
             group - student group
        out - 
        raises: repoError in case the element already exists
                validError in case the input is invalid
        '''
        student = Student(id,name,group)
        self.__validatorStudents.validateStudent(student)
        self.__repoStudents.add(student)
        
    def removeStudent(self,id,name,group):
        '''
        class function for removing a student
        in - id - student id 
             name - student name
             group - student group
        out - 
        raises: repoError in case the element doesn't exist
        '''
        student = Student(id,name,group)
        self.__repoStudents.remove(student)
        
    def updateStudentGroup(self,id,name,newGroup):
        '''
        class function for updating a student
        in - id - student id 
             name - student name
             newGroup - student group to be updated
        out - 
        raises: repoError in case the element doesn't exist
                validError in case the input is invalid
        '''       
        newStudent = Student(id,name,newGroup)
        self.__validatorStudents.validateStudent(newStudent)
        self.__repoStudents.update(newStudent)
   
    def getStudentByID(self,id):
        try:
            return self.__repoStudents.searchByID(id)
        except RepoError:
            raise RepoError  
        
    def getAllStudents(self):
        '''
        gets the list of all students
        '''
        return self.__repoStudents.getAll()