import sys

def main():
    try:
        if len(sys.argv) > 3: sys.exit("Too many command-line arguments")
        if len(sys.argv) < 3: sys.exit("Too few command-line arguments")
        filename = sys.argv[1]
        if verify(filename):
            lines = []
            writefile = open(sys.argv[2], 'w')
            with open(filename, 'r') as f:
                for line in f:
                    lines.append(line.replace('"','').replace(' ',''))

                writefile.write('first,last,house\n')
                for i in range(1, len(lines) + 1):
                    last, first, house = lines[i].split(',')
                    writefile.write(f'{first},{last},{house}')
            writefile.close()


    except IndexError:
        pass


def verify(filename):
    if filename[-4:] != '.csv': sys.exit(f"{filename} is not a CSV file")
    try:
        with open(filename) as f:
            pass
        return True
    except FileNotFoundError:
        sys.exit(f"Could not read {filename}")





if __name__ == "__main__":
    main()
