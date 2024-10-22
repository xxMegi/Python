line = "ab\ncde\txy\nXY"

sorted_alphabetically = sorted(line.split())
print(sorted_alphabetically)

sorted_by_length = sorted(line.split(), key=len)
print(sorted_by_length)