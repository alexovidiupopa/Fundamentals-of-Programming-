'''
imports
'''
from ui.console import Console

from validators.validators import StudentValidator, AssignmentValidator, GradeValidator

from controllers.contrAssignments import contrAssignments
from controllers.contrStudents import contrStudents
from controllers.contrGrades import contrGrades
from controllers.undoAction import undoAction

from repository.repoStudents import RepoStudents
from repository.repoAssignments import RepoAssignments
from repository.repoGrades import RepoGrades
from repository.fileRepoStudents import FileRepoStudents
from repository.fileRepoAssignments import FileRepoAssignments
from repository.fileRepoGrades import FileRepoGrades
from repository.pickleRepoStudents import PickleRepoStudents
from repository.pickleRepoAssignments import PickleRepoAssignments
from repository.pickleRepoGrades import PickleRepoGrades

from settings import Settings
from tests.data import Data

'''
initializing all the repos
'''

settings = Settings("settings.properties")
config = settings.configSettings()
inmemory = False
workingApp = True
if config == None:
    workingApp = False
elif config[0] == "inmemory":
    repoStudents = RepoStudents()
    repoAssignments = RepoAssignments() 
    repoGrades = RepoGrades()
    inmemory = True
elif config[0] == "textfiles":
    repoStudents = FileRepoStudents(config[1])
    repoAssignments = FileRepoAssignments(config[2])
    repoGrades = FileRepoGrades(config[3],repoStudents,repoAssignments)
else: 
    repoStudents = PickleRepoStudents(config[1])
    repoAssignments = PickleRepoAssignments(config[2])
    repoGrades = PickleRepoGrades(config[3]) 

if workingApp:
    '''
    initializing all the validators
    '''
    validatorStudent = StudentValidator()
    validatorAssignments = AssignmentValidator()
    validatorGrades = GradeValidator()
    
    '''
    initializing all the controllers
    '''
    controllerStudents = contrStudents(repoStudents,validatorStudent)
    controllerAssignments = contrAssignments(repoAssignments,validatorAssignments)
    controllerGrades = contrGrades(repoGrades,validatorGrades,repoStudents,repoAssignments)
    undoAction = undoAction(controllerStudents,controllerAssignments,controllerGrades)
    '''
    creating the data 
    '''
    if inmemory:
        data = Data(controllerStudents,controllerAssignments,controllerGrades)
        data.createData()
    
    '''
    running the console
    '''
    console = Console(controllerStudents,controllerAssignments,controllerGrades,undoAction)
    console.run()