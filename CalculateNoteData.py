from NoteClass import Note
from scipy.fft import rfft, rfftfreq, irfft

"""
    Calulates frequencies for a tick of note data
"""

def Get_Row(data:list, samplerate:int, channel_count:int) -> list[Note]:
    # escape condition
    if channel_count <= 0:
        return []
    
    # fourier transform
    yf = rfft(data)
    xf = rfftfreq(len(data), 1/sample_rate)

    # find loudest frequency

    # isolate frequency

    # determine volume

    # store results in an object
    r = Note()

    # filter out frequency from data
    filtered_data = data

    # Call self
    return [r] + Get_Row(filtered_data, channel_count-1)