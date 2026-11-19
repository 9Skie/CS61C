from pathlib import Path
import sys
import re
from enum import Enum



class CommandType(Enum):
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    C_IF = 5
    C_FUNCTION = 6
    C_RETURN = 7
    C_CALL = 8
    UNDEFINED = 9



class Parser:

    def __init__(self, file_name):

        vm_file = file_name + ".vm"
        with open(vm_file, "r") as vm_file:
            parsed_lines = []

            # discard white space and comments
            for line in vm_file:
                line = re.sub("//.*", "", line).strip()
                commands = line.split()
                if commands:
                    parsed_lines.append(commands)

        self.parsed_lines = parsed_lines
        self.index = 0

    def advance(self):
        self.index += 1

    def has_more_lines(self):
        return self.index < len(self.parsed_lines)
        
    def command_type(self):
        if self.parsed_lines[self.index][0] == "pop":
            return CommandType.C_POP
        elif self.parsed_lines[self.index][0] == "push":
            return CommandType.C_PUSH
        elif self.parsed_lines[self.index][0] in ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not",]:
            return CommandType.C_ARITHMETIC
            
        # the other types we have not currently encountered, as we are only doing pop/push, arithmetic/logic here

    def arg1(self):
        if self.command_type() == CommandType.C_ARITHMETIC:
            return self.parsed_lines[self.index][0]
        else:
            return self.parsed_lines[self.index][1]
        

    def arg2(self):
        if self.command_type() in [CommandType.C_PUSH, CommandType.C_POP, CommandType.C_FUNCTION, CommandType.C_CALL]:
            return int(self.parsed_lines[self.index][2])
        


class Writer:

    def __init__(self, file_name):

        self.filename = file_name
        self.output_f = open(file_name + ".asm", "w")
        self.label_counter = 0 # I like to call it comparison counter


    def write_arithmetic(self, command):
        
        # in chapter 7, it has not pre-defined how to exactly convert certain VM operations into assembler code.
        # so, some of these are just written as we go, and no, there really are no shortcutes to any of these

        # this line is here just for the clarity for us to know what VM byte code operation we turned into assembly
        self.output_f.write(f"// {command}\n")

        # remember kids, all of these just: 1. pop 2 values off top of stack, 2. do logical operation, 3. put result back
        # except neg and not

        if command == "neg":
            commands = [
                # pop
                "@SP", 
                "A=M-1", 
                #neg
                "M=-M"]
        elif command == "not":
            commands = [
                # pop
                "@SP", 
                "A=M-1", 
                # neg
                "M=!M"]

        else:
            commands = [
                # pop
                "@SP",
                "AM=M-1",
                "D=M",

                # pop
                "A=A-1",
            ]

            match command:
                case "add": 
                    commands.append(
                        # add
                        "M=D+M"
                    )
                case "sub":
                    commands.append(
                        # sub
                        "M=M-D"
                    )
                case "and":
                    commands.append(
                        # and
                        "M=D&M"
                    )
                case "or":
                    commands.append(
                        # or
                        "M=D|M"
                    )

                # these 3 are very annoying to deal with, as hack doesn't natively have comparisons between numbers
                # only between a number and 0
                # so gotta make it yourself!

                case "eq":
                    commands.extend(self.write_bool("JEQ"))
                
                case "gt":
                    commands.extend(self.write_bool("JGT"))

                case "lt":
                    commands.extend(self.write_bool("JLT"))

        # write the actual commands into the file
        commands = list(map(lambda x: x + "\n", commands))
        self.output_f.write("".join(commands))


    def write_bool(self, comparison_type):

        comparison = [
            # subtract the already popped 2 values
            "D=M-D",

            # check condition based on type
            f"@{comparison_type}_Success_{self.label_counter}",
            f"D;{comparison_type}",

            # Failed
            "@SP",
            "A=M-1",
            "M=0",
            f"@{comparison_type}_Skip_{self.label_counter}",
            "0;JMP",

            # Success
            f"({comparison_type}_Success_{self.label_counter})",
            "@SP",
            "A=M-1",
            "M=-1",

            # Skip from Fail (rr continue from Success)
            f"({comparison_type}_Skip_{self.label_counter})"
        ]

        self.label_counter += 1
        return comparison
    

    def write_push_pop(self, command, arg1, arg2):

        # this line is here just for the clarity for us to know what VM byte code operation we turned into assembly
        self.output_f.write(f"// {command}\n")
        
        if command == "push":

            match arg1:
                case "constant":
                    commands = [

                        # put value of arg2 into D
                        f"@{arg2}",
                        "D=A",

                        # push D into stack
                        "@SP",
                        "A=M",
                        "M=D",

                        # increment pointer value
                        "@SP",
                        "M=M+1"
                    ]
                    
                case "static":
                    commands = [

                        # retrieve value at a specific memory location, put into D
                        f"@{self.filename}.{arg2}",
                        "D=M",

                        # push D into stack
                        "@SP",
                        "A=M",
                        "M=D",

                        # increment pointer value
                        "@SP",
                        "M=M+1"
                    ]

                # the rest we haven't covered yet! Like temp or pointer

                
        if command == "pop":

            # you can't pop a constant!

            match arg1:
                case "static":
                    commands = [
                        # decrement pointer value
                        "@SP",
                        "AM=M-1",

                        # retireve value from top of stack
                        "D=M",

                        # put at a specific memory location
                        f"@{self.filename}.{arg2}",
                        "M=D",
                    ]
        
        # write the actual commands into the file
        commands = list(map(lambda x: x + "\n", commands))
        self.output_f.write("".join(commands))
    

    def close(self):
        self.output_f.close()



def main():
    if len(sys.argv) != 2:
        sys.exit("VM File Not Found.")

    vm_path = Path(sys.argv[1])   
    parser = Parser(vm_path.stem)
    writer = Writer(vm_path.stem)

    while parser.has_more_lines():
        if parser.command_type() == CommandType.C_ARITHMETIC:
            writer.write_arithmetic(parser.arg1())
        elif parser.command_type() == CommandType.C_PUSH or parser.command_type() == CommandType.C_POP:
            writer.write_push_pop(parser.parsed_lines[parser.index][0], parser.arg1(), parser.arg2())
        parser.advance()

    # don't know how to delete the last "\n" charater
    writer.close()


if __name__ == "__main__":
    main()
            

        