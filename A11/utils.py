
class FileInput(object):
    
    def __init__(self, fileName):
        self.__file = fileName
        self.points = []
        
    def getInput(self):
        with open(self.__file,"r") as file:
            self.n = int(file.readline())
            for times in range(self.n): 
                points = file.readline().strip().split(' ')
                self.points.append(Point(int(points[0]),int(points[1])))
        

class Point(object):
    pass


