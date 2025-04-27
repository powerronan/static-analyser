from analyser.parser import parse_file
from rules.unused_variables import find_unused_variables
from rules.unused_functions import find_unused_functions

def main():
    lines = parse_file("tests/test.py")
    variableName = find_unused_variables(lines)
    functionUnused = find_unused_functions(lines)

    for unused in variableName:
        print(unused)
    
    for unused in functionUnused:
        print(unused)
    

if __name__ == "__main__":
    main()