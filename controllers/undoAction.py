from errors.errors import UndoError
class undoAction(object):
    '''
    Class to take care of the undo/redo functionalities
    '''
    def __init__(self,controllerStudents,controllerAssignments,controllerGrades):
        self.__controllerStudents = controllerStudents 
        self.__controllerAssignments = controllerAssignments
        self.__controllerGrades = controllerGrades
        
        self.__undo = []
        self.__undoSave = []
        
        self.__redo = []
        self.__redoSave = []
    
        self.__undoActions = {"1":self.__undoAddStudent,"2":self.__undoRemoveStudent,"3":self.__undoUpdateStudent,
                       "5":self.__undoAddAssignment,"6":self.__undoRemoveAssignment,"7":self.__undoUpdateAssignment,
                       "9":self.__undoAssignToGroup,"10":self.__undoAssignToStudent,"12":self.__undoGradeStudent,
                       "addGrades":self.__undoDeleteGrade,"cascade":self.__undoCascadeDelete}
        self.__redoActions = {"1":self.__redoAddStudent,"3":self.__redoUpdateStudent,
                       "5":self.__redoAddAssignment,"7":self.__redoUpdateAssignment,
                       "9":self.__redoAssignToGroup,"10":self.__redoAssignToStudent,"12":self.__redoGradeStudent,
                       "cascadeStudent":self.__redoCascadeDeleteStudent,"cascadeAssignment":self.__redoCascadeDeleteAssignment}
    '''
    UNDO FUNCTIONALITIES
    '''
    def addToUndoList(self,action,object):
        '''
        Adds a tuple of the type (action,object) to the undo list
        '''
        self.__undo.append((action,object))
    
    def getUndoAction(self,undoElement):
        return undoElement[0]
    
    def getUndoObject(self,undoElement):
        return undoElement[1]
            
    def undoController(self):
        '''
        The undo controlleroller, in which we only execute the command, append in the undoSave list and also pop from the redoSave list into the redo one, in case it isn't empty.
        '''
        if self.__undo == []: 
            raise UndoError("Cannot undo anymore!")
        if self.__redoSave!=[]: 
            self.__redo.append(self.__redoSave.pop())
        lastUndo = self.__undo.pop()
        action = self.getUndoAction(lastUndo)
        object = self.getUndoObject(lastUndo)
        if action in self.__undoActions:
            self.__undoActions[action](object)
        self.__undoSave.append(lastUndo)
    
    def __undoAddStudent(self,student):
        '''
        Undoes the action of adding a student
        '''
        self.__controllerStudents.removeStudent(student.getID(),None,None)
    
    def __undoRemoveStudent(self,student):
        '''
        Undoes the action of removing a student
        '''
        self.__controllerStudents.addStudent(student.getID(),student.getName(),student.getGroup())
        
    def __undoUpdateStudent(self,student):
        '''
        Undoes the action of updating a student
        '''
        self.__controllerStudents.updateStudentGroup(student.getID(),student.getName(),student.getGroup())
        
    def __undoAddAssignment(self,assignment):
        '''
        Undoes the action of adding an assignment
        '''
        self.__controllerAssignments.removeAssignment(assignment.getID())
        
    def __undoRemoveAssignment(self,assignment):
        '''
        Undoes the action of removing an assignment
        '''
        self.__controllerAssignments.addAssignment(assignment.getID(),assignment.getDescription(),assignment.getDeadline())
        
    def __undoUpdateAssignment(self,assignment):
        '''
        Undoes the action of updating an assignment
        '''
        self.__controllerAssignments.updateAssignment(assignment.getID(),assignment.getDescription(),assignment.getDeadline())
        
    def __undoAssignToGroup(self,group):
        '''
        Undoes the action of assigning an assignment to a group
        '''
        self.__controllerGrades.removeAssignedToGroup(group)
        
    def __undoAssignToStudent(self,IDs):
        '''
        Undoes the action of assigning an assignment to a student
        '''
        self.__controllerGrades.removeAssignToStudent(IDs[0],IDs[1]) 
        
    def __undoGradeStudent(self,IDs):
        '''
        Undoes the action of grading a student at an assignment he's been given
        '''
        self.__controllerGrades.unGradeStudent(IDs[0],IDs[1])
    
    def __undoDeleteGrade(self,grade):
        '''
        Undoes the action of deleting a grade
        '''
        self.__controllerGrades.addAGrade(grade)
             
    def __undoCascadeDelete(self,operations):
        '''
        Undoes the action of a cascade delete
        '''
        while operations!=[]: 
            toUndo = operations.pop()
            action = self.getUndoAction(toUndo)
            object = self.getUndoObject(toUndo)
            self.__undoActions[action](object)

    '''
    REDO FUNCTIONALITIES
    '''
    
    def addToRedoList(self,action,object):
        '''
        Adds at the start of the redo list a tuple of the type (action,object)
        '''
        self.__redo.insert(0,(action,object))
    
    def getRedoAction(self,redoElement):
        return redoElement[0]
    
    def getRedoObject(self,redoElement):
        return redoElement[1]
    
    def redoController(self):
        '''
        The redo controlleroller, in which we execute the redo command, append the redo command into the redoSave list, and pop from the undoSave list into the undo one. 
        '''
        if self.__redo == []: 
            raise UndoError("Cannot redo anymore!")
        if self.__undoSave!=[]: 
            self.__undo.append(self.__undoSave.pop())
        lastRedo = self.__redo.pop(0)
        action = self.getRedoAction(lastRedo)
        object = self.getRedoObject(lastRedo)
        if action in self.__redoActions:
            self.__redoActions[action](object)
        self.__redoSave.append(lastRedo)
        
    def __redoAddStudent(self,student):        
        '''
        Redoes the action of adding a student
        '''
        self.__controllerStudents.addStudent(student.getID(),student.getName(),student.getGroup())
        
    def __redoRemoveStudent(self,student):
        '''
        Redoes the action of deleting a student
        '''
        self.__controllerStudents.removeStudent(student.getID())
    
    def __redoUpdateStudent(self,student):
        '''
        Redoes the action of updating a student
        '''
        self.__controllerStudents.updateStudentGroup(student.getID(),student.getName(),student.getGroup())
        
    def __redoAddAssignment(self,assignment):
        '''
        Redoes the action of adding an assignment
        '''
        self.__controllerAssignments.addAssignment(assignment.getID(),assignment.getDescription(),assignment.getDeadline())
        
    def __redoRemoveAssignment(self,assignment):
        '''
        Redoes the action of removing an assignment
        '''
        self.__controllerAssignments.removeAssignment(assignment.getID())
    
    def __redoUpdateAssignment(self,assignment):
        '''
        Redoes the action of updating an assignment
        '''
        self.__controllerAssignments.updateAssignment(assignment.getID(),assignment.getDescription(),assignment.getDeadline())
        
    def __redoAssignToGroup(self,parameters):
        '''
        Redoes the action of assigning to a group
        '''
        self.__controllerGrades.assignToGroup(parameters[0],parameters[1])
        
    def __redoAssignToStudent(self,parameters):
        '''
        Redoes the action of assigning to a student
        '''
        self.__controllerGrades.assignToStudent(parameters[0],parameters[1])
        
    def __redoGradeStudent(self,parameters):
        '''
        Redoes the action of grading to a group
        '''
        self.__controllerGrades.gradeStudent(parameters[0],parameters[1],parameters[2])
    
    def __redoCascadeDeleteStudent(self,student):
        '''
        Redoes the action of a cascade delete for a student
        '''
        self.__controllerGrades.removeStudentAndAssignments(student[0][1].getID())
        
    
    def __redoCascadeDeleteAssignment(self,assignment):
        '''
        Redoes the action of a cascade delete for an assignment
        '''
        self.__controllerGrades.removeAssignmentAndGrades(assignment[0][1].getID())
         