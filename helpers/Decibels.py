import numpy as np
import sys

ref = sys.float_info.max - 1

#stolen
def convert_to_decibel(arr):
    # ref = 1
    if arr!=0:
        return 20 * np.log10(abs(arr) / ref)
        
    else:
        return -60

# not stolen    
def get_average_decibels(data:list):
    sum = 0

    for sample in data:
        sum += convert_to_decibel(sample)
    
    if sum <= -60:
        return -60

    return sum / len(data)