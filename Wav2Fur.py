from NoteClass import Note
from ReadWav import Get_Data

"""
    Main
"""

data = []

data = Get_Data()

data = Filter_Data(data)

for segment in data:
    pass

convert_data()

output_data()