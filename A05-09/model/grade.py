
class Grade(object):
    '''
    The class of an object of type Grade
    '''
    def __init__(self, assignment, student, grade = -1):
        self.__assignment = assignment 
        self.__student = student 
        self.__grade = grade
        
    
    def __eq__(self,gradeToCheck):
        return self.__assignment.getID() == gradeToCheck.__assignment.getID() and self.__student.getID() == gradeToCheck.__student.getID() 
     
    def __str__(self):
        provisoryGrade = str(self.__grade)
        if self.__grade == -1:
            provisoryGrade = "not graded yet"
        return "Assignment ID:" + str(self.__assignment.getID()) + "   Student ID:" + str(self.__student.getID()) + "   Grade:" + provisoryGrade
    def __lt__(self,gradeToCheck):
        return self.__grade < gradeToCheck.__grade
    def getAssignment(self):
        return self.__assignment
    
    def getStudent(self):
        return self.__student
    
    def getAssignmentID(self):
        return self.__assignment.getID()
    
    def getStudentID(self):
        return self.__student.getID()
    
    def getGrade(self):
        return self.__grade
    
    def setGrade(self,newGrade):
        self.__grade = newGrade
        return
        