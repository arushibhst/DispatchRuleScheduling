from Job import Job
import heapq

class Machine: 
    def __init__(self, jobs):
        self.__jobs= jobs
        self.__prevJobFT = 0
        self.__schedule = []
        self.__allFlow = []
        self.__allTard = []

    def jobs(self):
        return self.__jobs
    
    def calcAvgFlow(self):
        total = sum(self.__allFlow)
        avg = total / len(self.__allFlow)
        return avg

    def calcAvgTard(self):
        total = sum(self.__allTard)
        avg = total / len(self.__allTard)
        return avg
    
    def printSched(self):
        print("Schedule: ")
        print(", ".join(self.__schedule))

    def processJobs(self):
        while self.__jobs:
            currJob = heapq.heappop(self.__jobs)
            self.__schedule.append(currJob.getName())
            currJob.process()
            # for first job or jobs that arrive later than FT of previous job
            if self.__prevJobFT == 0 or self.__prevJobFT < currJob.getAT():
                currJob.setFT(currJob.getAT() + currJob.getPT())
                flow = currJob.calcFlow()
                self.__allFlow.append(flow)
                tard = currJob.calcTard()
                self.__allTard.append(tard)
                self.__prevJobFT = currJob.getFT()
                continue
            currJob.setFT(self.__prevJobFT + currJob.getPT())
            flow = currJob.calcFlow()
            self.__allFlow.append(flow)
            tard = currJob.calcTard()
            self.__allTard.append(tard)
            self.__prevJobFT = currJob.getFT()
        self.printSched()
        print("Average Total Flowtime: " + str(self.calcAvgFlow()))
        print("Average Total Tardiness: " + str(self.calcAvgTard()))

# with FCFS rule
print(" ")
print("First Come First Serve")
jobs1 = []
heapq.heappush(jobs1, Job("A", 0, 11, 61, "FCFS"))
heapq.heappush(jobs1, Job("B", 1, 29, 45, "FCFS"))
heapq.heappush(jobs1, Job("C", 2, 31, 31, "FCFS"))
heapq.heappush(jobs1, Job("D", 3, 1, 33, "FCFS"))
heapq.heappush(jobs1, Job("E", 4, 2, 32, "FCFS"))
machine1 = Machine(jobs1)
machine1.processJobs()
# with SPT rule
print(" ")
print("Shortest Processing Time")
jobs2 = []
heapq.heappush(jobs2, Job("A", 0, 11, 61, "SPT"))
heapq.heappush(jobs2, Job("B", 1, 29, 45, "SPT"))
heapq.heappush(jobs2, Job("C", 2, 31, 31, "SPT"))
heapq.heappush(jobs2, Job("D", 3, 1, 33, "SPT"))
heapq.heappush(jobs2, Job("E", 4, 2, 32, "SPT"))
machine2 = Machine(jobs2)
machine2.processJobs()
# with EDD rule
print(" ")
print("Earliest Due Date")
jobs3 = []
heapq.heappush(jobs3, Job("A", 0, 11, 61, "EDD"))
heapq.heappush(jobs3, Job("B", 1, 29, 45, "EDD"))
heapq.heappush(jobs3, Job("C", 2, 31, 31, "EDD"))
heapq.heappush(jobs3, Job("D", 3, 1, 33, "EDD"))
heapq.heappush(jobs3, Job("E", 4, 2, 32, "EDD"))
machine3 = Machine(jobs3)
machine3.processJobs()

            