
class Assignment(object):
    '''
    The class of an object of type Assignment
    '''
    
    def __init__(self, id, description = "no description", deadline = "unspecified"):
        '''
        class initialization for an assignment. it has an id, a description and a deadline, which have some default values in case they are 
        left unspecified
        '''
        self.__id = id
        self.__description = description 
        self.__deadline = deadline
        
    def __eq__(self, assignmentToCheck):
        '''
        checks if two assignments are equal (Same id)
        '''
        return self.__id == assignmentToCheck.__id
        
    def getID(self):
        '''
        gets the id of an assignment
        '''
        return self.__id
    
    def getDescription(self):
        '''
        gets the description of an assignment
        '''
        return self.__description
    
    def getDeadline(self):
        '''
        gets the deadline of an assignment
        '''
        return self.__deadline
    
    def setDescription(self,newDescription):
        '''
        sets the description of an assignment to newDescription
        '''
        self.__description = newDescription
        return 
    
    def setDeadline(self,newDeadline):
        '''
        sets the deadline of an assignment to newDescription
        '''
        self.__deadline = newDeadline
        return
    
    def __str__(self):
        '''
        returns a nice string of the assignment data
        '''
        return "Assignment ID:" + str(self.__id) + "   Description:" + self.__description + "   Deadline:" + self.__deadline
    
    
        