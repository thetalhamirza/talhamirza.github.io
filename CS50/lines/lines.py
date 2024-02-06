import sys

def main():
    try:
        if len(sys.argv) > 2: sys.exit("Too many command-line arguments")
        filename = sys.argv[1]
        if verify(filename):
            print(lines(filename))

    except IndexError:
        sys.exit("Too few command-line arguments")


def verify(filename):
    if filename[-3:] != '.py': sys.exit("Not a Python file")
    try:
        with open(filename) as f:
            pass
        return True
    except FileNotFoundError:
        sys.exit("File does not exist")

def lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    code = []
    for i in lines:
        if i[0] == '#':
            pass
        elif len(i.lstrip()) > 0 and i.lstrip()[0] == '#':
            pass
        elif i.startswith('\n'):
            pass
        elif len(i.lstrip()) > 1 and i.lstrip().startswith('\n'):
            pass
        elif len(i.lstrip()) == 0:
            pass
        else:
            code.append(i)
    return len(code)


if __name__ == "__main__":
    main()
