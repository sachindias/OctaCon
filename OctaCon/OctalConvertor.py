from PIL import Image


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
    for count in range(len(character_list)):
        character = character_list[count]
        octal_no = oct(ord(character))[2:]
        note_order, number_order = OctalNoteConverter(octal_no, final_note_list)
        equation_list.append(note_order)
        equation_list_numbers.append(number_order)

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



