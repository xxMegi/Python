seq = [[],[4],(1,2),[3,4],(5,6,7)]

def suma(seq):
    return [sum(seq) for seq in seq]

print("Suma liczb w sekwencjach:", suma(seq))
