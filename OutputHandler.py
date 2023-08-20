from NoteClass import Note

def output_pattern():
    pass

def output_instrument():
    pass

def output_note_data():
    
    match input("""
                \n1. Output to .fur module (not yet supported)
                \n2. Output as pattern data
                \n3. Output as instrument data
                \nChoose a output format:
            """):
        case '2':
            output_pattern()
        case '3':
            output_instrument()
        case _:
            print("Invalid option")
            output_note_data()