import sys
from tabulate import tabulate

def main():
    try:
        if len(sys.argv) > 2: sys.exit("Too many command-line arguments")
        filename = sys.argv[1]
        if verify(filename):
            grid(filename)

    except IndexError:
        sys.exit("Too few command-line arguments")


def verify(filename):
    if filename[-4:] != '.csv': sys.exit("Not a CSV file")
    try:
        with open(filename) as f:
            pass
        return True
    except FileNotFoundError:
        sys.exit("File does not exist")

def grid(filename):
    with open(filename, 'r') as f:
        current = f.readlines()
    table = []
    for item in current:
        row = item.split(',')
        row[2] = row[2][0:-1]
        table.append(row)
    print(tabulate(table, headers = 'firstrow', tablefmt = 'grid'))



if __name__ == "__main__":
    main()
