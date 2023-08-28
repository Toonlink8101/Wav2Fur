from NoteClass import Note
from helpers.ReadWav import Get_Data
from helpers.FilterHanning import Filter_Data
from GetRow import Get_Row
from OutputHandler import output_note_data

import scipy.io.wavfile
import numpy

"""
    Main
"""

# get input
file_name = input("Please input the file to be read: ")

channel_number = int(input("Input the number of channels: "))

# fetch data
frames, samplerate = Get_Data(file_name)

# filter data
frames = Filter_Data(frames)

# unframes = []
# for frame in frames:
#     for value in frame:
#         unframes.append(value)
# scipy.io.wavfile.write("unframesTest.wav", samplerate, numpy.copy(unframes))
# exit()

# generate notes from sound data
note_data = []

for i in range(len(frames)):
    print("Frame count: " + str(i))
    note_data.append(Get_Row(frames[i], samplerate, channel_number))

# notify user
print("Finished processing!\a")

# output result
output_note_data(note_data)