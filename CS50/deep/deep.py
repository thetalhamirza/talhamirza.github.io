choice = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower()
if choice.find('42') != -1 or choice.find('forty two') != -1 or choice.find('forty-two') != -1:
    print('Yes')
else:
    print('No')