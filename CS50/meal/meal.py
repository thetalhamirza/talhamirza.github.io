def main():
    # choice = input("12-hour clock?")
    tfloat = convert(input('What time is it? '))
    if tfloat >= 7 and tfloat <= 8:
        print('breakfast time')
    elif tfloat >= 12 and tfloat <= 13:
        print('lunch time')
    elif tfloat >= 18 and tfloat <= 19:
        print('dinner time')


def convert(time):
    hours, minutes = time.split(':')
    final = int(hours) + (int(minutes)/60)
    return float(final)



if __name__ == "__main__":
    main()