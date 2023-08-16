import numpy as np
import scipy
from scipy.fft import rfft, rfftfreq, irfft
# from matplotlib import pyplot as plt

sample_rate, data = scipy.io.wavfile.read("what do you think it is.wav")

samples_per_frame = sample_rate / 60
frames_in_data = len(data) / samples_per_frame

frames = np.array_split(data, frames_in_data)

# recombine individual frames with its neighbor
# blend these pairs with a hanning window
window = np.hanning(samples_per_frame * 2)

yf = rfft(frames[6])
xf = rfftfreq(len(frames[6]), 1/sample_rate)

chopped = irfft(yf)

unframes = []

for i in frames:
    for j in i:
        unframes.append(j)

# print(unframes)

# typed_unframes = np.empty(len(unframes))

# for i in range(len(unframes)):
#     typed_unframes[i] = unframes[i]
#     print(typed_unframes)

typed_unframes = np.copy(unframes)

print(typed_unframes)

# scipy.io.wavfile.write("unframesTest.wav", sample_rate, typed_unframes)
