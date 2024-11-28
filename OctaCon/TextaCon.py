import numpy as np

import Setup
import OctalConvertor
import Processing
import Playing
import Printing


####################################
#THE OCTAL NOTE CONVERTOR - TEXTACON
####################################

def Run(
        
            phrase, scale, root,
            
            remove0 = False,
            length = False,
            
            play = False, 
            consoleprint = False, 
            
            textprint = False,
            textprint_location = "",
            
            MIDIprint = False,
            MIDIprint_location = "",
            chord = False,
            notelength = 2,
            veloctiy = 100
            ):

    #INITIAL SETUP
    note_list_full, scale_types_a, note_pos, MIDI_notes, MIDI_numbers, final_note_list \
        = Setup.InitialSetup()

    #SETS THE ROOT NOTE TO USE & BUILDS THE SCALE OF 8 NOTES
    final_note_list = Setup.ScaleBuilder(scale, root,
                                            scale_types_a, note_list_full,
                                            note_pos, final_note_list)

    #TURNS THE PHRASE INTO A SERIES OF NOTES (AND NOTE POSITIONS)
    equation_list, equation_list_numbers, character_list = OctalConvertor.Text(phrase, final_note_list)

    #PROCESSING INTO THE FORMAT THE USER WANTS
    #PART 1 - REMOVES EXCESS NOTES
    equation_list, equation_list_numbers = Processing.RemoveExcessNotes(equation_list, equation_list_numbers, remove0)
    #PART 2 - ADDING NOTES IN
    equation_list, equation_list_numbers = Processing.AddExtraNotes(root, length, equation_list, equation_list_numbers)

    #PLAYING IN THE CONSOLE
    Playing.Console(character_list, play, equation_list, equation_list_numbers, final_note_list, note_list_full)

    #PRINTING TO THE CONSOLE
    Printing.Console(consoleprint, character_list, equation_list, ["symbol", ""])

    #PRINTING TO A TEXT FILE
    Printing.TextFile(root, scale,
                           textprint, textprint_location,
                           character_list, equation_list, ["symbol", "", ""])

    #PRINTING TO A MIDI FILE
    Printing.MIDIFile(root,
            MIDIprint, MIDIprint_location, chord, notelength, veloctiy,
            MIDI_notes, MIDI_numbers, equation_list, equation_list_numbers,
            character_list, "")

################
#END OF FUNCTION
################

#EXAMPLE
Run("₸H1Ⓢ ↿S ÅN ε×4M☧しE", "Major", "C",
        remove0=True, 
        length = 0, 
        play=False, 
        consoleprint = True,
        textprint="Test_func",
        textprint_location = "TEXT_FILES\\",
        MIDIprint="Test_func",
        MIDIprint_location = "MIDI_FILES\\",
        chord = False,
        notelength = 2,
        veloctiy = 50
        )

