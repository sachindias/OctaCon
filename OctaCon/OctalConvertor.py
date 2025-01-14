from PIL import Image
import sys
import numpy as np


##############  #The main heart of the code this
#THE CONVERTOR  #This takes an octal number and
##############  #turns it into a note in the scale

def OctalNoteConverter(octal_no, final_note_list):
    note_order = []
    number_order = []

    if (len(octal_no) < 8):
        length_to_add = 8 - len(octal_no)
    else:
        length_to_add = 0

    octal_equivalent = "0" * length_to_add + octal_no

    for h in range(len(octal_equivalent)):
        note_order.append(final_note_list[int(octal_equivalent[h])])
        number_order.append(octal_equivalent[h])

    return note_order, number_order


###############################################
#GETTING THE CHARACTERS TO TRANSFORM INTO NOTES
###############################################


def Text(phrase, final_note_list):

    equation_list = []  #saves all the notes
    equation_list_numbers = []  #saves all the number positions of each note in the scale

    character_list = list(phrase)

    #these will track the positions of each of the symbol that are input between "//${...}$
    multi_start_pos = []
    multi_end_pos = []

    symbols_file = open("SUPPORTING_FILES\\Symbols.txt", "r")
    symbols_lines = symbols_file.readlines()

    symbol_list = []
    symbol_octal_numbers = []
    for line in symbols_lines:
        symbol_list.append(line.split("   ")[0])
        symbol_octal_numbers.append(line.split("   ")[1][:-1])

    #----------------------------------------------------------------
    #get the positions of the start and end of the input symbols

    index = 0
    while index < len(phrase):
        index = phrase.find('//${', index)
        if index == -1:
            break
        multi_start_pos.append(index)
        index += 4  # +2 because len('//${') == 2

    index2 = 0
    while index2 < len(phrase):
        index2 = phrase.find('}$', index2)
        if index2 == -1:
            break
        multi_end_pos.append(index2)
        index2 += 2  # +2 because len('}$') == 2

    #----------------------------------------------------------------
    #error messages for invalid syntax

    if (len(multi_start_pos) > len(multi_end_pos)):
        print('\n\033[1;31;48m' + "Error:", '\033[1;37;0m' + "improper syntax: //${...}$ not closed correctly\n")
        sys.exit(1)
    elif (len(multi_start_pos) < len(multi_end_pos)):
        print('\n\033[1;31;48m' + "Error:", '\033[1;37;0m' + "improper syntax: //${...}$ not opened correctly\n")
        sys.exit(1)

    #----------------------------------------------------------------
    #replaces the old character list with a new one including symbols

    new_character_list = []

    count = 0
    while (count < len(character_list)):

        if (count in multi_start_pos):

            loc = np.where(np.array(multi_start_pos) == count)[0][0]
            symbol = phrase[multi_start_pos[loc]+4:multi_end_pos[loc]]
            new_character_list.append(symbol)
            count = count + 5 + len(symbol)

        else:
            new_character_list.append(character_list[count])

        count = count + 1

    #----------------------------------------------------------------
    #goes through new character list and finds octal numbers for each

    for n in range(len(new_character_list)):
        if (len(new_character_list[n]) == 1):
            character = new_character_list[n]
            octal_no = oct(ord(character))[2:]

        else:
            try:
                symbol_loc = np.where(np.array(symbol_list) == new_character_list[n])[0][0]
                octal_no = symbol_octal_numbers[symbol_loc]
                count = count + len(new_character_list[n]) + 6

            #error if the symbol is not in the symbol file or has been entered incorrectly
            except Exception:
                    print('\n\033[1;31;48m' + "Error:", '\033[1;37;0m' + "symbol not found: %s\n" % new_character_list[n])
                    sys.exit(1)


        note_order, number_order = OctalNoteConverter(octal_no, final_note_list)
        equation_list.append(note_order)
        equation_list_numbers.append(number_order)

    character_list = new_character_list

    return equation_list, equation_list_numbers, character_list


##########################################
#GETTING THE IMAGE TO TRANSFORM INTO NOTES
##########################################

def Pictures(filename, final_note_list):

    equation_list = [] #saves all the notes
    equation_list_numbers = [] #saves all the number positions of each note in the scale

    #Load the image
    img = Image.open("INPUT_PICTURES\%s" %filename)

    #Convert image to RGB if not already in RGB mode
    if (img.mode != 'RGB'):
        img = img.convert('RGB')

    #Get pixel data & Convert RGB to Hex
    pixels = list(img.getdata())  #This returns a list of (R, G, B) tuples
    hex_colours = [f'{r:02x}{g:02x}{b:02x}' for r, g, b in pixels]

    for count in range(len(hex_colours)):
        hex_colour = hex_colours[count]
        octal_no = oct(int(hex_colour, 16))[2:]
        note_order, number_order = OctalNoteConverter(octal_no, final_note_list)
        equation_list.append(note_order)
        equation_list_numbers.append(number_order)

    return equation_list, equation_list_numbers, hex_colours



