from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        y, m, d = input("Date of Birth: ").split('-')
    except ValueError:
        sys.exit("Invalid Date")
    year, month, day = int(y), int(m), int(d)
    if not verify(year, month, day):
        sys.exit("Invalid Date")

    minutes = minutesLived(year, month, day)
    print(numToWords(minutes))


def verify(year, month, day):
    if (month > 0 and month <= 12) and (day > 0 and day <= 31):
        return True
    else:
        return False



def minutesLived(year, month, day):
    try:
        birth = date(year, month, day)
    except ValueError:
        return 'Invalid Date'
    today = date.today()
    delta = today - birth
    minutes = int(delta.total_seconds() / 60)
    return minutes


def numToWords(minutes):
    return p.number_to_words(minutes, andword='').capitalize() + ' minutes'



if __name__ == "__main__":
    main()
