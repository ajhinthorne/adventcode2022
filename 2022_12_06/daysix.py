# %% import packages

import pandas as pd
import re

# %%
d6_signal_file = "C:/Users/Adam Hinthorne/Desktop/Advent2022Local/adventcode2022/2022_12_06/daysix_input.txt"

def readfile(filename):
    with open(filename,"r") as file:
        lines = file.read().splitlines()
    return lines

d6_signal_array = readfile(d6_signal_file)
signal_string = d6_signal_array[0]

# %% writing our find marker function
def find_marker(signal,marker_length):
    marker = 0
    i = 1
    for x in range(marker_length + 1,len(signal) + 1,1):
        signal_substr = signal[i:x] ### pull out our substring marker, marker_length + 1 is the first possible value for the marker, i denotes the start of the string
        unique_value_array = pd.unique(re.split('(?<=\w)(?=\w)',signal_substr))

        if len(unique_value_array) == marker_length:
            marker = x ##x is the first value where the previous marker_length number of characters are unique
            break
        else:
            i += 1

    if marker == 0:
        print('There has been an error, marker returned 0!')
        return marker
    else:
        return marker

# %% testing our function
test_string = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
find_marker(test_string,4)

# %% finding our marker

find_marker(signal_string,4) 
### 1282 <- ithis is correct

#### Part 2
### changed the above function to include a marker_length parameter to now find the start of message signal

# %% testing on an example string from part 2, with new marker length of 14
find_marker(test_string,14)

# %% finding marker length of 14 in our signal
find_marker(signal_string,14)

# 3513 <- this is correct

# %%
