import random


def main():
    total = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        choice = int(input(f"{x} + {y} = "))
        correct = False
        tries = 1
        while not correct and tries < 3:
            if choice == x+y:
                total += 1
                correct = True
            else:
                print("EEE")
                tries += 1
                choice = int(input(f"{x} + {y} = "))
        if correct == False:
            print(f"{x} + {y} =", x+y)
    print("Score:", total)


def get_level():
     while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        current = random.randint(0,9)
    elif level == 2:
        current = random.randint(10,99)
    elif level == 3:
        current = random.randint(100,999)
    else:
        raise ValueError
    return current

if __name__ == "__main__":
    main()
