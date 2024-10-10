def simple_reverse(string = None):
    if not(isinstance(string, str)):
        return 'Invalid Input'
    elif len(string) < 2:
        return string
    else:
        new_str = []
        for i in range(len(string)-1, -1, -1):
            new_str.append(string[i])
        return "".join(new_str)

s = 'hello'
print(simple_reverse(s))
print(s[::-1])
print(''.join(reversed(s)))

print(simple_reverse(0))
print(simple_reverse('h'))
print(simple_reverse())

