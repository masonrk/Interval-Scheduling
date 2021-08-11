import random
#initialize variables and arrays
start_array, finish_array, duration_array = [],[],[]

def print_values():
    #prints the min, max, and mean
    print("                       |", "High |   mean   |  Low" )
    print("Earliest Start Time    | ",max(start_array)," | ", sum(start_array)/len(start_array), " | ", min(start_array))
    print("Earliest Finish Time   |", max(finish_array), " | ", sum(finish_array)/len(finish_array), "| ", min(finish_array))
    print("Shortest duration Time |", max(duration_array), " | ", sum(duration_array)/len(duration_array), "| ", min(duration_array))


def scheduleJobs(val):
    tmparray = []
    optimized = []
    tmparray = jobs.copy() #copy list
    tmparray.sort(key=lambda x: x[val])  # this sorts by the position in truple
    while len(tmparray) != 0: #while loop that loops until array is empty
        optimized.insert(len(optimized), tmparray[0]) #insert first position of tmparray in the optimized array
        tmparray.pop(0) #remove first position
        optstart,optduration,optfinish = optimized[len(optimized)-1]
        #this loop iterates through tmparray in reverse removing all values that conflict in time
        for j in reversed(tmparray):
            tmpstart, tmpduration, tmpfinish = j
            if(tmpstart > optstart and tmpstart < optfinish) or (tmpfinish > optstart and tmpfinish < optfinish) or (tmpstart < optstart and tmpfinish > optfinish):
                tmparray.remove(j) #remove the values
    return len(optimized)  # return the amount of jobs scheduled
#Execute algorithms 1000 times
for k in range(1000):
    #initialize vars
    start, duration, finish = 0, 0, 0,
    jobs = []
    #this loop creates a jobs array containing a truple in every position i.
    for i in range(1000):
        duration, start = random.randint(10, 500), random.randint(1,9500) #duration and start are set to corresponding random ints
        finish = start + duration #finish is the sum of start and duration
        truple = (start, duration, finish) #creates the truple
        jobs.insert(i, truple) #insert truple into postion i

    start_array.insert(i,scheduleJobs(0)) #get the number of scheduled jobs and insert into array
    finish_array.insert(i, scheduleJobs(2))#get the number of scheduled jobs and insert into array
    duration_array.insert(i, scheduleJobs(1))#get the number of scheduled jobs and insert into array
print_values()#call the print function

