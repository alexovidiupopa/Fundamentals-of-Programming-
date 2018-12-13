class assignmentDTO():
    '''
    class for the assignment dto
    '''
    def __init__(self,assignment,grade):
        self.__assignment = assignment
        self.__grade = grade
        
    def getAvgGrade(self):
        return self.__grade
    
    def __str__(self):
        return "Assignment ID:" + str(self.__assignment.getID()) + "  Description:" + self.__assignment.getDescription() + "  Deadline:" + str(self.__assignment.getDeadline()) + "  Average grade:" + str(self.__grade)
    
    def __eq__(self,other):
        return self.__assignment.getID() == other.__assignment.getID()