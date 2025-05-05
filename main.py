from analyser.parser import parse_file
from rules.unused_variables import find_unused_variables
from rules.unused_functions import find_unused_functions
from rules.unreachable_code import detect_unreachable_code

def main():
    lines = parse_file("tests/test.py")
    variableName = find_unused_variables(lines)
    functionUnused = find_unused_functions(lines)
    linesUnreachable = detect_unreachable_code(lines)

    for var_name, lineNo in variableName.items():
        print(f"Variable: '{var_name}' at line number '{lineNo}' is not used.")
    
    for func_name, lineNo in functionUnused.items():
        print(f"Function: '{func_name}' at line number '{lineNo}' is not used.")
    
    for lineNo in linesUnreachable:
        print(f"Unreachable code detected at '{lineNo}'")
    

if __name__ == "__main__":
    main()