import math

def leastCommonMultiple(a, b):
    return (a * b) / math.gcd(a, b)

def add_frac(frac1, frac2): #suma
    denominator = leastCommonMultiple(frac1[1], frac2[1])
    counter = frac1[0] * (denominator / frac1[1]) + frac2[0] * (denominator / frac2[1])
    return [counter, denominator]

def sub_frac(frac1, frac2): #różnica
    denominator = leastCommonMultiple(frac1[1], frac2[1])
    counter = frac1[0] * (denominator / frac1[1]) - frac2[0] * (denominator / frac2[1])
    return [counter, denominator]

def mul_frac(frac1, frac2): #iloczyn
    counter = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    gcd = math.gcd(counter, denominator)
    return [counter / gcd, denominator / gcd]

def div_frac(frac1, frac2): #iloraz
    return mul_frac(frac1, frac2[::-1])

def is_positive(frac): #dodatni: True czy False
    return frac[0] * frac[1] > 0

def is_zero(frac): # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2): # -1 | 0 | +1
    denominator = leastCommonMultiple(frac1[1], frac2[1])
    counter1 = frac1[0] * (denominator / frac1[1])
    counter2 = frac2[0] * (denominator / frac2[1])

    if counter1 > counter2: return 1
    elif counter2 > counter1: return -1
    else: return 0

def frac2float(frac): #konwersja do float
    return float(frac[0] / frac[1])
