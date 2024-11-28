import numpy as np



##########################################################################
#PROCESSING INTO THE FORMAT THE USER WANTS - PART 1 - REMOVES EXCESS NOTES
##########################################################################

def RemoveExcessNotes(
        equation_list,
        equation_list_numbers,
        remove0,
        ):

    measures_array = np.array([0 ,0 ,0 ,0 ,0 ,0])

    for i in range(len(measures_array)):
        n = 0
        while (n < (len(equation_list_numbers))):
            if (int(equation_list_numbers[n][i]) != 0):
                measures_array[i] = 1
            n = n + 1

    if (remove0 == True):
        new_equation_list = [None ] *len(equation_list)
        new_equation_list_numbers = [None ] *len(equation_list_numbers)

        try:
            removal_loop_no = np.where(measures_array == 1)[0][0]
            for n in range(len(equation_list)):
                new_equation_list[n] = equation_list[n][removal_loop_no:]
                new_equation_list_numbers[n] = equation_list_numbers[n][removal_loop_no:]

            equation_list = new_equation_list
            equation_list_numbers = new_equation_list_numbers
        except Exception:
            (1 == 1)

    return equation_list, equation_list_numbers




#####################################################################
#PROCESSING INTO THE FORMAT THE USER WANTS - PART 2 - ADDING NOTES IN
#####################################################################

def AddExtraNotes(
        root,
        length,

        equation_list,
        equation_list_numbers
        ):

    if (length != False):
        if (length > len(equation_list[0])):
            length_to_add = length - len(equation_list[0])
            extra_notes_to_add = [root] * length_to_add
            extra_numbers_to_add = ["0"] * length_to_add

            new_equation_list = [None] * len(equation_list)
            new_equation_list_numbers = [None] * len(equation_list_numbers)

            for n in range(len(equation_list)):
                new_equation_list[n] = np.concatenate((extra_notes_to_add, equation_list[n]))
                new_equation_list_numbers[n] = np.concatenate((extra_numbers_to_add, equation_list_numbers[n]))

            equation_list = new_equation_list
            equation_list_numbers = new_equation_list_numbers

    return equation_list, equation_list_numbers

