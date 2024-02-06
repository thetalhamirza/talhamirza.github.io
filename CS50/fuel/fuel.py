while True:
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split('/')
        x,y = int(x),int(y)
        if x > y:
            raise ValueError
        percent = round(x/y * 100)
        if percent <= 1:
            print("E")
        elif percent >=99:
            print("F")
        else:
            print(f"{percent}%")
        break
    except (ZeroDivisionError, ValueError):
        pass