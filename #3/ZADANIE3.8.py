seq1 = [0,1,2,3]
seq2 = [6,5,4,3]

def wspolne(seq1, seq2):
    return list(set(seq1) & set(seq2))

def wszystkie(seq1, seq2):
    return list(set(seq1) | set(seq2))

print("Wspólne elementy:", wspolne(seq1, seq2))
print("Wszystkie elementy:", wszystkie(seq1, seq2))