def main():
    print("$" + str(value(input("Greeting: "))))


def value(inner):
    greet = inner.lower().strip()
    if greet[0:5] == 'hello':
        return 0
    elif greet[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

