import unittest

from model.student import Student
from model.assignment import Assignment

from validators.validators import StudentValidator, AssignmentValidator, GradeValidator

from controllers.contrAssignments import contrAssignments
from controllers.contrStudents import contrStudents
from controllers.contrGrades import contrGrades
from controllers.undoAction import undoAction

from repository.repoStudents import RepoStudents
from repository.repoAssignments import RepoAssignments
from repository.repoGrades import RepoGrades

from errors.errors import ValidError, UndoError, RepoError

class TestModels(unittest.TestCase):

    def setUp(self):
        self.__test_student = Student(1,"Alin",123)
        self.__test_assignment = Assignment(2,"lab12","11/11/2034")
        
    def test_model_get_set(self):
        self.assertEqual(self.__test_student.getGroup(),123)
        self.__test_student.setGroup(134)
        self.assertEqual(self.__test_student.getGroup() ,134)
        
        self.assertEqual(self.__test_assignment.getDescription(),"lab12")
        self.__test_assignment.setDescription("asd")
        self.assertEqual(self.__test_assignment.getDescription(),"asd")
        
class TestRepository(unittest.TestCase):
    
    def setUp(self):
        self.__repoStudents = RepoStudents()
        
    
    def testRepoAdd(self):
        student = Student(1,"alex",99)
        self.__repoStudents.add(student)
        students = self.__repoStudents.getAll()
        self.assertEqual(students[0].getID(),1)
        
    def testRepoRemove(self):
        student = Student(1,"asd",123)
        self.__repoStudents.add(student)
        self.__repoStudents.remove(student)
        students = self.__repoStudents.getAll()
        self.assertEqual(students,[])
        
    def testRepoUpdate(self):
        student = Student(1,"asd",123)
        self.__repoStudents.add(student)
        newStudent = Student(1,"abc",123)
        self.__repoStudents.update(newStudent)
        students = self.__repoStudents.getAll()
        self.assertEqual(students[0].getName(),"abc")
        
    def testRepoGet(self):
        self.assertIsInstance(self.__repoStudents.getAll(),list)
        
