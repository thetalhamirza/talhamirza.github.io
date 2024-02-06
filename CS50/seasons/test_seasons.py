from seasons import verify, minutesLived, numToWords

def main():
    ...


def test_verify():
    assert verify(2000, 21, 50) == False
    assert verify(2000, 12, 31) == True


def test_numToWords():
    assert numToWords(1440) == "One thousand, four hundred forty minutes"
    assert numToWords(2190) == "Two thousand, one hundred ninety minutes"








if __name__ == "__main__":
    main()
