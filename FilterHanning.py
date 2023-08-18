import numpy as np

def Filter_Data(data:list[list]) -> list[list]:
    # init
    r = []
    window = np.hanning(len())

    # generate filtered data
    for i in range(1, len(data)):
        r.append(np.concatenate(data[i-1], data[i]))

    