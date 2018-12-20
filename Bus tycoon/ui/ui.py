
class Console(object):
    
    def __init__(self, controller):
        self.__controller = controller
        self.__commands = {"1":self.__uiCertainRoute,"2":self.__uiPrintRoutes,"3":self.__uiComputeTravelled}
        
    def __uiCertainRoute(self):
        print("Input the route you wish to see all the buses travelling across:")
        route = int(input())
        busesAcross = self.__controller.getBusOnRoute(route)
        if busesAcross == []:
            print("No such route exists, or no buses travel on the route.")
        for bus in busesAcross: 
            print(bus)
            
    def __uiPrintRoutes(self):
        routes = self.__controller.getBusRoutes()
        for route in routes: 
            print(route)
            
    def __uiComputeTravelled(self):
        print("Input the bus id you want to calculate the travelled distance of:")
        busID = int(input())
        distanceAndBus = self.__controller.computeDistance(busID)
        print("The distance is:" + str(distanceAndBus[0]))
        print("Info about the bus: ")
        print(distanceAndBus[1])
    
    def __PrintMenu(self):
        print("\nCommands you can use:")
        print("1 - to display all buses travelling across a certain route")
        print("2 - to display all bus routes")
        print("3 - to compute how many kilometres a bus has travelled in total")
        print("\n")
           
    def run(self):
        print("Hello")
        while True: 
            self.__PrintMenu()
            print(">>")
            command = input()
            if command == "exit":
                print("Goodbye")
                return 
            elif command in self.__commands: 
                try: 
                    self.__commands[command]()
                except ValueError:
                    print("Invalid numerical value")
            else: 
                print("Invalid command")
