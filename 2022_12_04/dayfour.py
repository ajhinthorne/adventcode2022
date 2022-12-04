###import packages
#%%
import re
import pandas

###range function, this will allow us to create arrays from the input txt
#https://www.geeksforgeeks.org/range-to-a-list-in-python/
[*range(2,4,1)]


# %%
d4_input_file = "C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_04/dayfour_input.txt"

def readfile(filename):
    with open(filename,"r") as file:
        lines = file.read().splitlines()
    return lines


#%%
job_list = readfile(d4_input_file)
job_list[0]



#%%

def find_total_overlapping_jobs(input_file):

    overlapping_jobs_array = []

    for item in input_file: 
        job_array = re.split(",",item)
        e1 = job_array[0]
        e2 = job_array[1]

        e1_array = re.split("-",e1)
        e1_min = int(e1_array[0])
        e1_max = int(e1_array[1])

        e2_array = re.split("-",e2)
        e2_min = int(e2_array[0])
        e2_max = int(e2_array[1])

        if (e1_min <= e2_min) & (e1_max >= e2_max): #e1 contains e2         
            overlapping_jobs_array.append(item)

        elif (e1_min >= e2_min) & (e1_max <= e2_max): #e2 contains e1
            overlapping_jobs_array.append(item)
        
        else:
            continue

        
    return overlapping_jobs_array

##testing my function
# %%
job_list[:5]
test = find_total_overlapping_jobs(job_list[:5])
len(test)

#%%
#run my function on the full_jobs_list
overlapping_jobs = find_total_overlapping_jobs(job_list)
len(overlapping_jobs)

###we are correct! 538 jobs are contained in other jobs

#%%
#################### Part 2 ############################
def find_any_overlapping_jobs(input_file):

    overlapping_jobs_array = []

    for item in input_file: 
        job_array = re.split(",",item)
        e1 = job_array[0]
        e2 = job_array[1]

        e1_array = re.split("-",e1)
        e1_min = int(e1_array[0])
        e1_max = int(e1_array[1])

        e2_array = re.split("-",e2)
        e2_min = int(e2_array[0])
        e2_max = int(e2_array[1])

        if (e1_max < e2_min) | (e1_min > e2_max): #max value of one does not overlap with the min value of the other       
            continue
        else: #otherwise we record the overlapping job
            overlapping_jobs_array.append(item)

        
    return overlapping_jobs_array


#%%
any_overlap_jobs = find_any_overlapping_jobs(job_list)
len(any_overlap_jobs)

###792 <- this is the right answer!


# %%