class TestControllers(unittest.TestCase):
    
    def setUp(self):
        self.__repoStudents = RepoStudents()
        self.__repoAssignments = RepoAssignments()
        self.__repoGrades = RepoGrades()
        self.__validatorStudent = StudentValidator()
        self.__validatorAssignments = AssignmentValidator()
        self.__validatorGrades = GradeValidator()
        self.__controllerStudents = contrStudents(self.__repoStudents,self.__validatorStudent)
        self.__controllerAssignments = contrAssignments(self.__repoAssignments,self.__validatorAssignments)
        self.__controllerGrades = contrGrades(self.__repoGrades,self.__validatorGrades,self.__repoStudents,self.__repoAssignments)
        
    
    def testStudentAdd(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerStudents.addStudent(2,"alin",123)
        self.assertRaises(RepoError,self.__controllerStudents.addStudent,1,"alex",123)
        students = self.__controllerStudents.getAllStudents()
        self.assertEqual(students[0].getName(),"alex")
        self.assertEqual(students[1].getGroup(),123)
        
    def testStudentRemove(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.assertRaises(RepoError,self.__controllerStudents.removeStudent,2,None,None)
        self.__controllerStudents.removeStudent(1,None,None)
        students = self.__controllerStudents.getAllStudents()
        self.assertEqual(students,[])
        
    def testStudentUpdate(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerStudents.updateStudentGroup(1, "alex",1234)
        self.assertRaises(RepoError,self.__controllerStudents.updateStudentGroup,2,None,None)
        students = self.__controllerStudents.getAllStudents()
        self.assertEqual(students[0].getGroup(),1234)
        
    def testAssignmentAdd(self):
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerAssignments.addAssignment(2,"lab3","12/11/2018")
        self.assertRaises(ValidError,self.__controllerAssignments.addAssignment,10,"lab3","11/10/2010")
        self.assertRaises(RepoError,self.__controllerAssignments.addAssignment,1,"lab3","11/10/2018")
        assignments = self.__controllerAssignments.getAllAssignments()
        self.assertEqual(assignments[0].getDescription(),"lab2")
        self.assertEqual(assignments[1].getDeadline(),"12/11/2018")
    
    def testAssignmentRemove(self):
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.assertRaises(RepoError,self.__controllerAssignments.removeAssignment,2)
        self.__controllerAssignments.removeAssignment(1)
        assignments = self.__controllerAssignments.getAllAssignments()
        self.assertEqual(assignments,[])
    
    def testAssignmentUpdate(self):
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerAssignments.updateAssignment(1, "lab1", "12/12/2018")
        self.assertRaises(RepoError,self.__controllerAssignments.updateAssignment,2,"lab3","12/12/2018")
        self.assertRaises(ValidError,self.__controllerAssignments.updateAssignment,1,"lab3","12/12/2010")
        assignments = self.__controllerAssignments.getAllAssignments()
        self.assertEqual(assignments[0].getDeadline(),"12/12/2018")
        
    def testAssignToStudent(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerGrades.assignToStudent(1, 1)
        grades = self.__controllerGrades.getAllGrades()
        self.assertEqual(grades[0].getStudentID(),1)
        self.assertEqual(grades[0].getGrade(),-1)
        
    def testAssignToGroup(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerStudents.addStudent(2,"alin",124)
        self.__controllerStudents.addStudent(3,"edi",123)
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerGrades.assignToGroup(1, 123)
        grades = self.__controllerGrades.getAllGrades()
        self.assertEqual(len(grades),2)
        self.assertEqual(grades[0].getStudentID(), 1)
        self.assertEqual(grades[1].getStudentID(), 3)
    
    def testGrading(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerGrades.assignToStudent(1,1)
        self.__controllerGrades.gradeStudent(1,1,10)
        self.assertRaises(RepoError,self.__controllerGrades.gradeStudent,1,1,3)
    
    def testCascadingDeleteStudent(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerAssignments.addAssignment(2, "lab3", "11/12/2018")
        self.__controllerGrades.assignToStudent(1,1)
        self.__controllerGrades.assignToStudent(2,1)
        self.__controllerGrades.removeStudentAndAssignments(1)
        grades = self.__controllerGrades.getAllGrades()
        self.assertEqual(grades,[])
        student = self.__controllerStudents.getAllStudents()
        self.assertEqual(student,[])
        
    def testCascadingDeleteAssignment(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__controllerStudents.addStudent(2,"radu",125)
        self.__controllerAssignments.addAssignment(1, "lab2", "11/12/2018")
        self.__controllerGrades.assignToStudent(1,1)
        self.__controllerGrades.assignToStudent(1,2)
        self.__controllerGrades.removeAssignmentAndGrades(1)
        grades = self.__controllerGrades.getAllGrades()
        self.assertEqual(grades,[])
        assignments = self.__controllerAssignments.getAllAssignments()
        self.assertEqual(assignments,[])
        
        
class TestUndo(unittest.TestCase):
    
    def setUp(self):
        self.__repoStudents = RepoStudents()
        self.__repoAssignments = RepoAssignments()
        self.__repoGrades = RepoGrades()
        self.__validatorStudent = StudentValidator()
        self.__validatorAssignments = AssignmentValidator()
        self.__validatorGrades = GradeValidator()
        self.__controllerStudents = contrStudents(self.__repoStudents,self.__validatorStudent)
        self.__controllerAssignments = contrAssignments(self.__repoAssignments,self.__validatorAssignments)
        self.__controllerGrades = contrGrades(self.__repoGrades,self.__validatorGrades,self.__repoStudents,self.__repoAssignments)
        self.__undoAction = undoAction(self.__controllerStudents,self.__controllerAssignments,self.__controllerGrades)
        
    def testUndoRedoStudent(self):
        self.__controllerStudents.addStudent(1,"alex",123)
        self.__undoAction.addToUndoList("1",Student(1,"alex",123))
        self.__undoAction.addToRedoList("1",Student(1,"alex",123))
        self.__undoAction.undoController()
        students = self.__controllerStudents.getAllStudents()
        self.assertEqual(students,[])
        self.__undoAction.redoController()
        students = self.__controllerStudents.getAllStudents()
        self.assertEqual(len(students),1)
        self.__controllerStudents.removeStudent(1,"alex",123)
        self.__undoAction.addToUndoList("2",Student(1,"alex",123))
        self.__undoAction.addToRedoList("2",Student(1,"alex",123))
        self.__undoAction.undoController()
        students = self.__controllerStudents.getAllStudents()
        self.assertEqual(len(students),1)
        pass
if __name__ == "__main__":
    unittest.main()