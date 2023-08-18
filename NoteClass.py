from NoteValueConverter import Value2Note

class Note:
    def __init__(self, value:int, volume:int, detune:int):
        self.value = value
        self.volume = volume
        self.detune = detune

    def output_pattern(self) -> str:
        r = str(Value2Note(self.value)) + ".."
        
        if(self.volume < 16):
            r += '0' + hex(self.volume)[-1]
        else:
            r +=  hex(self.volume)[-2:]
        
        r += "E5" + hex(self.detune)

        return r