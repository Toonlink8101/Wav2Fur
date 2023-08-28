import numpy as np

#stolen
def convert_to_decibel(arr):
    ref = 1
    if arr!=0:
        return 20 * np.log10(abs(arr) / ref)
        
    else:
        return -60

# not stolen    
def get_average_decibels(data:list):
    sum = 0

    for sample in data:
        sum += convert_to_decibel(sample)
    
    return sum / len(data)