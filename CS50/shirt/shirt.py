import sys
from os.path import splitext
from PIL import Image, ImageOps



def main():
    verifyArgv()
    imagefile = Image.open(sys.argv[1])
    shirtfile = Image.open("shirt.png")
    muppet = ImageOps.fit(imagefile, shirtfile.size)
    muppet.paste(shirtfile, shirtfile)
    muppet.save(sys.argv[2])






def verifyArgv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    ext1 = splitext(sys.argv[1])[1]
    ext2 = splitext(sys.argv[2])[1]
    if ext1 not in ['.jpg', '.jpeg', '.png']:
        sys.exit("Invalid Input")
    if ext2 not in ['.jpg', '.jpeg', '.png']:
        sys.exit("Invalid Output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    try:
        with open(sys.argv[1],'r') as file:
            pass
    except FileNotFoundError:
        sys.exit("Input does not exist")





if __name__=="__main__":
    main()
