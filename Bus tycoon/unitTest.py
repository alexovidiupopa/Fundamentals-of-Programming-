'''
Created on 20 dec. 2018

@author: Alex
'''
import unittest
from repo.repoRoutes import RoutesRepository
from repo.repoBuses import BusesRepository
from controller.controller import AppController

class Test(unittest.TestCase):


    def setUp(self):
        self.__repoRoutes = RoutesRepository("routes.txt")
        self.__repoBuses = BusesRepository("buses.txt")
        self.__controller = AppController(self.__repoRoutes,self.__repoBuses)
    
    def testGetBusRoutes(self):
        routes = self.__controller.getBusRoutes()
        self.assertNotEqual(routes,[])
        self.assertEqual(routes[0].getRouteCode(),1)
        self.assertEqual(routes[1].getLength(),21)
        
    def testGetBusOnRoute(self):
        busesTravellingOnRoute = self.__controller.getBusOnRoute(5)
        self.assertEqual(busesTravellingOnRoute[0].getTimesUsed(),7)
        self.assertEqual(busesTravellingOnRoute[1].getTimesUsed(),1)
        self.assertEqual(busesTravellingOnRoute[1].getModel(),"tesla")
        self.assertNotEqual(busesTravellingOnRoute[1].getModel(),"teslah")
    def testTotalDistance(self):
        totalDistance = self.__controller.computeDistance(1)
        self.assertEqual(totalDistance[0],30)
        self.assertEqual(totalDistance[1].getModel(),"mercedes")
        totalDistance = self.__controller.computeDistance(4)
        self.assertEqual(totalDistance[0], 105)    
        self.assertEqual(totalDistance[1].getModel(),"renault")
        self.assertNotEqual(totalDistance[0], 104)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()