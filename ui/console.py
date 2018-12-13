from errors.errors import ValidError, RepoError, UndoError, FileRepoError, PickleRepoError
from model.student import Student
from model.assignment import Assignment
from model.grade import Grade

class Console(object):
    
    def __init__(self,controllerStudents,controllerAssignments,controllerGrades,undoAction):
        self.__controllerStudents = controllerStudents
        self.__controllerAssignments = controllerAssignments
        self.__controllerGrades = controllerGrades
        self.__undoAction = undoAction
        self.__choices = {"1":self.__uiAddStudent,"2":self.__uiRemoveStudent,"3":self.__uiUpdateStudent,"4":self.__uiPrintStudents,"5":self.__uiAddAssignment,"6":self.__uiRemoveAssignment,"7":self.__uiUpdateAssignment,"8":self.__uiPrintAssignments,"9":self.__uiAssignToGroup,"10":self.__uiAssignToStudent,"11":self.__uiPrintGrades,"12":self.__uiGradeStudent,"13":self.__uiStatisticsAssignment,"14":self.__uiStatisticsLateStudents,"15":self.__uiStatisticsSchoolSituation,"16":self.__uiStatisticsAssignmentsAtLeastOneGrade,"17":self.__uiUndo,"18":self.__uiRedo}
    
    def __uiAddStudent(self):
        print("Adding a student...\nID:")
        id = int(input())
        print("Name:")
        name = input()
        print("Group:")
        group = input()
        self.__controllerStudents.addStudent(id,name,group)
        self.__undoAction.addToUndoList("1",Student(id,name,group))
        self.__undoAction.addToRedoList("1",Student(id,name,group))
        
    def __uiRemoveStudent(self):
        print("Removing a student...\nID:")
        id = int(input())
        undoRedo = self.__controllerGrades.removeStudentAndAssignments(id)
        self.__undoAction.addToUndoList("cascade",undoRedo[0])
        self.__undoAction.addToRedoList("cascadeStudent",undoRedo[1])
    def __uiUpdateStudent(self):
        print("Updating a student...\nID:")
        id = int(input())
        print("Name:")
        name = input()
        print("Group:")
        group = input()
        oldStudent = self.__controllerStudents.getStudentByID(id)
        self.__controllerStudents.updateStudentGroup(id,name,group)
        self.__undoAction.addToUndoList("3",oldStudent)
        self.__undoAction.addToRedoList("3",Student(id,name,group))
    
    def __uiPrintStudents(self):
        students = self.__controllerStudents.getAllStudents()
        if not students:
            print("Nothing to print!")
            return
        students.sort(key = lambda x: x.getID())
        for student in students:
            print(student)
            
    def __uiAddAssignment(self):
        print("Adding an assignment...\nID:")
        id = int(input())
        print("Description:")
        description = input()
        print("Deadline:")
        deadline = input()
        self.__controllerAssignments.addAssignment(id,description,deadline)
        self.__undoAction.addToUndoList("5",Assignment(id,description,deadline))
        self.__undoAction.addToRedoList("5",Assignment(id,description,deadline))
        
    def __uiRemoveAssignment(self):
        print("Remove an assignment...\nID:")
        id = int(input())
        undoRedo = self.__controllerGrades.removeAssignmentAndGrades(id)
        self.__undoAction.addToUndoList("cascade",undoRedo[0])
        self.__undoAction.addToRedoList("cascadeAssignment",undoRedo[1])
        
    def __uiUpdateAssignment(self):
        print("Updating an assignment...\nID:")
        id = int(input())
        print("New description:")
        description = input()
        print("New deadline:")
        deadline = input()
        oldAssignment = self.__controllerAssignments.getAssignmentByID(id)
        self.__controllerAssignments.updateAssignment(id,description,deadline)
        self.__undoAction.addToUndoList("7",oldAssignment)
        self.__undoAction.addToRedoList("7",Assignment(id,description,deadline))
    
    def __uiPrintAssignments(self):
        assignments = self.__controllerAssignments.getAllAssignments()
        if not assignments:
            print("Nothing to print!")
            return
        assignments.sort(key = lambda x: x.getID())
        for assignment in assignments:
            print(assignment)
 
    def __uiPrintGrades(self):
        grades = self.__controllerGrades.getAllGrades()
        if not grades:
            print("Nothing to print!")
            return 
        for grade in grades: 
            print(grade)
    
    def __uiAssignToGroup(self):
        print("Assigning an assignment to a group of students...\nAssignment ID:")
        assignmentID = int(input())
        print("The group:")
        group = input()
        self.__controllerGrades.assignToGroup(assignmentID,group)
        self.__undoAction.addToUndoList("9",group) 
        self.__undoAction.addToRedoList("9",(assignmentID,group))
        
    def __uiAssignToStudent(self):  
        print("Assigning an assignment to a student...\nAssignment ID:")
        assignmentID = int(input())
        print("Student ID:")
        studentID = int(input())
        self.__controllerGrades.assignToStudent(assignmentID,studentID)
        self.__undoAction.addToUndoList("10",(assignmentID,studentID))
        self.__undoAction.addToRedoList("10",(assignmentID,studentID))
        
    def __uiGradeStudent(self):
        print("Grading a student...\nStudent ID:")
        studentID = int(input())
        self.__printUngradedAssignments(studentID)
        print("Now choose an assignment you wish to grade:")
        assignmentID = int(input())
        print("And the grade you want to give:")
        grade = float(input())
        self.__controllerGrades.gradeStudent(assignmentID,studentID,grade)
        self.__undoAction.addToUndoList("12",(assignmentID,studentID))
        self.__undoAction.addToRedoList("12",(assignmentID,studentID,grade))
    
    def __printStatistic(self,statistics):
        if not statistics: 
            print("No entries of the required statistic type!")
            return 
        for statistic in statistics: 
            print(statistic)
    def __uiStatisticsAssignment(self):
        print("Creating a statistic for an assignment...\nAssignment ID:")
        id = int(input())
        statistics = self.__controllerGrades.createListOfGivenAssignment(id)
        self.__printStatistic(statistics)
            
    def __uiStatisticsLateStudents(self):
        print("Created a statistic containing all late students")
        statistics = self.__controllerGrades.createListOfLateStudents()
        self.__printStatistic(statistics)
    
    def __uiStatisticsSchoolSituation(self):
        print("Created a statistic containing the best school situations, ordered by grade")
        statistics = self.__controllerGrades.createBestSchoolSituation()
        self.__printStatistic(statistics)
    
    def __uiStatisticsAssignmentsAtLeastOneGrade(self):
        print("Created a statistic containing all assignments for which there is at least one grade")
        statistics = self.__controllerGrades.createAssignmentsAtLeastOneGrade()
        self.__printStatistic(statistics)
        
    def __printUngradedAssignments(self,studentID):
        gradesExist = False
        grades = self.__controllerGrades.getAllGrades()
        for grade in grades: 
            if grade.getStudentID() == studentID and grade.getGrade() == -1:
                print(grade)
                gradesExist = True
        if gradesExist == False:
            print("No assignments available for this student.")
            raise RepoError
    
    def __uiUndo(self):
        self.__undoAction.undoController()
        
    def __uiRedo(self):
        self.__undoAction.redoController()
        
    def __printMenu(self):
        print("These are your options: ")
        print("Students commands:")
        print("1: Add a student to the list.")
        print("2: Remove a student from the list.")
        print("3: Update a student.")
        print("4: List all the students.")
        print("-"*40)
        print("Assignments commands:")
        print("5: Add an assignment to the list.")
        print("6: Remove an assignment from the list.")
        print("7: Update an assignment.")
        print("8: List all the assignments.")
        print("-"*40)
        print("Assigning/grading commands:")
        print("9: To assign a certain assignment to a group of students.")
        print("10: To assign a certain assignment to a student.")
        print("11: To list all grades.")
        print("12: To grade a student.")
        print("-"*40)
        print("Statistics commands:")
        print("13: To show all students who received a certain assignment,ordered alphabetically or by average.")
        print("14: To print all students which are late handing in at least one assignment.")
        print("15: To create a statistic containing the best school situations")
        print("16: To create a statistic containing all assignments which have at least one grade.")
        print("-"*40)
        print("Undo/redo:")
        print("17: To undo the last action performed.")
        print("18: To redo the last action undone.")
        print("-"*40)
        print("Utilities:")
        print("help: to print the menu again")
        print("exit: to exit the application")

    def run(self):
        
        print("Hello! Welcome to the lab assignments application! ")
        while True:
            print(">>")
            command = input()
            if command == "exit":
                print("Goodbye!")
                return
            elif command == "help":
                self.__printMenu()
            elif command in self.__choices:
                try: 
                    self.__choices[command]()
                except ValueError as ve:
                    print("Wrong numerical value")
                except ValidError as ve:
                    print("Validation error!")
                    print(ve)
                except RepoError as re:
                    print("Repository error!")
                    print(re)
                except FileRepoError as fre:
                    print("File repo error!")
                    print(fre)
                except PickleRepoError as pre:
                    print("Pickle repo error!")
                    print(pre)
                except UndoError as ue: 
                    print("Undo error!")
                    print(ue)
            else: 
                print("Invalid command!")