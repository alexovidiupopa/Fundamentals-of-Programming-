'''
Created on 10 ian. 2019

@author: Alex
'''

from iterative import Iterative
from recursive import Recursive
from utils import FileInput
def run():
    fileInput = FileInput("input.txt")
    fileInput.getInput()
    iterative = Iterative()
    recursive = Recursive()
    iterative.solve(fileInput.n,fileInput.points)
    recursive.solve(fileInput.n,fileInput.points)
    pass

run()