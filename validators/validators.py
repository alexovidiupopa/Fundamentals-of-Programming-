from errors.errors import ValidError
import datetime


class StudentValidator(object):
    '''
    the class to validate if a student is correctly inputted
    '''
    def validateStudent(self,student):
        errors = ""
        if student.getID()<0:
            errors+="Invalid id"
        if student.getName() == "":
            errors+="Invalid name"
        if student.getGroup() == "":
            errors += "Invalid group"
        if len(errors)>0:
            raise ValidError(errors)
        
class AssignmentValidator(object):
    '''
    the class to validate if an assignment is correctly inputted
    '''
    def validateInt(self,integer):
        try: 
            newInteger = int(integer)
            return newInteger
        except: 
            return -1 
    
    def validateAssignment(self,assignment):
        errors = ""
        if assignment.getID()<0:
            errors += "Invalid id"
        deadline = assignment.getDeadline().split('/')
        if len(deadline) != 3:
            errors+="Invalid deadline"
        else: 
            if self.validateInt(deadline[0]) < 0 or self.validateInt(deadline[0]) > 31:
                errors += "Invalid day of the month"
            if self.validateInt(deadline[1]) <= 0 or self.validateInt(deadline[1]) > 12:
                errors += "Invalid month of the year"
            currentYear = int(datetime.datetime.now().year)
            if self.validateInt(deadline[2]) <= 0 or self.validateInt(deadline[2]) < currentYear or self.validateInt(deadline[2]) > currentYear + 1 :
                errors += "Invalid year."
        if len(errors)>0:
            raise ValidError(errors)
    
    
        
class GradeValidator(object):
    '''
    the class to validate if a grade is correctly inputted
    '''
    def validateGrade(self,grade):
        errors = ""
        if grade.getStudentID() < 0:
            errors += "Invalid student id"
        if grade.getAssignmentID()<0:
            errors += "Invalid assignment id"
        if grade.getGrade()<=0 and grade.getGrade()!=-1 or grade.getGrade()>10:
            errors += "Invalid grade"
        if len(errors)>0:
            raise ValidError(errors)
        
    def validateLateDeadline(self,assignment):
        deadline = datetime.datetime.strptime(assignment.getDeadline(),"%d/%m/%Y")
        currentDate = datetime.datetime.now()
        if deadline < currentDate: 
            return True
        return False
