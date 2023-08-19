from NoteClass import Note
from ReadWav import Get_Data
from FilterHanning import Filter_Data
from PromptUser import Get_User_Data
from CalculateNoteData import Get_Row

"""
    Main
"""

file_name, channel_number = Get_User_Data()

data, samplerate = Get_Data()

data = Filter_Data(data)

note_data = []

for i in range(len(data)):
    note_data.append(Get_Row(data[i], samplerate, channel_number))

output_data()