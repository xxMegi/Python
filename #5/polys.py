
def add_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    result = [0] * max_len
    for i in range(max_len):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def sub_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    result = [0] * max_len
    for i in range(max_len):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] -= poly2[i]
    return result

def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coef1 in enumerate(poly1):
        for j, coef2 in enumerate(poly2):
            result[i + j] += coef1 * coef2
    return result

def is_zero(poly):
    return all(coef == 0 for coef in poly)

def eq_poly(poly1, poly2):
    return is_zero(sub_poly(poly1, poly2))

def eval_poly(poly, x0):
    result = 0
    for coef in reversed(poly):
        result = result * x0 + coef
    return result

def combine_poly(poly1, poly2):
    result = [0]
    for coef in reversed(poly1):
        result = add_poly(mul_poly(result, poly2), [coef])
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def pow_poly(poly, n):
    result = [1]
    for _ in range(n):
        result = mul_poly(result, poly)
    return result

def diff_poly(poly):
    return [i * poly[i] for i in range(1, len(poly))]