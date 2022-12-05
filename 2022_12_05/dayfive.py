# %% import packages
import pandas as pd
import numpy as np
import re

#%%
### parse_movement_instructions from file

d5_movement_instructions = "C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_05/movement_instructions.txt"

def readfile(filename):
    with open(filename,"r") as file:
        lines = file.read().splitlines()
    return lines

movement_instructions = pd.DataFrame(readfile(d5_movement_instructions),columns=['instructions_text'])

movement_instructions['move_count'] = movement_instructions['instructions_text'].apply(lambda x: int(re.search('(?<=move\s)\d+',x).group(0)))
movement_instructions['start_stack'] = movement_instructions['instructions_text'].apply(lambda x: int(re.search('(?<=from\s)\d+',x).group(0)))
movement_instructions['end_stack'] = movement_instructions['instructions_text'].apply(lambda x: int(re.search('(?<=to\s)\d+',x).group(0)))



#%% creating our start locations dataframe

sl_columns = ['id','name','stack','position']

start_locations_array = [[1,'W',1,1],
[2,'B',1,2],
[3,'G',1,3],
[4,'Z',1,4],
[5,'R',1,5],
[6,'D',1,6],
[7,'C',1,7],
[8,'V',1,8],
[9,'V',2,1],
[10,'T',2,2],
[11,'S',2,3],
[12,'B',2,4],
[13,'C',2,5],
[14,'F',2,6],
[15,'W',2,7],
[16,'G',2,8],
[17,'W',3,1],
[18,'N',3,2],
[19,'S',3,3],
[20,'B',3,4],
[21,'C',3,5],
[22,'P',4,1],
[23,'C',4,2],
[24,'V',4,3],
[25,'J',4,4],
[26,'N',4,5],
[27,'M',4,6],
[28,'G',4,7],
[29,'Q',4,8],
[30,'B',5,1],
[31,'H',5,2],
[32,'D',5,3],
[33,'F',5,4],
[34,'L',5,5],
[35,'S',5,6],
[36,'T',5,7],
[37,'N',6,1],
[38,'M',6,2],
[39,'W',6,3],
[40,'T',6,4],
[41,'V',6,5],
[42,'J',6,6],
[43,'G',7,1],
[44,'T',7,2],
[45,'S',7,3],
[46,'C',7,4],
[47,'L',7,5],
[48,'F',7,6],
[49,'P',7,7],
[50,'Z',8,1],
[51,'D',8,2],
[52,'B',8,3],
[53,'W',9,1],
[54,'Z',9,2],
[55,'N',9,3],
[56,'M',9,4]
]

start_locations_df = pd.DataFrame(start_locations_array,columns = sl_columns)


# %% movement function to alter location_df

###move function for cratemover 9000
def move_function(start_loc,n,start,end):
    end_locations = start_loc
    
    ### changing positions in end column
    end_locations['position'] = np.where(end_locations['stack'] == end, end_locations['position'] + n, end_locations['position'])
    
    ### changing positions and stacks in moved blocks
    end_locations['position'] = np.where((end_locations['stack'] == start) & (end_locations['position'] <= n), -1 * (end_locations['position'] - n - 1), end_locations['position'])
    end_locations['stack'] = np.where((end_locations['stack'] == start) & (end_locations['position'] <= n),end,end_locations['stack'])


    ### chaning positions of remaining blocks in old column
    end_locations['position'] = np.where((end_locations['stack'] == start) & (end_locations['position'] > n),end_locations['position'] - n, end_locations['position'])

    return end_locations



# %%

change_df = start_locations_df

for instructions in movement_instructions.iterrows():    
    change_df = move_function(change_df,instructions[1]['move_count'],instructions[1]['start_stack'],instructions[1]['end_stack'])

change_df


# %%
change_df[change_df['position'] == 1].sort_values('stack')

### 'TBVFVDZPN' <- we got the correct answer!



############## Part 2 ##############################
###alter function for cratemover_9001
# %%
def move_function_cratemover_9001(start_loc,n,start,end):
    end_locations = start_loc
    
    ### changing positions in end column
    end_locations['position'] = np.where(end_locations['stack'] == end, end_locations['position'] + n, end_locations['position'])
    
    ### changing positions and stacks in moved blocks
    ###we don't need to update the postion on the cratemover 9001
    #end_locations['position'] = np.where((end_locations['stack'] == start) & (end_locations['position'] <= n), -1 * (end_locations['position'] - n - 1), end_locations['position'])
    end_locations['stack'] = np.where((end_locations['stack'] == start) & (end_locations['position'] <= n),end,end_locations['stack'])


    ### chaning positions of remaining blocks in old column
    end_locations['position'] = np.where((end_locations['stack'] == start) & (end_locations['position'] > n),end_locations['position'] - n, end_locations['position'])

    return end_locations


# %%
#simulation for cratemover 9001
change_df_9001 = start_locations_df

for instructions in movement_instructions.iterrows():    
    change_df_9001 = move_function_cratemover_9001(change_df_9001,instructions[1]['move_count'],instructions[1]['start_stack'],instructions[1]['end_stack'])

change_df_9001[change_df_9001['position'] == 1].sort_values('stack')

### answer: VLCWHTDSZ <- this is the right answer!!! 



# %%
