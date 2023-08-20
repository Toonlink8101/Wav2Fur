from NoteClass import Note
from scipy.fft import rfft, rfftfreq, irfft
import numpy as np
from helpers.Bandpass import butter_bandpass_filter
from helpers.Decibels import get_average_decibels
from helpers.freq2note import freq2note
from helpers.Notch import notch_filter

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
            if loudest_freq[1] < amplitude and frequency > 30 and frequency % 30 != 0:
                loudest_freq = (frequency, amplitude)

    # remove amplitude component
    loudest_freq = loudest_freq[0]

    print(loudest_freq)

    if loudest_freq == 0:
        r = freq2note(60, -1000)
        row = []
        for i in range(channel_count):
            row += [r]
        return row

    # isolate frequency
    isolated_freq_data = butter_bandpass_filter(data, loudest_freq-1, loudest_freq+1, samplerate)

    # determine volume
    decibels = get_average_decibels(isolated_freq_data)

    # convert frequency and loudness to note object
    r = freq2note(loudest_freq, decibels)

    # filter out frequency from data
    filtered_data = notch_filter(data, loudest_freq, samplerate)

    # Call self
    return [r] + Get_Row(filtered_data, samplerate, channel_count-1)