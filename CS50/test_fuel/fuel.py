def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    x,y = fraction.split('/')
    x,y = int(x), int(y)
    if y == 0: raise ZeroDivisionError
    if x > y: raise ValueError
    percent = int(x / y * 100)
    return percent

def gauge(percent):
    if percent >= 99:
        return 'F'
    elif percent <= 1:
        return 'E'
    else:
        return f'{percent}%'

if __name__ == "__main__":
    main()


