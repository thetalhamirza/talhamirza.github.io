from validator_collection import checkers

def main():
    print(validate(input("What is your email address? ")))


def validate(addr):
    valid = checkers.is_email(addr)
    return "Valid" if valid else "Invalid"






if __name__ == "__main__":
    main()
