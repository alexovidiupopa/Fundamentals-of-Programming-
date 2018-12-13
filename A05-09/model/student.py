
class Student(object):
    '''
    The class of an object of type Student
    '''
    def __init__(self, id,name, group,avgGrade = 0 ):
        '''
        student initalization. A student has an id (unique), a name, and a group, as specified in the requirements.
        '''
        self.__id = id
        self.__name = name 
        self.__group = group
        self.__avgGrade = avgGrade
    
    def __eq__(self, studentToCheck):
        '''
        Returns true/false depending on whether two students are equal (have the same id)
        '''
        return self.__id == studentToCheck.__id
     
    def getID(self):
        '''
        gets the id of a student
        '''
        return self.__id
    
    def getName(self):
        '''
        gets the name of a student
        '''
        return self.__name
    
    def getGroup(self):
        '''
        gets the group of a student
        '''
        return self.__group
    
    def getAvgGrade(self):
        return self.__avgGrade
    
    def setName(self, newName):
        '''
        sets the name of a student to newName
        '''
        self.__name = newName
        return
        
    def setGroup(self,newGroup):
        '''
        sets the group of a student to newGroup
        '''
        self.__group = newGroup
        return 
    
    def __str__(self):
        '''
        returns a string with the student in a certain format.
        '''
        return "Student ID:"+ str(self.__id) + "   " + "Name:" + self.__name + "   Group:" + str(self.__group)