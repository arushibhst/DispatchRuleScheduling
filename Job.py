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
        self.__isProcessed = False

    def __lt__(self, other):
        if self.__rule == "FCFS":
            return self.__AT < other.getAT()
        elif self.__rule == "SPT":
            return self.__PT < other.getPT()
        # else earliest due date (EDD)
        return self.__DD < other.getDD()

    def setFT(self, finish):
        self.__FT = finish
    
    def setFlow(self, flow):
        self.__flowtime = flow

    def getName(self):
        return self.__name
    
    def getAT(self):
        return self.__AT
    
    def getPT(self):
        return self.__PT
    
    def getDD(self):
        return self.__DD
    
    def getRule(self):
        return self.__rule
    
    def getFT(self):
        return self.__FT
    
    def getFlowtime(self):
        return self.__flowtime
    
    def isProcessed(self):
        return self.__isProcessed
    
    def process(self):
        if(self.isProcessed == True):
            print("already processed")
        self.__isProcessed = True
        return self.__isProcessed
