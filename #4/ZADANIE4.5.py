L = [1, 2, 3, 4, 5, 6]
def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

#ITERACYJNIE
odwracanie(L, 1, 4)
expected_L = [1, 5, 4, 3, 2, 6]
assert L == expected_L


L2 = [1, 2, 3, 4, 5, 6]
def odwracanie2(L2, left, right):
    if left < right:
        L2[left], L2[right] = L2[right], L2[left]
        odwracanie2(L2, left + 1, right - 1)

#REKURENCYJNIE:
odwracanie2(L2, 1, 4)
expected_L2 = [1, 5, 4, 3, 2, 6]
assert L2 == expected_L2