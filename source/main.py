from file_handler import IOException, TypeException
from parsing.parse import parser
from parsing.parse_handler import SyntaxRecogException, MachineInitException
import sys
import re

def check_file(file_name):
    if not file_name.endswith('.tur'):
        raise TypeException
    else:
        return True

def file_exec(file_name):
    par = parser()
    count = 0
    with open(file_name) as f:
        for line in f:
            count += 1
            line = re.sub(r'[#].*', "", line)
            line = line.strip()
            if not line:
                continue
            par.set_line_count(count)
            par.parse(line)

def console():
    welcome = "##   Welcome To the Turing Machine Simulation System   ##"
    print '#' * len(welcome)
    print welcome
    print '#' * len(welcome)
    par = parser()
    while True:
        try:
            text = raw_input('\n#Tmachine> ')
            text = re.sub(r'[#].*', "", text)
            text = text.strip()
            if not text:
                continue
            par.parse(text)
        except (SyntaxRecogException, MachineInitException) as s:
            print s

def main():
    try:
        if len(sys.argv) == 1:
            console()
        else:
            read_file = sys.argv[1]
            try:
                check_file(read_file)
                file_exec(read_file)
            except (IOException, TypeException, SyntaxRecogException, MachineInitException) as s:
                print s
    except (KeyboardInterrupt, EOFError) as x:
        print 'print "\nTuring Machine Simulator Terminates ....\n"'

if __name__ == "__main__":
    main()
