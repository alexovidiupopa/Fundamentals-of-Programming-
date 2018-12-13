import random
from errors.errors import RepoError
class Data(object):
    '''
    A class which populates my entities
    '''
    def __init__(self,contrStudents,contrAssignments,contrGrades):
        self.__contrStudents = contrStudents
        self.__contrAssignments = contrAssignments
        self.__contrGrades = contrGrades
        
    def __AddStudents(self):
        studentNames = ["alex","alin","tudor","victor","radu","razvan","toras","edi","iulia","paul","alina","paula","cristiana","andrei","leo","george","gheorghe"]
        studentFirstNames = ["popa","marian","popescu","radu","muntean","chirciu","stoica","dumitrescu","benchea","martinescu","calburean","ene","ghita","popovici"]
        studentGroups = ["125","123","111","153","100"]
        for index in range (1,101):
            self.__contrStudents.addStudent(index,studentNames[random.randint(0,12)]+ " " +studentFirstNames[random.randint(0,8)],studentGroups[random.randint(0,4)])
        
    def __AddAssignments(self):
        assignmentNames = ["lab","assignment","laboratory","seminar","homework"]
        assignmentDates = ["01/10/2018","08/10/2018","15/10/2018","22/10/2018","29/10/2018","11/11/2018","18/11/2018","30/11/2018","5/12/2018","10/12/2018","20/12/2018","27/12/2018"]
        for index in range(1,101):
            self.__contrAssignments.addAssignment(index,assignmentNames[random.randint(0,3)] + str(random.randint(1,40)),assignmentDates[random.randint(0,10)])
    def __AddGrades(self):
        for index in range(0,100):
            try: 
                self.__contrGrades.assignToStudent(random.randint(1,100),random.randint(1,100))
            except RepoError: 
                continue
    def __GradeStudents(self):
        grades = self.__contrGrades.getAllGrades()
        index = 0
        while index<len(grades):
            self.__contrGrades.gradeStudent(grades[index].getAssignmentID(),grades[index].getStudentID(),round(random.uniform(1,10),2))
            index += random.randint(1,3)
        
    def createData(self):
        self.__AddStudents()
        self.__AddAssignments()
        self.__AddGrades()
        self.__GradeStudents()
