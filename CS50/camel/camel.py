camel = input("camelCase: ")
snake = ''

for char in camel:
    if char.isupper() and not char == camel[0]:
        snake = snake + '_' + char.lower()
    elif char.islower() or char == camel[0]:
            snake = snake + char

print('snake_case:', snake)

#haven't included a lot of validation checks here, which can be implemented
#like space as initial char, initial char capital, etc.