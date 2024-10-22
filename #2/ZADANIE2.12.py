line = "ab\ncde\txy\nXY"

first = ''.join([word[0] for word in line.split()])
print(first)

last = ''.join([word[-1] for word in line.split()])
print(last)