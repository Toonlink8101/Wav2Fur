from NoteClass import Note
from helpers.ReadWav import Get_Data
from helpers.FilterHanning import Filter_Data
from helpers.Input import Get_User_Data
from CalculateNoteData import Get_Row
from helpers.OutputHandler import output_note_data

"""
    Main
"""

file_name, channel_number = Get_User_Data()

frames, samplerate = Get_Data()

frames = Filter_Data(frames)

note_data = []

for i in range(len(frames)):
    note_data.append(Get_Row(frames[i], samplerate, channel_number))

output_note_data()