from NoteClass import Note
from ReadWav import Get_Data
from FilterHanning import Filter_Data
from PromptUser import Get_User_Data

"""
    Main
"""

file_name, channel_number = Get_User_Data()

data = Get_Data()

data = Filter_Data(data)

for segment in data:
    Get_Row(data)

convert2notes()

output_data()