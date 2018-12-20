from models.route import Route

class RoutesRepository(object):
    
    def __init__(self,fileName):
        self.__routes = []
        file = open(fileName,"r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            self.__routes.append(Route(int(line[0]),int(line[1])))
        file.close()
        
    def getAll(self):
        return self.__routes[:]
    
    def getRouteByCode(self,code):
        routes = self.getAll()
        for route in routes: 
            if route.getRouteCode() == code:
                return route 
