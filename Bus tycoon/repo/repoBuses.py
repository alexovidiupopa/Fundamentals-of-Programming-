from models.bus import Bus

class BusesRepository(object):
    
    def __init__(self,fileName):
        self.__buses = []
        file = open(fileName,"r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            self.__buses.append(Bus(int(line[0]),int(line[1]),line[2],int(line[3])))
        file.close()
        
    def getAll(self):
        return self.__buses[:]

    def getBusWithID(self,busID):
        for bus in self.__buses: 
            if bus.getID() == busID: 
                return bus
