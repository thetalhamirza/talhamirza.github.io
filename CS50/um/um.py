import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    value = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(value)



if __name__ == "__main__":
    main()
