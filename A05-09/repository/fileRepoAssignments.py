from errors.errors import FileRepoError
from model.assignment import Assignment
from model.iterablestructure import IterableStructure
class FileRepoAssignments:
    '''
    Class for the repoAssignments, in text file form
    '''
    def __init__(self,fileName):
        self.__fileName = fileName
        
    def __readAssignments(self):
        '''
        Class method to read the assignments from the text file
        and return a list of elements of their type.
        '''
        file = open(self.__fileName, "r")
        content = file.readlines()
        assignments = IterableStructure()
        for line in content:
            line.strip()
            line = line.replace('\n','')
            line = line.split(';')
            assignments.append(Assignment(int(line[0]),line[1],line[2]))
        file.close()
        return assignments
    
    def __writeAssignments(self,assignments):
        '''
        Class method to store the assignments from the parameter assignments 
        into the text file.
        ''' 
        file = open(self.__fileName,"w")
        for assignment in assignments:
            file.write(str(assignment.getID()) + ";" + assignment.getDescription() + ";" + assignment.getDeadline() + "\n")
        file.close()
        
    def add(self,element):
        '''
        Class method to add an assignment to the assignments repo.
        Raises FileRepoError if the assignment already exists.
        '''
        assignments = self.__readAssignments()
        if element in assignments:
            raise FileRepoError("Element already exists!")
        assignments.append(element)
        self.__writeAssignments(assignments)
        
    def remove(self,element):
        '''
        Class method to remove an assignment from the assignment repo
        Raises FileRepoError if the assignment doesnt exist.
        '''
        assignments = self.__readAssignments()
        if element not in assignments:
            raise FileRepoError("Element doesn't exist!")
        for i in range(len(assignments)):
            if assignments[i] == element:
                del assignments[i]
                break 
        self.__writeAssignments(assignments)
        
    def update(self,element):
        '''
        Class method to update an assignment from the assignment repo
        Raises FileRepoError if the assignment doesnt exist.
        '''
        assignments = self.__readAssignments()
        if element not in assignments:
            raise FileRepoError("Element doesn't exist!")
        for i in range(len(assignments)):
            if assignments[i] == element:
                assignments[i] = element
                break 
        self.__writeAssignments(assignments)
    
    def searchByID(self,id):
        '''
        Class method that searches for an assignment with the id <id> in the repo
        Returns the assignment if it exists, raises FileRepoError otherwise
        '''
        assignments = self.__readAssignments()
        for assignment in assignments:
            if assignment.getID() == id:
                return assignment 
        raise FileRepoError("ELement doesnt exist!")   
    
    def getAll(self):
        '''
        Class method that gets all the assignments
        '''
        assignments = self.__readAssignments()
        returnList = []
        for i in range(0,len(assignments)):
            returnList.append(assignments[i])
        return returnList[:]