import math
from NoteClass import Note

def freq2note(frequency, loudness) -> Note:
    # reference frequency
    f0 = 440

    # number of semitones
    n = 12 * math.log(frequency/f0, 2)

    # calculate note value
    semitones_from_f0 = int(n)

    f0_value = 57 # value for A4
    
    note_value = f0_value + semitones_from_f0
    
    # calculate detune
    semitone_fraction = n % 1
    detune_value = round((0x80 * semitone_fraction) + 0x80)

    # calculate volume
    #TODO: fix this, IDK what's happening, too loud?
    volume_value = 0x7F - int(loudness / -6 * 8)

    return Note(note_value, volume_value, detune_value)

# for loudness in range(0, -121, -1):
    # print((.75*loudness), "db -> fur", 0x7F - int((loudness*.75) / -6 * 8))