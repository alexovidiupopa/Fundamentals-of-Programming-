class AppController(object):
    '''
    Class for the app controller
    '''
    def __init__(self, repoRoutes, repoBuses):
        '''
        Class constructor. The class will know about the routes repository as well as about the buses repository.
        '''
        self.__repoRoutes = repoRoutes
        self.__repoBuses = repoBuses
    
    def getBusRoutes(self):
        '''
        Method that gets all the routes from the routes repository.
        In: - 
        Out: a list containing all the routes from the routes repository.
        Raises: - 
        Exceptions: -
        '''
        return self.__repoRoutes.getAll()
    
    def getBusOnRoute(self,route):
        '''
        In- route - integer
        Out- busesOnRoute - a list containing all the buses which travelled on the route with the code <route>
        Raises: - 
        Exceptions: -
        '''
        busesOnRoute = []
        allBuses = self.__repoBuses.getAll()
        for bus in allBuses:
            if bus.getRouteCode() == route:
                busesOnRoute.append(bus)
        return busesOnRoute[:]

    def computeDistance(self,busID):
        '''
        In- busID - integer
        Out: a tuple of form (totalDistance,searchedBus) , where: 
                    totalDistance = integer which represents the total distance travelled by the bus with the id <busID> on all its routes
                    searchedBus = the bus with the given id, whose info we need.
        Raises:-
        Exceptions: - 
        '''
        totalDistance = 0
        searchedBus = None
        searchedBus = self.__repoBuses.getBusWithID(busID)
        route = self.__repoRoutes.getRouteByCode(searchedBus.getRouteCode())
        lengthOfRoute = route.getLength()
        totalDistance += lengthOfRoute * searchedBus.getTimesUsed()
        return (totalDistance,searchedBus)
