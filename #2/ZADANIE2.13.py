line = "ab\ncde\txy\nXY"

quantity = sum(len(word) for word in line.split())
print(quantity)