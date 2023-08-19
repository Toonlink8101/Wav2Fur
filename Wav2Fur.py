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

for segment in data:
    Get_Row(segment, samplerate, channel_number)

convert2notes()

output_data()