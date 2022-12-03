
#%% import needed packages
import re
import pandas as pd
import math


#%% read the daythree_input file to get the sack list

def readfile(filename):
    with open(filename,"r") as file:
        lines = file.read().splitlines()
    return lines

sack_list = readfile("C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_03\daythree_input.txt")

###testing string splitting functions
#https://stackoverflow.com/questions/46766530/python-split-a-string-by-the-position-of-a-character
# %%
print(
sack_list[0],
len(sack_list[0])/2,
sack_list[0][:12],
sack_list[0][12:])

###function to find characters in a strin 
re.findall('z',sack_list[0])

## definiting a search function
#%%
def find_matches(list_one,list_two):
    shared_item = ''
    for character in list_one:
        if len(re.findall(character,list_two)) > 0:
            shared_item = character
            break

    return shared_item

def character_score(char):
    score_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    match = re.search(char,score_string)
    score = match.span()[1]

    return score

def find_shared_items(item_list):

    shared_items_array = []

    for items in item_list:
        slice_position = int(len(items)/2)
        c1 = items[:slice_position]
        c2 = items[slice_position:]

        shared_items_array += find_matches(c1,c2)

    return shared_items_array

### calculating the final answer!
# %%

shared_items = find_shared_items(sack_list)

priority_sum = 0

for item in shared_items:
    priority_sum += character_score(item)

priority_sum

### 7597 is correct!




##### Part 2 ##########

# %%

i = 0
shared_badge_array = []

for item in sack_list:
    
    if (i % 3) != 0: #skip any elf that's not the first of their group
        i += 1
        continue
    
    else:
        elf_group = []
        elf_group = sorted(sack_list[i:i+3],key=len) # so we loop through the shortest item list for speed
        i += 1

        for character in elf_group[0]:
            if (len(re.findall(character,elf_group[1])) > 0) & (len(re.findall(character,elf_group[2])) > 0):
                print(character)
                shared_item = character
                
        shared_badge_array.append(shared_item)
                
shared_badge_array     


#%%
badge_priority_sum = 0

for item in shared_badge_array:
    badge_priority_sum += character_score(item)

badge_priority_sum

###2607 is the right answer!

# %%
