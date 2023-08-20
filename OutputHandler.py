from NoteClass import Note

def output_pattern(data:list[list[Note]]):
    output = "org.tildearrow.furnace - Pattern Data (166)\n0\n"
    row_count = 256

    # TODO: Implement clipboard
    # TODO: implement row counter, user prompting
    # TODO: prompt user for clipboard header

    for row in data:
        for note in row:
            output += note.output() + '|'
        output += "\n"

    print(output)

def output_instrument(data:list[list[Note]]):
    pass

def output_note_data(data:list[list[Note]]):
    
    while True:
        match input("""
                    \n1. Output to .fur module (not yet supported)
                    \n2. Output as pattern data
                    \n3. Output as instrument data
                    \nChoose a output format:
                """):
            case '1':
                print("Not yet supported")
                continue
            case '2':
                output_pattern(data)
                break
            case '3':
                output_instrument(data)
                break
            case _:
                print("Invalid option")
                continue