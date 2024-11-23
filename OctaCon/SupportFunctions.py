
#########################
#REMOVE BLANK LINES
#########################

def RemoveBlankLines(filename):
    keep_lines = []
    
    with open("SUPPORTING_FILES/%s.txt" %filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if (line != '\n'):
                keep_lines.append(line)

    with open("SUPPORTING_FILES/%s.txt" %filename, "w") as file:
        for n in range(len(keep_lines)):
            file.write(keep_lines[n])
