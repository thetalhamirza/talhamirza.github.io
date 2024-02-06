import random


while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level > 0:
        break

secret = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess > 0:
        if guess == secret:
            print("Just right!")
            break
        elif guess > secret:
            print("Too large!")
        elif guess < secret:
            print("Too small!")
    else:
        continue

...

