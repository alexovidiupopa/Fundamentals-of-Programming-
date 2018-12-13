from repository.repoGrades import RepoGrades
from errors.errors import FileRepoError
from model.grade import Grade
from model.iterablestructure import IterableStructure

class FileRepoGrades:
    '''
    Class that handles the grades repo for text files
    '''
    def __init__(self,fileName,fileRepoStudents,fileRepoAssignments):
        self.__fileName = fileName
        self.__fileRepoStudents = fileRepoStudents
        self.__fileRepoAssignments = fileRepoAssignments
        
    def __len__(self):
        return len(self.__readGrades())
    
    def __readGrades(self):
        '''
        Class method that reads the grades from the text file
        '''
        file = open(self.__fileName,"r")
        content = file.readlines()
        grades = IterableStructure()
        for line in content: 
            line.strip()
            line = line.replace('\n','')
            line = line.split(';')
            student = self.__fileRepoStudents.searchByID(int(line[1]))
            assignment = self.__fileRepoAssignments.searchByID(int(line[0]))
            grades.append(Grade(assignment,student,float(line[2])))
        file.close()
        return grades
    
    def __writeGrades(self,grades):
        '''
        Class method that writes the grades into the text file.
        '''
        file = open(self.__fileName,"w")
        for grade in grades:
            file.write(str(grade.getAssignmentID())+ ";" + str(grade.getStudentID()) + ";" + str(grade.getGrade()) + "\n")
        file.close()
        
    def add(self,element):
        '''
        Class that adds a grade into the grades repo
        Raises FileRepoError if the grade already exists
        '''
        grades = self.__readGrades()
        if element in grades: 
            raise FileRepoError("Element already exists!")
        grades.append(element)
        self.__writeGrades(grades)
            
    def remove(self,element):
        '''
        Class that removes a grade from the grades repo
        Raises FileRepoError if the grade doesnt exist
        '''
        grades = self.__readGrades()
        if element not in grades:
            raise FileRepoError("Element doesnt exist!")
        for i in range(len(grades)):
            if grades[i] == element:
                del grades[i]
                break 
        self.__writeGrades(grades)
        
    def update(self,element):
        '''
        Class that updates a grade from the grades repo
        Raises FileRepoError if the grade doesnt exist
        '''
        grades = self.__readGrades()
        if element not in grades:
            raise FileRepoError("Element doesnt exist!")
        for i in range(len(grades)):
            if grades[i] == element:
                grades[i] = element
                break 
        self.__writeGrades(grades)
    
    def removeStudentID(self,studentID):
        '''
        Class method that removes the grade with student id <studentID>
        '''
        grades = self.__readGrades()
        for i in range(len(grades)):
            if grades[i].getStudentID() == studentID:
                del grades[i]
                break
        self.__writeGrades(grades)

    def removeAssignmentID(self,assignmentID):
        '''
        Class method that removes the grade with assignment id <assignmentID>
        '''
        grades = self.__readGrades()
        for i in range(len(grades)):
            if grades[i].getAssignmentID() == assignmentID:
                del grades[i]
                break
        self.__writeGrades(grades) 

    def getAll(self):
        '''
        Class method that returns all the grades from the repo.
        '''
        grades = self.__readGrades()
        returnList = []
        for i in range(0,len(grades)):
            returnList.append(grades[i])
        return returnList[:]