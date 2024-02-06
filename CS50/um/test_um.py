from um import count


def test_count_normal():
    assert count("um, hello?") == 1
    assert count("um, um um um um umumumumum") == 5
    assert count("um, um, thats yum yum") == 2
    assert count("UM OkAY UM") == 2

def test_count_abnormal():
    assert count("umm") == 0
    assert count("u") == 0
    assert count("yum") == 0

def test_count_extreme():
    assert count("um, um, um, um, um, um, um, um, um, um") == 10
