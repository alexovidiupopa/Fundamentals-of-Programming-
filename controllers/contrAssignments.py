from model.assignment import Assignment
from errors.errors import RepoError
class contrAssignments(object):
    '''
    Class that controls the assignments
    '''
    def __init__(self,repoAssignments,validatorAssignments):
        '''
        class init for the assignments controller
        '''
        self.__repoAssignments = repoAssignments
        self.__validatorAssignments = validatorAssignments
        
    def addAssignment(self,id,description,deadline):
        '''
        class function for adding an assignment
        in: id - assignment id 
            description - assignment description
            deadline - assignment deadline
        out: - 
        raises: repoError in case the element exists
                validError in case the input is invalid
        '''
        assignment = Assignment(id,description,deadline)
        self.__validatorAssignments.validateAssignment(assignment)
        self.__repoAssignments.add(assignment)
    
    def removeAssignment(self,id,description="abc",deadline="10/10/2018"):
    
        '''
        class function for removing an assignment
        in: id - assignment id 
            description - assignment description
            deadline - assignment deadline
        out: - 
        raises: repoError in case the element doesn't exist
                validError in case the input is invalid
        '''
        assignment = Assignment(id,description,deadline)
        self.__validatorAssignments.validateAssignment(assignment)
        self.__repoAssignments.remove(assignment)
    
    def getAssignmentByID(self,id):
        try:  
            return self.__repoAssignments.searchByID(id)
        except RepoError:
            raise RepoError
       
    def updateAssignment(self,id,description,newDeadline):
        '''
        class function for updating an assignment
        in: id - assignment id 
            description - assignment description
            newDeadline - assignment deadline to be updated
        out: - 
        raises: repoError in case the element doesn't
                validError in case the input is invalid
        '''
        newAssignment = Assignment(id,description,newDeadline)
        self.__validatorAssignments.validateAssignment(newAssignment)
        self.__repoAssignments.update(newAssignment)
        
    def getAllAssignments(self):
        '''
        gets the list of all assignments
        '''
        return self.__repoAssignments.getAll()
    