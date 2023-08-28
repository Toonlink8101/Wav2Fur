import scipy.io.wavfile
import numpy as np

"""
    Reads wav file and returns a list of 60hz audio intervals
"""
def Get_Data(file_path: str) -> list[list]:
    sample_rate, data = scipy.io.wavfile.read(file_path)

    data = list(data)

    samples_per_frame = sample_rate // 60
    frames_in_data = (len(data) // samples_per_frame) + 1

    samples2add = samples_per_frame - int(len(data) % samples_per_frame)

    # for i in range(samples2add):
    # data.append(0)
    # data[100] += 1

    # Why does adding zeros at the end just ruin everything?
    # unframes = []
    # for value in data:
    #     unframes.append(value)
    # scipy.io.wavfile.write("unframesTest.wav", sample_rate, np.copy(unframes))
    # exit()

    return np.array_split(data, frames_in_data), sample_rate