from NoteClass import Note

"""
    Calulates frequencies for a tick of note data
"""

def Get_Row(data:list, channel_count:int) -> list[Note]:
    # escape condition
    if channel_count <= 0:
        return []
    
    # find loudest frequency

    # isolate frequency

    # determine volume

    # store results in an object
    r = Note()

    # filter out frequency from data
    filtered_data = data

    # Call self
    return [r] + Get_Row(filtered_data, channel_count-1)