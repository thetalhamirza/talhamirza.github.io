def main():
    InString = input()
    return convert(InString)

def convert(textin):

    if ':)' in textin:
        if ':(' in textin:
            final = textin.replace(':)', '🙂')
            final2 = final.replace(':(', '🙁')
            print(final2)
        else:
            print(textin.replace(':)', '🙂'))
    elif ':(' in textin:
        print(textin.replace(':(', '🙁'))







if __name__ == "__main__":
    main()