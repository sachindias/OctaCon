import numpy as np 
import winsound
from time import sleep
import sys
from mido import Message, MidiFile, MidiTrack


#########################
#THE OCTAL NOTE CONVERTOR
#########################

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

    ##############  #The main heart of the code, this takes a character
    #THE CONVERTOR  #and turns it into a note in the defined scale
    ##############  #inputs require the character, list of notes in the scale [final_note_list]

    def octal_note_converter(character, final_note_list):
    
        note_order = []
        number_order = []
        
        unicode_character = oct(ord(character))[2:]
    
        if (len(unicode_character) < 8):
            length_to_add = 8 - len(unicode_character)
        else:
            length_to_add = 0
        
        octal_equivalent = "0"*length_to_add + unicode_character
    
        for h in range(len(octal_equivalent)):
    
            note_order.append(final_note_list[int(octal_equivalent[h])])
            number_order.append(octal_equivalent[h])
                
        return note_order, number_order
   
    
   
    ##############
    #INITIAL SETUP
    ##############
    
    #List of all 12 notes
    note_list_full = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
 
    scale_types = open("SUPPORTING_FILES\\scale_types.txt", "r")
    scale_type_lines = scale_types.readlines()
 
    scale_types_a = []
    note_pos = []
 
    for x in scale_type_lines:
        scale_types_a.append(x.split('   ')[0])
        note_pos_temp = []
        for n in range(8):
            note_pos_temp.append(int(x.split('   ')[n+1]))
        note_pos.append(note_pos_temp)
        
    MIDI_notes = np.array(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",
                           "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
    MIDI_numbers = np.array([x for x in range(48,72)])
    
    final_note_list = []



    ##########################
    #SETS THE ROOT NOTE TO USE
    ##########################
    
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
        
        if (len(root_pos[0]) != 0):     
            root_pos = root_pos[0][0]
            new_note_list = note_list_full[root_pos:] + note_list_full[:root_pos]
            note_pos_new = note_pos[scale_name_no[0][0]]
            
            for t in range(len(note_pos_new)):
                final_note_list.append(new_note_list[note_pos_new[t]-1])
        
        if (len(final_note_list) == 0):
            print('\n\033[1;31m' + "Error:", '\033[1;37m' + "root note invalid\n")  
     
    else:
        print('\n\033[1;31m' + "Error:", '\033[1;37m' + "root note invalid\n")           
     
        
     
    ###############################################
    #GETTING THE CHARACTERS TO TRANSFORM INTO NOTES
    ###############################################       
      
    equation_list = [] #saves all the notes 
    equation_list_numbers = [] #saves all the number positions of each note in the scale
    
    character_list = list(phrase)
    for count in range(len(character_list)):
        character = character_list[count]
        note_order, number_order = octal_note_converter(character,final_note_list)
        equation_list.append(note_order)
        equation_list_numbers.append(number_order)
              


 
    ##########################################################################    
    #PROCESSING INTO THE FORMAT THE USER WANTS - PART 1 - REMOVES EXCESS NOTES
    ##########################################################################
    
    measures_array = np.array([0,0,0,0,0,0])
    
    for i in range(len(measures_array)):
        n = 0
        while (n < (len(equation_list_numbers))):
            #print(n, "-")
            if (int(equation_list_numbers[n][i]) != 0):
                measures_array[i] = 1
            n = n + 1

    if (remove0 == True):
        new_equation_list = [None]*len(equation_list)
        new_equation_list_numbers = [None]*len(equation_list_numbers)
        
        try:
            removal_loop_no = np.where(measures_array == 1)[0][0]           
            for n in range(len(equation_list)):
                new_equation_list[n] = equation_list[n][removal_loop_no:]
                new_equation_list_numbers[n] = equation_list_numbers[n][removal_loop_no:]
                
            equation_list = new_equation_list 
            equation_list_numbers = new_equation_list_numbers
        except Exception:
            (1 == 1)



    #####################################################################    
    #PROCESSING INTO THE FORMAT THE USER WANTS - PART 2 - ADDING NOTES IN
    #####################################################################           

    if (length != False):
        if (length > len(equation_list[0])):
            length_to_add = length - len(equation_list[0])
            extra_notes_to_add = [root]*length_to_add
            extra_numbers_to_add = ["0"]*length_to_add
            
            new_equation_list = [None]*len(equation_list)
            new_equation_list_numbers = [None]*len(equation_list_numbers)
            
            for n in range(len(equation_list)):
                new_equation_list[n] = np.concatenate((extra_notes_to_add, equation_list[n]))
                new_equation_list_numbers[n] = np.concatenate((extra_numbers_to_add, equation_list_numbers[n]))
            
            equation_list = new_equation_list  
            equation_list_numbers = new_equation_list_numbers



    #######################    
    #PLAYING IN THE CONSOLE
    #######################

    if (play == True):  
        
        if (len(equation_list) > 0):
            space_len = 0
            percentage_norm = 100/((len(character_list) * (len(equation_list[0]) + 1) - 1))
        
        print("\nNotes Will Be Played Below:")
        sleep(1)
        j = 1
         
        for n in range(len(character_list)):
            if (n > 0):
                sys.stdout.write('\r')
                sys.stdout.write("[%-40s] %d%%   Note: %s" % ('='*round(0.4*percentage_norm*(space_len + j + 1)), percentage_norm*(space_len + j + 2), "  "))
                space_len = len(equation_list[0])*n + n
                
                winsound.PlaySound("Notes\\space", winsound.SND_FILENAME)
                 
            for j in range(len(equation_list[0])):
                sys.stdout.write('\r')
                sys.stdout.write("[%-40s] %d%%   Note: %s" % ('='*round(0.4*percentage_norm*(space_len + j + 1)), percentage_norm*(space_len + j + 1), final_note_list[int(equation_list_numbers[n][j])]))
                sys.stdout.flush()
                
                equation_sound_note = final_note_list[int(equation_list_numbers[n][j])]        
                loc_root = np.where(np.array(note_list_full) == "G#")[0][0]
                
                if (np.where(np.array(note_list_full) == equation_sound_note)[0][0] < loc_root):
                    winsound.PlaySound("Notes\\high_%s" %equation_sound_note, winsound.SND_FILENAME)   
                elif (np.where(np.array(note_list_full) == equation_sound_note)[0][0] > loc_root):
                    winsound.PlaySound("Notes\\low_%s" %equation_sound_note, winsound.SND_FILENAME)
                elif (np.where(np.array(note_list_full) == equation_sound_note)[0][0] == loc_root and int(equation_list_numbers[n][j]) == 7):
                    winsound.PlaySound("Notes\\high_%s" %equation_sound_note, winsound.SND_FILENAME)
                elif (np.where(np.array(note_list_full) == equation_sound_note)[0][0] == loc_root):
                    winsound.PlaySound("Notes\\low_%s" %equation_sound_note, winsound.SND_FILENAME)  
                sleep(0.2)

        print("\n")



    ########################   
    #PRINTING TO THE CONSOLE
    ########################
    
    if (consoleprint == True):
        print("\nHere is the order of notes:")
        for n in range(len(equation_list)): 
            print("[", n, "]", "[symbol = ",character_list[n], "]", equation_list[n])



    ######################## 
    #PRINTING TO A TEXT FILE
    ########################

    if (textprint != False):
        
        file_name = textprint
        file = open("%s%s.txt" %(textprint_location, file_name), "w", encoding="utf-8")

        file.write("Input Symbols: \n\n")
        for n in range(len(character_list)):
            file.write("%s" %character_list[n])
            
        TS = len(equation_list[0])
        
        file.write("\n\nScale: %s %s - Suggested Time Signature: %s/4\n\n" %(root, scale[0].upper() + scale[1:],TS))
        file.write("Full Information:\n")
        for n in range(len(character_list)):
            
                file.write("[%s]%s" %(n+1," "*int(7-int(str(np.log10(n+1))[0]))))
                file.write("[symbol = %s]  " %(character_list[n]))
                file.write("%s" %equation_list[n])
                file.write("\n")
                
        file.close()   
        
        
    ########################   
    #PRINTING TO A MIDI FILE
    ########################

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
                    track.append(Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=0, time=int(1920/4/notelength)))
                
                elif (chord == True):
                    if (MIDI_pos not in chord_used_list):
                        track.append(Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=veloctiy, time=0))
                        chord_used_list.append(MIDI_pos)

                    else:
                       print('\n\033[1;33m' + "WARNING:", '\033[1;37m' + "duplicates notes were found and removed in '%s', this can occur for chords" %character_list[n])    
                       
            if (chord == True):
                end_of_chord_list = np.flip(chord_used_list[:-1]) 
                
                track.append(Message('note_on', channel=0, note=MIDI_numbers[MIDI_pos], velocity=0, time=int(1920/4/notelength)))   
                for end in range(len(end_of_chord_list)):
                    track.append(Message('note_on', channel=0, note=MIDI_numbers[end_of_chord_list[end]], velocity=0, time=0))
                
                chord_used_list.append(MIDI_pos)
                    
        mid.save("%s%s.mid" %(MIDIprint_location, file_name_MIDI))
    
    
    
    ############################   
    #FINAL STEPS OF THE FUNCTION
    ############################


    equation_list = np.array(equation_list)
    equation_list_numbers = np.array(equation_list_numbers)

################  
#END OF FUNCTION
################



#EXAMPLE
'''
TextCon("₸H1Ⓢ ↿S ÅN ε×4M☧しE", "Major", "C", 
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
'''
