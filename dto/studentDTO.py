from model.student import Student
class studentDTO: 
    '''
    class for the student dto
    '''
    def __init__(self,student,grade):
        self.__student = student
        self.__grade = grade
        
    def getStudentName(self):
        return self.__student.getName()
    
    def getGrade(self):
        return self.__grade 
       
    def __str__(self):
        grade = self.getGrade()
        if grade == -1: 
            grade = "not graded yet"
        return "Student ID:" + str(self.__student.getID()) + "  Name:" + self.getStudentName() + "  Group:" + str(self.__student.getGroup()) + "  Grade:" + str(grade)