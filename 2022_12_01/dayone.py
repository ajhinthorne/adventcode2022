###dayone problem: https://adventofcode.com/2022/day/1
###Problem: Retrieve 50 stars

# %% import packages
import pandas as pd
import numpy as np
import re




###reading txt files in python: https://www.pythontutorial.net/python-basics/python-read-text-file/
# %%
###read the elf list
with open("C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_01/dayone_input.txt",'r') as f:
    elf_list = f.readlines()

elf_list

np.shape(elf_list)


# %%
###loop through the elf list and assign elf_ids to each caloric value
elf_df = pd.DataFrame(columns = ['elf_id','calorie_count'])
elf_id = 1

for calorie_count in elf_list:
    int_str = re.sub('\\n','',calorie_count)
    
    if len(int_str) == 0:
        elf_id = elf_id + 1

        continue

    else: 
        elf_array = pd.DataFrame([[elf_id,int_str]],columns = ['elf_id','calorie_count'])

    elf_df = elf_df.append(elf_array)

# %%
### changing the calorie count to integers
elf_df['calorie_count'] = elf_df['calorie_count'].apply(lambda x: int(x))

###calculating the max the group is carrying
elf_df.groupby(['elf_id']).sum().max()[0]


### Problem Part 2
# %%
elf_df.groupby(['elf_id']).sum().sort_values('calorie_count',ascending=False)['calorie_count'].head(3).sum()