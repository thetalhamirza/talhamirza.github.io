from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
...
try:
    if len(sys.argv) > 1:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            figlet.setFont(font = sys.argv[2])
        else:
            sys.exit("Unidentifiable argument")

    elif len(sys.argv) == 1:
        fontlist = figlet.getFonts()
        fontlen = len(fontlist)
        random = random.randint(0, fontlen)
        figlet.setFont(font = fontlist[random])

    else:
        sys.exit("Too many arguments")

except IndexError:
    sys.exit("Too few arguments")

...

inner = input("Input: ")

print("Output:", figlet.renderText(inner))
