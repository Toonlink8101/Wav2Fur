import numpy as np

def Filter_Data(data:list[list]) -> list[list]:
    # init
    r = []
    window = np.hanning(len(data[0]) * 2)

    # generate filtered data
    for i in range(1, len(data)):
        window = np.hanning(len(data[i-1]) + len(data[i]))
        r.append(np.multiply(window, list(data[i-1]) + list(data[i])))
        
        # no filter
        # r.append(list(data[i-1]) + list(data[i]))

    # for i in range(len(r)):
    #     for j in range(len(r[i])):
    #         r[i][j] = round(r[i][j])

    return r

    