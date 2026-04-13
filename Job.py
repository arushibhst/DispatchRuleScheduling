import heapq 

class Job:
    def __init__(self, name, AT, PT, DD, rule):
        self.__name = name
        self.__AT = AT
        self.__PT = PT
        self.__DD = DD
        self.__rule = rule
        self.__FT = 0
        self.__flowtime = 0
        self.__tardiness = 0
        self.__isProcessed = False

    def __lt__(self, other):
        if self.__rule == "FCFS":
            return self.__AT < other.getAT()
        elif self.__rule == "SPT":
            return self.__PT < other.getPT()
        # else earliest due date (EDD)
        elif self.__rule == "EDD":
            return self.__DD < other.getDD()
        # custom rule: Shortest Processing Time and Earliest Due Date combined 
        # this compares the sum of the two parameters
        return (self.__PT + self.__DD) < (other.getPT() + other.getDD())
    
    def calcFlow(self):
        self.__flowtime = self.__FT - self.__AT
        if(self.__flowtime < 0): print("error calculating flowtime")
        return self.__flowtime
    
    def calcTard(self):
        self.__tardiness = max(self.__FT-self.__DD, 0)
        return self.__tardiness

    def setFT(self, finish):
        self.__FT = finish

    def getName(self):
        return self.__name
    
    def getAT(self):
        return self.__AT
    
    def getPT(self):
        return self.__PT
    
    def getDD(self):
        return self.__DD
    
    def getFT(self):
        return self.__FT
    
    def isProcessed(self):
        return self.__isProcessed
    
    def process(self):
        if(self.isProcessed() == True):
            print("already processed")
        self.__isProcessed = True
        return self.__isProcessed
