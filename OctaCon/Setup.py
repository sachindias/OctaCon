import numpy as np


##############
#INITIAL SETUP
##############

def InitialSetup():

    #List of all 12 notes
    note_list_full = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    scale_types = open("SUPPORTING_FILES\\Scales.txt", "r")
    scale_type_lines = scale_types.readlines()

    scale_types_a = []
    note_pos = []

    for x in scale_type_lines:
        scale_types_a.append(x.split('   ')[0])
        note_pos_temp = []
        for n in range(8):
            note_pos_temp.append(int(x.split('   ')[n +1]))
        note_pos.append(note_pos_temp)

    MIDI_notes = np.array(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
                           "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
    MIDI_numbers = np.array([x for x in range(48 ,72)])

    final_note_list = []

    return note_list_full, scale_types_a, note_pos, MIDI_notes, MIDI_numbers, final_note_list



########################################################
#SETS THE ROOT NOTE TO USE & BUILDS THE SCALE OF 8 NOTES
########################################################

def ScaleBuilder(
        scale,
        root,

        scale_types_a,
        note_list_full,
        note_pos,
        final_note_list
        ):

    #Finds the correct scale from the list
    scale_name_no = np.where(scale.lower() == np.array(scale_types_a))

    try:
        scale_tester = scale_name_no[0][0]
    except Exception:
        print('\n\033[1;31;48m' + "Error:", '\033[1;37;0m' + "scale not found\n")

    if (len(root) < 3):
        root = root.upper()

        if (len(root) == 2):
            if (root[1] == "B"):
                if (root[0] == "A"):
                    root = "G" + "#"
                else:
                    root = chr(ord(root[0]) - 1) + "#"

        root_pos = np.where(np.array(note_list_full) == root)

        #Gets all notes between start & end of scale &
        #gets the correct positions of notes in the scale
        if (len(root_pos[0]) != 0):
            root_pos = root_pos[0][0]
            new_note_list = note_list_full[root_pos:] + note_list_full[:root_pos]
            note_pos_new = note_pos[scale_name_no[0][0]]

            #Builds the scale
            for t in range(len(note_pos_new)):
                final_note_list.append(new_note_list[note_pos_new[t] - 1])

        if (len(final_note_list) == 0):
            print('\n\033[1;31m' + "Error:", '\033[1;37m' + "root note invalid\n")

    else:
        print('\n\033[1;31m' + "Error:", '\033[1;37m' + "root note invalid\n")

    return final_note_list
