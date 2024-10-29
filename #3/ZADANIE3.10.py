def roman2int(roman):
    roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_to_arabic[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total


print("XIX =", roman2int("XIX"))
print("MXXIV =", roman2int("MXXIV"))

#inny sposób słownik
#roman_to_arabic = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
