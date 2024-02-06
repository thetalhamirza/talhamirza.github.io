names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

current = ''

for i in range(len(names) - 1):
    current = current + ", " + names[i]

outer = current[2:]

if len(names) > 2:
    final = outer + ", and " + names[-1]
elif len(names) == 2:
    final = names[-2] + ' and ' + names[-1]
else:
    final = names[-1]


print()
print("Adieu, adieu, to " + final)
