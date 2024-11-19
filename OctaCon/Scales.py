import SupportFunctions

#########################
#ADD TO SCALES
#########################

#Metadata should be in the form [1,2,3,4,5,6,7,8]
def Add(scale, metadata):
    
    input_string = scale
    for n in range(8):
        input_string = input_string + "   " + str(metadata[n])
    
    with open("SUPPORTING_FILES/Scales.txt", "a") as file:
        file.write("\n" + input_string)

        
    SupportFunctions.removeBlankLines("Scales")

#########################
#DELETE FROM SCALES
#########################

def Delete(scale):
    
    keep_lines = []
    
    with open("SUPPORTING_FILES/Scales.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            name = line.split("   ")[0]
            if (name != scale):
                keep_lines.append(line)

    with open("SUPPORTING_FILES/Scales.txt", "w") as file:
        for n in range(len(keep_lines)):
            file.write(keep_lines[n])
    
    SupportFunctions.removeBlankLines("Scales")

#########################
#AMEND SCALES
#########################
    
def Amend(change, scale, name = False, position = False, note = False):
    
    keep_lines = []
    
    if (change == "name"):
        
        with open("SUPPORTING_FILES/Scales.txt", "r") as file:
            lines = file.readlines()
            for line in lines: 
                name_old = line.split("   ")[0]
                
                if (name_old != scale):
                    keep_lines.append(line) 
                
                elif (name_old == scale):
                    keep_lines.append(name + "   " + line.split(name_old)[1])

        with open("SUPPORTING_FILES/Scales.txt", "w") as file:
            for n in range(len(keep_lines)):
                file.write(keep_lines[n])                
        
        
    if (change == "note"):    
        
        with open("SUPPORTING_FILES/Scales.txt", "r") as file:
            lines = file.readlines()
            for line in lines: 
                scale_name = line.split("   ")[0]
                
                if (scale_name != scale):
                    keep_lines.append(line) 
                    
                elif (scale_name == scale):
                    notes = line.split("   ")
                    notes[position + 1] = str(note)
                    keep_lines.append('   '.join(notes))
                              
        with open("SUPPORTING_FILES/Scales.txt", "w") as file:
            for n in range(len(keep_lines)):
                file.write(keep_lines[n])          
        
    SupportFunctions.removeBlankLines("Scales")