import SupportFunctions

#########################
#ADD TO SYMBOLS
#########################

def Add(symbol, octal):
    
    input_string = symbol + "   " + str(octal)
    
    with open("SUPPORTING_FILES/Symbols.txt", "a") as file:
        file.write("\n" + input_string)

        
    SupportFunctions.RemoveBlankLines("Symbols")
    

#########################
#DELETE FROM SYMBOLS
#########################

def Delete(symbol):
    
    keep_lines = []
    
    with open("SUPPORTING_FILES/Symbols.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            name = line.split("   ")[0]
            if (name != symbol):
                keep_lines.append(line)

    with open("SUPPORTING_FILES/Symbols.txt", "w") as file:
        for n in range(len(keep_lines)):
            file.write(keep_lines[n])
    
    SupportFunctions.RemoveBlankLines("Symbols")
    
    
#########################
#AMEND SYMBOLS
#########################
    
def Amend(change, symbol, name = False, octal = False):
    
    keep_lines = []
    
    if (change == "name"):
        
        with open("SUPPORTING_FILES/Symbols.txt", "r") as file:
            lines = file.readlines()
            for line in lines: 
                name_old = line.split("   ")[0]
                
                if (name_old != symbol):
                    keep_lines.append(line) 
                
                elif (name_old == symbol):
                    keep_lines.append(name + "   " + line.split("   ")[1])

        with open("SUPPORTING_FILES/Scales.txt", "w") as file:
            for n in range(len(keep_lines)):
                file.write(keep_lines[n])                
        
        
    if (change == "octal"):    
        
        with open("SUPPORTING_FILES/Symbols.txt", "r") as file:
            lines = file.readlines()
            for line in lines: 
                symbol_name = line.split("   ")[0]
                
                if (symbol_name != symbol):
                    keep_lines.append(line) 
                    
                elif (symbol_name == symbol):
                    keep_lines.append(symbol + "   " + line.split("   ")[1])
                              
        with open("SUPPORTING_FILES/Symbols.txt", "w") as file:
            for n in range(len(keep_lines)):
                file.write(keep_lines[n])          
        
    SupportFunctions.RemoveBlankLines("Symbols")