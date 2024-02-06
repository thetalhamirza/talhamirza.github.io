orig = input('Input: ')
final = ''

for char in orig:
    if char in ('a','e','i','o','u','A','E','I','O','U'):
        continue
    final = final + char

print("Output:", final)