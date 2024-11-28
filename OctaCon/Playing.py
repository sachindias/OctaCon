import numpy as np
from time import sleep
import sys
import winsound


#######################
#PLAYING IN THE CONSOLE
#######################

def Console(
        input_list,

        play,

        equation_list,
        equation_list_numbers,
        final_note_list,
        note_list_full,
        ):

    if (play == True):

        if (len(equation_list) > 0):
            space_len = 0
            percentage_norm = 100 / ((len(input_list) * (len(equation_list[0]) + 1) - 1))

        print("\nNotes Will Be Played Below:")
        sleep(1)
        j = 1

        for n in range(len(input_list)):
            if (n > 0):
                sys.stdout.write('\r')
                sys.stdout.write("[%-40s] %d%%   Note: %s" % (
                '=' * round(0.4 * percentage_norm * (space_len + j + 1)), percentage_norm * (space_len + j + 2), "  "))
                space_len = len(equation_list[0]) * n + n

                winsound.PlaySound("Notes\\space", winsound.SND_FILENAME)

            for j in range(len(equation_list[0])):
                sys.stdout.write('\r')
                sys.stdout.write("[%-40s] %d%%   Note: %s" % (
                '=' * round(0.4 * percentage_norm * (space_len + j + 1)), percentage_norm * (space_len + j + 1),
                final_note_list[int(equation_list_numbers[n][j])]))
                sys.stdout.flush()

                equation_sound_note = final_note_list[int(equation_list_numbers[n][j])]
                loc_root = np.where(np.array(note_list_full) == "G#")[0][0]

                if (np.where(np.array(note_list_full) == equation_sound_note)[0][0] < loc_root):
                    winsound.PlaySound("Notes\\high_%s" % equation_sound_note, winsound.SND_FILENAME)
                elif (np.where(np.array(note_list_full) == equation_sound_note)[0][0] > loc_root):
                    winsound.PlaySound("Notes\\low_%s" % equation_sound_note, winsound.SND_FILENAME)
                elif (np.where(np.array(note_list_full) == equation_sound_note)[0][0] == loc_root and int(
                        equation_list_numbers[n][j]) == 7):
                    winsound.PlaySound("Notes\\high_%s" % equation_sound_note, winsound.SND_FILENAME)
                elif (np.where(np.array(note_list_full) == equation_sound_note)[0][0] == loc_root):
                    winsound.PlaySound("Notes\\low_%s" % equation_sound_note, winsound.SND_FILENAME)
                sleep(0.2)

        print("\n")