import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s.strip())
    if matches:
        #Error handling
        if matches.group(1):
            if int(matches.group(1)) < 1 or int(matches.group(1)) > 12:
                raise ValueError
        if matches.group(4):
            if int(matches.group(4)) < 1 or int(matches.group(4)) > 12:
                raise ValueError
        if matches.group(2):
            if int(matches.group(2)) >= 60 or int(matches.group(2)) < 0:
                raise ValueError
        if matches.group(5):
            if int(matches.group(5)) >= 60 or int(matches.group(5)) < 0:
                raise ValueError


        # hour1
        hour1 = int(matches.group(1))
        if matches.group(3) == "PM" and hour1 != 12:
            hour1 += 12
        elif matches.group(3) == "AM" and hour1 == 12:
            hour1 -= 12
        if matches.group(2) == None:
            startTime = f"{hour1:02}:00"
        else:
            startTime = f"{hour1:02}:{matches.group(2)}"


        # hour2
        hour2 = int(matches.group(4))
        if matches.group(6) == "PM" and hour2 != 12:
            hour2 += 12
        elif matches.group(6) == "AM" and hour2 == 12:
            hour2 -= 12
        if matches.group(5) == None:
            endTime = f"{hour2:02}:00"
        else:
            endTime = f"{hour2:02}:{matches.group(5)}"


        # 24-hour format
        time = f"{startTime} to {endTime}"
        return time
    else:
        raise ValueError



if __name__ == "__main__":
    main()
