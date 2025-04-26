# Handle parsing files

def parse_file(filepath):
    file = open(filepath, "r")
    content = file.read()
    print(content)
    file.close()