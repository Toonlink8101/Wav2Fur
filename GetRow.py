from NoteClass import Note
from scipy.fft import rfft, rfftfreq, irfft
import numpy as np
from helpers.Bandpass import butter_bandpass_filter
from helpers.Decibels import get_average_decibels
from helpers.freq2note import freq2note
from helpers.Notch import notch_filter
from helpers.RelationGen import note_freqs

"""
    Returns a dictionary with frequencies as keys and decibels as values
"""
def GetFrequencies(data: list, samplerate:int) -> dict:
    r = {}

    for current_frequency in note_freqs():
        # if current_frequency%1000 <= 2:
        #     print(current_frequency//1000, "khz")
        filtered_frequency = butter_bandpass_filter(data, current_frequency-1, current_frequency+1, samplerate)
        decibels = get_average_decibels(filtered_frequency)
        r.update({current_frequency: decibels})

    return r

"""
    Calulates frequencies for a tick of note data
"""
def Get_Row(data:list, samplerate:int, channel_count:int) -> list[Note]:
    row = []

    frequencies = GetFrequencies(data, samplerate)

    sorted_frequencies = sorted(frequencies.items(), key=lambda kv:(kv[1], kv[0]))
    
    # convert frequency and loudness to note objects
    for freq in sorted_frequencies[:channel_count]:
        row.append(freq2note(freq[0], freq[1]))

    return row