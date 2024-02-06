import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        a, b, c, d = ip.split('.')
        a, b, c, d = int(a), int(b), int(c), int(d),
        if a >= 0 and a <= 255:
            if b >= 0 and b <= 255:
                if c >= 0 and c <= 255:
                    if d >= 0 and d <= 255:
                        return True
        return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
