# Dispatching Rule Scheduling
#### This program finds a solution to a static scheduling problem with 5 jobs, using four dispatching rules: First Come First Serve, Shortest Processing Time, Earliest Due Date, and a combination of the Shortest Processing Time and Earliest Due Date rules.

## How to run:
- Make sure Python 3 is installed
- Make sure Job.py and Machine.py are in the same folder
- Change directory (cd) to the folder where the files are located
- Run the command: python Machine.py
- Note: No external dependencies required

## Program Output: 
First Come First Serve  
Schedule: A, B, C, D, E  
Average Total Flowtime: 51.6  
Average Total Tardiness: 24.2  

Shortest Processing Time  
Schedule: D, E, A, B, C  
Average Total Flowtime: 28.0  
Average Total Tardiness: 9.4  
 
Earliest Due Date  
Schedule: C, E, D, B, A  
Average Total Flowtime: 47.0  
Average Total Tardiness: 8.6  
 
Custom Rule: Shortest Processing Time and Earliest Due Date  
Schedule: D, C, E, B, A  
Average Total Flowtime: 41.8  
Average Total Tardiness: 9.2  
