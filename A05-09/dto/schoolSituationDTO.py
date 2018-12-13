
class schoolSituationDTO(object):
    '''
    class for the school situation dto
    '''
    def __init__(self,student,avgGrade):
        self.__student = student
        self.__avgGrade = avgGrade
        
    def __str__(self):
        return "Student ID:" + str(self.__student.getID()) + "  Name:" + self.__student.getName() + "  Group:" + str(self.__student.getGroup()) + "  Average grade:" + str(self.__avgGrade)
    
    def getAvgGrade(self):
        return self.__avgGrade
    
    def __eq__(self,other):
        return self.__student.getID() == other.__student.getID()
    