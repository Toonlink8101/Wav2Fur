from NoteClass import Note
from ReadWav import Get_Data
from FilterHanning import Filter_Data

"""
    Main
"""

data = Get_Data()

data = Filter_Data(data)

for segment in data:
    pass

convert2notes()

output_data()