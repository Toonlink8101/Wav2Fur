"""
    Code I stole again...
"""

from scipy import signal

def notch_filter(data:list, notch_frequency:float, samplerate:int):
    # Create/view notch filter
    quality_factor = 20.0  # Quality factor
    
    # Design a notch filter using signal.iirnotch
    b_notch, a_notch = signal.iirnotch(notch_frequency, quality_factor, samplerate)

    return signal.filtfilt(b_notch, a_notch, data)