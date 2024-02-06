def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    else:
        valid = True
        done = False
        for i in range(len(s)):
            if not(s[i].isalnum()):         #does it contain special characters?
                return False

            if i==0 or i==1:               #check if first 2 chars are letters or not
                if not(s[i].isalpha()):
                    valid = False

            if i in [2,3,4,5]:
                if s[i].isnumeric() and done == False:
                    done = True
                    if s[i] == '0':             #checks if 1st int is 0
                        valid = False
                    if not(s[i:].isnumeric()):           #checks if following chars are int till the end
                        valid = False

        return valid

if __name__ == "__main__":
    main()
