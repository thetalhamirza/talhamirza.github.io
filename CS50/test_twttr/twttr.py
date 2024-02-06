def main():
    print(shorten(input("Enter a string: ")))


def shorten(word):
    outer = ''
    for char in word:
        if char.lower() in ['a','e','i','o','u']:
            pass
        else:
            outer = outer + char
    return outer


if __name__ == "__main__":
    main()
