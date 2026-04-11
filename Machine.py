from Job import Job
import heapq

class Machine: 
    def __init__(self, jobs):
        self.__jobs= jobs
        self.__prevJobFT = 0

    def jobs(self):
        return self.__jobs
    
    def processJobs(self):
        while self.__jobs:
            currJob = heapq.heappop(self.__jobs)
            print("Processing: " + currJob.getName())
            currJob.process()
            # for first job or jobs that arrive later than FT of previous job
            if self.__prevJobFT == 0 or self.__prevJobFT < currJob.getAT():
                currJob.setFT(currJob.getAT() + currJob.getPT())
                self.__prevJobFT = currJob.getFT()
                print(currJob.getName() + "finish:" + str(currJob.getFT()))
                continue
            currJob.setFT(self.__prevJobFT + currJob.getPT())
            self.__prevJobFT = currJob.getFT()
            print(currJob.getName() + "finish:" + str(currJob.getFT()))

jobs = []
heapq.heappush(jobs, Job("A", 0, 11, 61, "EDD"))
heapq.heappush(jobs, Job("B", 1, 29, 45, "EDD"))
heapq.heappush(jobs, Job("C", 2, 31, 31, "EDD"))
heapq.heappush(jobs, Job("D", 3, 1, 33, "EDD"))
heapq.heappush(jobs, Job("E", 4, 2, 32, "EDD"))
mach = Machine(jobs)
mach.processJobs()
            