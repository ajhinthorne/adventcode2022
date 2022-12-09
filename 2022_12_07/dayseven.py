# %% import packages
import re
import pandas as pd
import json

#find the size of directories with size < 100,000

#%% read input file
def readfile(filename):
    with open(filename,"r") as file:
        lines = file.read().splitlines()

    return lines

d7_input_file = "C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_07/dayseven_input.txt"

command_list = readfile(d7_input_file)
# %%

###commands I need to deal with
#cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
#cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
#cd / switches the current directory to the outermost directory, /.
#ls means list. It prints out all of the files and directories immediately contained by the current directory:
#123 abc means that the current directory contains a file named abc with size 123.
#dir xyz means that the current directory contains a directory named xyz.

#%%% helpful functions

def calculate_size(command):
    size = int(re.search('\d+',command).group(0))
    file_name = re.search('[a-z]+',command).group(0)
    return [size,file_name]

calculate_size(command_list[5])

def 



# %%

dir_object = {
    "outer_dir": {"total_size":0, 
                    "files" : [],
                    "subdirectories": [] }}
current_dir = ''
previous_dir = ''

dir_sizes = pd.DataFrame(columns = ['name','size','subdirectories'])

{"name":  ,
    "total_size": 0
    "files": [{"name": ,"size": }],
    "subdirectories": ,
}

for cmd in command_list[0:5]:

    if len(re.findall('(?<=\$\scd\s)\w+',cmd)) > 0: ### if command enters new directory

        if re.findall('(?<=\$\scd\s)\w+',cmd)[0] not in dir_object.keys():
            current_dir = re.search('(?<=\$\scd\s)\w+',cmd).group(0)
            
            new_dir_object = {"total_size": 0, "files" : [{}], "subdirectories": []}

            dir_object[current_dir] = new_dir_object

    elif cmd == '$ cd /':
        previous_dir = current_dir
        current_dir = "outer_dir"
        continue

    elif cmd == '$ ls':
        continue

    elif cmd == '$ cd ..':
        temp_current_dir = current_dir
        current_dir = previous_dir
        previous_dir = temp_current_dir
        continue


    elif len(re.findall('\d+\s.*',cmd)) > 0: #### this indicates a file line


        
        
        file_name = re.findall('(?<=\d\s).*',cmd)[0]
        file_size = int(re.findall('\d+',cmd)[0])

        new_file_object = {"name": file_name, ### adding the file name
        "size": file_size} ### adding the file size

        dir_object[current_dir]["files"].append(new_file_object)

        

    elif len(re.findall('(?<=dir\s)\w+',cmd)) > 0: ### this indicates a directory line            
            if re.findall('(?<=\$\scd\s)\w+',cmd)[0] not in dir_object.keys():            
                new_dir_object = {"total_size": 0, "files" : [{}], "subdirectories": []}

                dir_object[current_dir] = new_dir_object







dir_object






#%%
for cmd in command_list[0:14]:

    if (len(current_dir) > 0) & (dir_list.count(current_dir) == 0):
        dir_list.append(current_dir)

    if '$' in cmd:
        if cmd == '$ ls':
            print('list')
        elif cmd == '$ cd /':
            previous_dir = current_dir
            current_dir = '/'
            print('Moving into outer directory')
        elif cmd == '$ cd ..':
            temp_current_dir = current_dir
            current_dir = previous_dir
            previous_dir = temp_current_dir
            print('Moving out one directory')
        else:
            previous_dir = current_dir
            current_dir = re.search('(?<=\$\scd\s)\w*',cmd).group(0)
            print('Moving into a new directory')

    


print(dir_list,
    "my current directory is: " + current_dir +". My previous_directory was: " + previous_dir)

# %% ### testing out creating a json file

my_dir_list = {
                "top_priority": {"name":'abc',
                "size": 0,
                "subdirectories": ['def','ghi']},
                "second_priority": {"name":'def',
                "size": 0,
                "subdirectories": ['ghi']},
                "third_priority" : {"name":'ghi',
                "size": 12,
                "subdirectories": [] }               
}

#%%

test_json = json.dumps(my_dir_list)

print(test_json)
# %%
json_data = json.loads(test_json)

json_data
# %%

my_second_object = [{
    "top_priority": {"size":0,"subdirectories": ['def','ghi']},
    "second_priority": {"size":0,"subdirectories": ['xyz']}}]

json_data_two = json.loads(my_second_object)

# %%
my_key = "YAY"

my_new_object = {my_key: {"123": "abc", "456": "def"}}
my_new_object
# %%
