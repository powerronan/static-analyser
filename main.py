from analyser.parser import parse_file
from rules.unused_variables import find_unused_variables

def main():
    lines = parse_file("tests/test.py")
    variableName = find_unused_variables(lines)

    print(variableName)
    

if __name__ == "__main__":
    main()