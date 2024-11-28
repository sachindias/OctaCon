import numpy as np

import Setup
import Processing
import Playing
import Printing
import OctalConvertor


####################################
#THE OCTAL NOTE CONVERTOR - PICTACON
####################################

def Run(

        filename, scale, root,

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

    #TURNS THE PICTURE INTO A SERIES OF NOTES (AND NOTE POSITIONS)
    equation_list, equation_list_numbers, hex_colours = OctalConvertor.Pictures(filename, final_note_list)

    #PROCESSING INTO THE FORMAT THE USER WANTS
    #PART 1 - REMOVES EXCESS NOTES
    equation_list, equation_list_numbers = Processing.RemoveExcessNotes(equation_list, equation_list_numbers, remove0)
    #PART 2 - ADDING NOTES IN
    equation_list, equation_list_numbers = Processing.AddExtraNotes(root, length, equation_list, equation_list_numbers)

    #PLAYING IN THE CONSOLE
    Playing.Console(hex_colours, play, equation_list, equation_list_numbers, final_note_list, note_list_full)

    #PRINTING TO THE CONSOLE
    Printing.Console(consoleprint, hex_colours, equation_list, ["colour", "#"])

    #PRINTING TO A TEXT FILE
    Printing.TextFile(root, scale,
                           textprint, textprint_location,
                           hex_colours, equation_list, ["colour", "#", " "])

    #PRINTING TO A MIDI FILE
    Printing.MIDIFile(root,
            MIDIprint, MIDIprint_location, chord, notelength, veloctiy,
            MIDI_notes, MIDI_numbers, equation_list, equation_list_numbers,
            hex_colours, "#")

################
#END OF FUNCTION
################

#EXAMPLE
Run("Tester2.png", "Major", "C",
        remove0=True,
        length = 2,
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




