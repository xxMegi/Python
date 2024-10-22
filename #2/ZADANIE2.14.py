line = "ab\ncde\txy\nXY"

longest_word = max(line.split(), key=len)
print(longest_word)

longest_word_length = len(longest_word)
print(longest_word_length)