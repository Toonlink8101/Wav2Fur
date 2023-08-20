import scipy.io.wavfile
import numpy as np

"""
    Reads wav file and returns a list of 60hz audio intervals
"""
def Get_Data(file_path: str) -> list[list]:
    sample_rate, data = scipy.io.wavfile.read(file_path)

    samples_per_frame = sample_rate / 60
    frames_in_data = len(data) // samples_per_frame

    samples2remove = int(len(data) % samples_per_frame)

    data = data[:len(data)-samples2remove]

    return np.array_split(data, frames_in_data), sample_rate