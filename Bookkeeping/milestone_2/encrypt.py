key = int(input('Enter your key: '))
message = input('Enter your message: ')
result = ''

for char in message:
    if char.isalpha():
        code = ord(char)
        if char.isupper():
            code = (code - key - 65) % 26 + 65
        else:
            code = (code - key - 97) % 26 + 97
        result += chr(code)
    else:
        result += char

print('Result: ', result)


def is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
