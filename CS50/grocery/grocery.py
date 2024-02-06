
grocery = {}

while True:
    try:
        current = input().upper()
        if current not in grocery:
            grocery[current] = 1
        else:
            grocery[current] = grocery[current] + 1
    except EOFError:
        print()
        for item in sorted(grocery):
            print(grocery[item], item)
        break
