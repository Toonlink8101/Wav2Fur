from NoteClass import Note
from helpers.ReadWav import Get_Data
from helpers.FilterHanning import Filter_Data
from CalculateNoteData import Get_Row
from OutputHandler import output_note_data

"""
    Main
"""

# get input
file_name = input("Please input the file to be read: ")

channel_number = input("Input the number of channels: ")

# fetch data
frames, samplerate = Get_Data(file_name)

# filter data
frames = Filter_Data(frames)

# generate notes from sound data
note_data = []

for i in range(len(frames)):
    note_data.append(Get_Row(frames[i], samplerate, channel_number))

# output result
output_note_data(note_data)