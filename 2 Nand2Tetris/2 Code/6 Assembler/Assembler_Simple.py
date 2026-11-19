import sys
import re
import os


def main():

    if len(sys.argv) != 2:
        sys.exit("Python Assembler not used correctly.")
    
    # Pass 1, remove white space and comments
    with open(sys.argv[1], 'r') as f:

        parsed_lines = []
        
        # Advance
        for line in f:
            line = re.sub("//.*", "", line) # Turns // and anything behind it into "", essentially removing comments.
            line = "".join(line.split()) # Remove any additional spaces and other formatting

            # If it isn't an empty line
            if line:
                # There will be later things to check line number here...
                parsed_lines.append(line)


    # Instruction Type
    translated = []
    for p_line in parsed_lines:
                
        # Is this a L_Instruction?
        if p_line[0] == "(":
            raise ValueError("Labels not supported yet")

        # Is this a A_Instruction?
        elif p_line[0] == "@":
            if not p_line[1:].isdigit():
                raise ValueError("Symbols not supported yet")
            else:
                binary = "0" + f"{int(p_line[1:]):015b}"

        # If not the above 2, it must be a C_instruction
        else:
                     
            # To determine which type of C_instruction it is, we check for the existence of "=" and ";
            # binary = fixed prefix + comp + dest + jump
            equals, semicolon = p_line.find("="), p_line.find(";")
                     
            # if both are found, dest=comp;jump
            if equals >= 0 and semicolon >= 0:
                binary = "111" + comp[p_line[equals+1:semicolon]] + dest[p_line[:equals]]+ jump[p_line[semicolon+1:]]

            # if only equals is found, dest=comp
            elif equals >= 0:
                binary = "111" + comp[p_line[equals+1:]] + dest[p_line[:equals]] + "000"

            # if only semicolon is found, comp;jump
            elif semicolon >= 0:
                binary = "111" + comp[p_line[:semicolon]] + "000" + jump[p_line[semicolon+1:]]
            
        translated.append(binary)
        

    # Writes Out
    base, _ = os.path.splitext(sys.argv[1])
    out_name = base + ".hack"
    with open(out_name, "w") as f_out:
        f_out.write("\n".join(translated))


# Pre-defined symbol tables
syms = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'SCREEN': 16384, 'KBD': 24576,
        'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8,
        'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15}

comp = {'0'  : '0101010', '1'  : '0111111', '-1' : '0111010',
        'D'  : '0001100', 'A'  : '0110000', 'M'  : '1110000',
        '!D' : '0001101', '!A' : '0110001', '!M' : '1110001',
        '-D' : '0001111', '-A' : '0110011', '-M' : '1110011',
        'D+1': '0011111', 'A+1': '0110111', 'M+1': '1110111',
        'D-1': '0001110', 'A-1': '0110010', 'M-1': '1110010',
        'D+A': '0000010', 'D+M': '1000010', 'D-A': '0010011',
        'D-M': '1010011', 'A-D': '0000111', 'M-D': '1000111', 
        'D&A': '0000000', 'D&M': '1000000', 'D|A': '0010101', 'D|M': '1010101'}

dest = {'M': '001', 'D': '010', 'DM': '011', 'MD': '011', 'A': '100',
        'AM': '101', 'AD': '110', 'ADM': '111'}

jump = {'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100',
        'JNE': '101', 'JLE': '110', 'JMP': '111'}


main()