from NoteClass import Note
from scipy.fft import rfft, rfftfreq, irfft
import numpy as np
from helpers.Bandpass import butter_bandpass_filter
from helpers.Decibels import get_average_decibels
from helpers.freq2note import freq2note

"""
    Calulates frequencies for a tick of note data
"""

def Get_Row(data:list, samplerate:int, channel_count:int) -> list[Note]:
    # escape condition
    if channel_count <= 0:
        return []
    
    # fourier transform
    yf = rfft(data)
    xf = rfftfreq(len(data), 1/samplerate)

    # find loudest frequency
    loudest_freq = (0, 0)

    for frequency in xf:
        for amplitude in np.abs(yf):
            if loudest_freq[1] < amplitude and frequency > 30:
                loudest_freq = (frequency, amplitude)

    # remove amplitude component
    loudest_freq = loudest_freq[0]

    # isolate frequency
    isolated_freq_data = butter_bandpass_filter(data, loudest_freq-1, loudest_freq+1, samplerate)

    # determine volume
    loudness = get_average_decibels(isolated_freq_data)

    # convert frequency and loudness to note object
    r = freq2note()

    # filter out frequency from data
    filtered_data = data

    # Call self
    return [r] + Get_Row(filtered_data, samplerate, channel_count-1)