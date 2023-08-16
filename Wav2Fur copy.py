import numpy as np
import scipy
from scipy.fft import rfft, rfftfreq, irfft
# from matplotlib import pyplot as plt

sample_rate, data = scipy.io.wavfile.read("what do you think it is.wav")

samples_per_frame = sample_rate / 60
frames_in_data = len(data) / samples_per_frame

frames = np.array_split(data, frames_in_data)


yf = rfft(frames[6])
xf = rfftfreq(len(frames[6]), 1/sample_rate)

# print("length of yf: " + str(len(yf)))
# print("length of xf: " + str(len(xf)))

# plt.plot(xf, np.abs(yf))
# plt.show()

# print(str(np.abs(yf)))
# print(str(sorted(np.abs(yf))))

# for i in xf:
#     for j in yf:
#         print(str(i) + ", " + str(np.abs(j)))

# largest_value = (0, 0)

# for i in xf:
#     for j in np.abs(yf):
#         if largest_value[1] < j and i >= 30:
#             largest_value = (i, j)

# print(largest_value)

# paired_points = []

# for i in xf:
#     for j in np.abs(yf):
#         pair = (i, j)
#         paired_points.append(pair)

# sorted_points = sorted(paired_points, reverse=True)

# last_point = sorted_points[0]

# for i in sorted_points:
#     if(i[1] < last_point[1]):
#         break
#     last_point = i
#     print(last_point)

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
