class Settings():
    '''
    Class to configure the settings from settings.properties
    '''
    def __init__(self,fileName):
        self.__fileName = fileName
        
    def __readFile(self):
        '''
        Reads the settings from a file, splitting the input and creating a list of each pair.
        In case of IOError when opening the file, it will print a message.
        '''
        fileInput = []
        try:
            f = open(self.__fileName)
            line = f.readline()
            while len(line)>0:
                line = line.replace('\n','')
                line = line.split("=")
                fileInput.append(line)
                line = f.readline()
            f.close()
        except IOError:
            print("Settings file error!")
        return fileInput[:]
    
    def configSettings(self):
        '''
        Reads the settings from a file
        out: a tuple of the form (typeOfRepo,repoStudentsLocation,repoAssignmentsLocation,repoGradesLocation)
        '''
        fileInput = self.__readFile()
        if fileInput == []:
            return None
        try:
            return (fileInput[0][1],fileInput[1][1],fileInput[2][1],fileInput[3][1])
        except IndexError: 
            print("Settings file error!")    
    