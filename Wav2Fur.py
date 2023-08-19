from NoteClass import Note
from ReadWav import Get_Data
from FilterHanning import Filter_Data
from PromptUser import Get_User_Data
from CalculateNoteData import Get_Row

"""
    Main
"""

file_name, channel_number = Get_User_Data()

frames, samplerate = Get_Data()

frames = Filter_Data(frames)

note_data = []

for i in range(len(frames)):
    note_data.append(Get_Row(frames[i], samplerate, channel_number))

output_data()