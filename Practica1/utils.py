class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message

def prime_relative(a, b):
    if b == 0:
        return a == 1
    else:
        return prime_relative(b, a % b)

'''
Se usa el maximo comun divisor
La idea principal es encontrar 'x' y 'n'
tal que ax + ny = mcd(a,n). Como a y n son
primos relativos =>
ax + ny = 1 =>
ax + ny = 1 (mod n) =>
ax = 1 (mod n)
'''
def inverse(a,m):
    m0 = m
    y = 0
    x = 1

    if (m == 1) :
        return 0

    while (a > 1) :
        q = a // m #cociente
        t = m
        m = a % m #residuo
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0) : #positivo
        x = x + m0
    return x
