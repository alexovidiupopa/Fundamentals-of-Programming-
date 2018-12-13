from model.grade import Grade
from model.assignment import Assignment
from model.student import Student
from dto.studentDTO import studentDTO
from dto.schoolSituationDTO import schoolSituationDTO
from dto.assignmentDTO import assignmentDTO
from errors.errors import RepoError
from model.iterablestructure import gnomeSort,filter
class contrGrades(object):
    '''
    Class that controls the grades
    '''
    def __init__(self,repoGrades,validatorGrades,repoStudents,repoAssignments):
        '''
        class init for the grades controller
        '''
        self.__repoGrades = repoGrades
        self.__validatorGrades = validatorGrades
        self.__repoStudents = repoStudents
        self.__repoAssignments = repoAssignments
        
    '''
    ASSIGNING + GRADING FUNCTIONS
    '''
    def assignToGroup(self,assignmentID,group):
        '''
        in: assignmentID - assignmentID 
            group - the group to which we wish to assign 
        out: - 
        raises: repoError in case the element doesn't exist
                validError in case the input is invalid
        '''
        students = self.__repoStudents.getAll()
        ok = False
        for student in students: 
            if student.getGroup() == group:
                try:
                    assignment = self.__repoAssignments.searchByID(assignmentID)
                    grade = Grade(assignment,student)
                    self.__validatorGrades.validateGrade(grade)
                    self.__repoGrades.add(grade)
                    ok = True
                except RepoError as re: 
                    if ok == False: 
                        raise RepoError(re)
                
    def assignToStudent(self,assignmentID,studentID):
        '''
        in: assignmentID - assignmentID 
            studentID - studentID 
        out: - 
        raises: repoError in case the element doesn't exist
                validError in case the input is invalid
        '''
        students = self.__repoStudents.getAll()
        for student in students:
            if student.getID() == studentID:
                assignment = self.__repoAssignments.searchByID(assignmentID)
                grade = Grade(assignment,student)
                self.__validatorGrades.validateGrade(grade)
                self.__repoGrades.add(grade)
                
    def gradeStudent(self,assignmentID,studentID,GradeValue):
        '''
        class function for giving a grade
        in: assignmentID - assignment id 
            studentID - student id 
            GradeValue - grade to be given
        out: -
        raises: repoError in case the element doesn't exist
                validError in case the input is invalid
        '''
        assignment = self.__repoAssignments.searchByID(assignmentID)
        student = self.__repoStudents.searchByID(studentID)
        gradeToAdd = Grade(assignment,student,GradeValue)
        self.__validatorGrades.validateGrade(gradeToAdd)
        grades = self.__repoGrades.getAll()
        if gradeToAdd not in grades:
            raise RepoError("The student hasn't been assigned this assignment yet.")
        for grade in grades:
            if grade == gradeToAdd and grade.getGrade()==-1:
                self.__repoGrades.update(gradeToAdd)
                return 
        raise RepoError("Assignment for the student has already been graded.")
    
    def removeAssignedToGroup(self,group):
        '''
        A function that removes a certain assignment that has been assigned to a group, to be used in the undo part.
        '''
        grades = self.getAllGrades()
        ok = True
        while ok == True: 
            ok = False 
            for grade in grades: 
                Student = self.__repoStudents.searchByID(grade.getStudentID())
                if Student.getGroup() == group: 
                    try:
                        self.__repoGrades.remove(grade) 
                        ok = True
                        break
                    except RepoError: 
                        return
                    
    def removeAssignToStudent(self,assignmentID,studentID):
        '''
        A function that removes a certain assignment that has been assigned to a student, to be used in the undo part.
        '''
        assignment = self.__repoAssignments.searchByID(assignmentID)
        student = self.__repoStudents.searchByID(studentID)
        self.__repoGrades.remove(Grade(assignment,student))
        
    def unGradeStudent(self,assignmentID,studentID):
        '''
        A function that un-grades a student, to be used in the undo part.
        '''
        assignment = self.__repoAssignments.searchByID(assignmentID)
        student = self.__repoStudents.searchByID(studentID)
        self.__repoGrades.update(Grade(assignment,student,-1))
    '''
    FUNCTIONS FOR THE CASCADE DELETE
    '''
    def filterStudent(self,grade):
        if grade.getStudentID() == self.studentToBeFilteredFor.getID():
            return True
        return False
    
    def filterAssignment(self,grade):
        if grade.getAssignmentID() == self.assignmentToBeFilteredFor.getID():
            return True 
        return False
    
    def filterGradesAfterStudent(self,student):
        '''
        in - student after which to filter the assigned assignments
        out-grades[], a list containing all the grades/assignments given to student <student>
        '''
        self.studentToBeFilteredFor = student 
        grades = self.__repoGrades.getAll()
        grades = filter(grades,self.filterStudent)
        return grades[:]
    
    def filterGradesAfterAssignment(self,assignment):
        '''
        in - assigned after which to filter the assigned assignments
        out-grades[], a list containing all the grades/assignments of type <assignment>
        '''
        self.assignmentToBeFilteredFor = assignment
        grades = self.__repoGrades.getAll()
        grades = filter(grades,self.filterAssignment)
        return grades[:]
    
    def removeStudentAndAssignments(self,studentID):
        '''
        in - studentID - the student who and whose assignments we want to remove
        out - none
        raises: repoError if there's no such student
        '''
        student = self.__repoStudents.searchByID(studentID)
        grades = self.filterGradesAfterStudent(student)
        undoList = []
        redoList = []
        '''
        vericoosList = []
        '''
        for grade in grades: 
            self.__repoGrades.removeStudentID(grade.getStudentID())
            undoList.append(("addGrades",grade))
            #redoList.append(("removeGrades",i))
            '''
            vericoosList.append(("9",notamea))
            '''
        self.__repoStudents.remove(student)
        undoList.append(("2",student))
        redoList.append(("2",student))
        return (undoList,redoList)
        '''
        vericoolist.append(student)
        '''
    def addAGrade(self,grade):
        '''
        adds a grade to the repo
        note: the grade is already valid and non-existent!
        '''
        self.__repoGrades.add(grade)
        
    def removeAssignmentAndGrades(self,assignmentID):
        '''
        in - assignmentID - the assignment which and all its assignments
        out - none
        raises: repoEror if there's no such student
        '''
        assignment = self.__repoAssignments.searchByID(assignmentID)
        grades = self.filterGradesAfterAssignment(assignment)
        undoList = []
        redoList = []
        for grade in grades: 
            self.__repoGrades.removeAssignmentID(grade.getAssignmentID())
            undoList.append(("addGrades",grade))
            #redoList.append(("removeGrades",i))
        self.__repoAssignments.remove(assignment)
        undoList.append(("6",assignment))
        redoList.append(("6",assignment))
        return (undoList,redoList)
        
    '''
    STATISTICS FUNCTIONS
    '''
    def averageGradeForStudent(self,studentID):
        '''
        in- studentID : the student ID 
        out- -1 if there are no grades with the studentID 
             the average grade for the studentd with the <studentID> at all assignments
        '''
        sum = 0.0
        numberOfGrades = 0
        grades = self.__repoGrades.getAll()
        for grade in grades:
            if studentID == grade.getStudentID() and grade.getGrade() != -1:
                sum += grade.getGrade()
                numberOfGrades += 1
        if numberOfGrades:
            return float(sum/numberOfGrades)
        return -1
    
    def averageGradeForAssignment(self,assignmentID):
        '''
        in- studentID : the assignment ID 
        out- -1 if there are no grades with the assignmentID 
             the average grade for the all the assignments of <assignmentID>
        '''
        sum = 0.0
        numberOfGrades = 0
        grades = self.__repoGrades.getAll()
        for grade in grades:
            if assignmentID == grade.getAssignmentID() and grade.getGrade() != -1:
                sum += grade.getGrade()
                numberOfGrades += 1
        if numberOfGrades:
            return float(sum/numberOfGrades)
        return -1
    
    def compareGrades(self,element1,element2):
        if element1.getStudentName()>element2.getStudentName():
            return True
        elif element1.getStudentName() < element2.getStudentName():
            return False 
        else: 
            return element1.getGrade() >= element2.getGrade()
        
    def createListOfGivenAssignment(self,assignmentID):
        '''
        creates and returns a list (using a DTO to store the data) of all the assignments with the id <assignmentID>
        the list is ordered after the student name, or the grade, in case they have the same name
        in : assignmentID - the assignment ID 
        out: result[] - list 
        '''
        
        assignment = self.__repoAssignments.searchByID(assignmentID)
        grades = self.filterGradesAfterAssignment(assignment)
        result = []
        for grade in grades: 
            result.append(studentDTO(grade.getStudent(),grade.getGrade()))
        #result.sort(key = lambda element: (element.getStudentName(),element.getGrade()))
        gnomeSort(result,self.compareGrades)
        return result[:]
       
    def createListOfLateStudents(self):
        '''
        creates and returns a list containing all the late students
        '''
        result = []
        grades = self.getAllGrades()
        for grade in grades: 
            if self.__validatorGrades.validateLateDeadline(grade.getAssignment()) is True and grade.getGrade() == -1 and grade.getStudent() not in result: 
                result.append(grade.getStudent())
        return result[:]
    
    def bestSchoolSituation(self,element1,element2):
        return element1.getAvgGrade() <= element2.getAvgGrade()
            
    def createBestSchoolSituation(self):
        '''
        creates and returns a list containing the students with the best school situation, ordered 
        by their average grade, descending.
        '''
        result = []
        grades = self.getAllGrades()
        for grade in grades: 
            student = grade.getStudent()
            avgGrade = self.averageGradeForStudent(grade.getStudentID())
            if avgGrade!=-1:
                schoolSituationDTO1 = schoolSituationDTO(student,avgGrade)
                if schoolSituationDTO1 not in result: 
                    result.append(schoolSituationDTO1)
        #result.sort(key = lambda element: element.getAvgGrade(),reverse = True)
        gnomeSort(result,self.bestSchoolSituation)
        return result[:]
    
    def createAssignmentsAtLeastOneGrade(self):
        '''
        creates and returns a list containing all the assignments who have at least one grade, ordered 
        by the average grade of the assignment, descending.
        '''
        
        result = []
        grades = self.getAllGrades()
        for grade in grades: 
            if grade.getGrade()!=-1:
                avgGrade = self.averageGradeForAssignment(grade.getAssignmentID())
                assignment = grade.getAssignment()
                if avgGrade != -1:
                    assignmentDTOCreated = assignmentDTO(assignment,avgGrade)
                    if assignmentDTOCreated not in result:
                        result.append(assignmentDTOCreated)
        #result.sort(key = lambda element: element.getAvgGrade(),reverse = True)
        gnomeSort(result,self.bestSchoolSituation)
        return result[:]
    
    def getAllGrades(self):
        return self.__repoGrades.getAll()