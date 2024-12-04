import numpy as np
from mido import Message, MidiFile, MidiTrack


########################
#PRINTING TO THE CONSOLE
########################

def Console(consoleprint, input_list, equation_list, text_options):

    if (consoleprint == True):
        print("\nHere is the order of notes:")
        for n in range(len(equation_list)):
            print("[", n, "]", "[%s = %s%s]" %(text_options[0], text_options[1], input_list[n]), equation_list[n])



########################
#PRINTING TO A TEXT FILE
########################

def TextFile(

        root,
        scale,

        textprint,
        textprint_location,

        input_list,
        equation_list,
        text_options
        ):

    if (textprint != False):

        file_name = textprint
        file = open("%s%s.txt" % (textprint_location, file_name), "w", encoding="utf-8")

        if (text_options[0] == "colour"):
            input_list = [item.upper() for item in input_list]

        file.write("Input %s: \n" %(text_options[0].capitalize() + "s"))
        for n in range(len(input_list)):
            file.write("%s%s%s" %(text_options[1], input_list[n], text_options[2]))

        TS = len(equation_list[0])

        file.write("\n\nScale: %s %s - Suggested Time Signature: %s/4\n\n" % (root, scale[0].upper() + scale[1:], TS))
        file.write("Full Information:\n")
        for n in range(len(input_list)):
            file.write("[%s]%s" % (n + 1, " " * int(7 - int(str(np.log10(n + 1))[0]))))
            file.write("[%s = %s%s]  " %(text_options[0], text_options[1], input_list[n]))
            file.write("%s" % equation_list[n])
            file.write("\n")

        file.close()



########################
#PRINTING TO A MIDI FILE
########################

def MIDIFile(

    root,

    MIDIprint,
    MIDIprint_location,
    chord,
    notelength,
    veloctiy,

    MIDI_notes,
    MIDI_numbers,
    equation_list,
    equation_list_numbers,

    input_list,
    text_options
    ):

    if (MIDIprint != False):

        file_name_MIDI = MIDIprint

        mid = MidiFile(type=1)
        track = MidiTrack()
        mid.tracks.append(track)
        start_note = np.where(MIDI_notes == root)[0][0]
        last_note = np.where(MIDI_notes == root)[0][1]

        for n in range(len(equation_list)):
            chord_used_list = []
            for i in range(len(equation_list[0])):

                if (equation_list[n][i] == root):

                    if (int(equation_list_numbers[n][i]) == 0):
                        MIDI_pos = start_note

                    elif (int(equation_list_numbers[n][i]) == 7):
                        MIDI_pos = last_note
                else:

                    MIDI_pos_temp = np.where(MIDI_notes == equation_list[n][i])[0]
                    for k in range(len(MIDI_pos_temp)):
                        if (MIDI_pos_temp[k] > start_note):
                            if (MIDI_pos_temp[k] < last_note):
                                MIDI_pos = MIDI_pos_temp[k]

                if (chord == False):
                    track.append(Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=veloctiy, time=0))
                    track.append(Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=0,
                                         time=int(1920 * notelength)))

                elif (chord == True):
                    if (MIDI_pos not in chord_used_list):
                        track.append(
                            Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=veloctiy, time=0))
                        chord_used_list.append(MIDI_pos)

                    else:
                        if (text_options == "#"):
                            input_list = [item.upper() for item in input_list]
                        print('\n\033[1;33m' + "WARNING:",
                              '\033[1;37m' + "duplicates notes were found and removed in '%s%s', this can occur for chords" %(text_options,input_list[n]))

            if (chord == True):
                end_of_chord_list = np.flip(chord_used_list[:-1])

                track.append(Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=0,
                                     time=int(1920 * notelength)))
                for end in range(len(end_of_chord_list)):
                    track.append(
                        Message('note_on', channel=0, note=MIDI_numbers[end_of_chord_list[end]], velocity=0, time=0))

                chord_used_list.append(MIDI_pos)

        mid.save("%s%s.mid" % (MIDIprint_location, file_name_MIDI))