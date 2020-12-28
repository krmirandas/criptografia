import random
import numpy as np
from sympy import Matrix
from math import *


class CryptographyException(Exception):

    def __init__(self):
        self.message = "Invalid key"

    def __str__(self):
        return self.message


def rand(alphabet):
    n = random.randint(4, len(alphabet))
    return ''.join(random.choice(alphabet) for i in range(n))

def randKey(alphabet, n):
    return ''.join(random.choice(alphabet) for i in range(n))

def encrypt(alphabet, plain, key):
    # Convierta caracteres simples y caracteres clave en códigos numéricos
    keyCode = alphabet.index(key)
    plainCode = alphabet.index(plain)

    # Mezcla la tecla + simple y regresa a cero
    cipherCode = (keyCode + plainCode) % len(alphabet)
    # Convierta cipherCode nuevamente en un caracter
    cipher = alphabet[cipherCode]

    return cipher


def invertChar(alphabet, character):

    # Convierte el char en un código numérico
    characterCode = alphabet.index(character)

    # Obtiene el char contrario
    invertedCode = (len(alphabet) - characterCode) % len(alphabet)

    invertedCharacter = alphabet[invertedCode]

    return invertedCharacter


def invert(alphabet, ciphered):

    invertedText = ""

    for character in ciphered:
        invertedText += invertChar(alphabet, character)
    return invertedText


def getPositions(key, alphabet):

    pos_pass = []
    for letter in key:
            pos_pass.append(alphabet.find(letter))
    return pos_pass


def generateMatrix(key, alphabet):

    pos_pass = np.asarray(getPositions(key, alphabet))
    a = pos_pass.reshape(int(sqrt(len(key))), int(sqrt(len(key))))

    return a

def inverse(n, module):

    for x in range(1, module):
        if ((n * x) % module == 1):
            return x
    return False


def dot_matrix(Matrix, alphabet, string):

    pos_pass = np.asarray(getPositions(string, alphabet))
    vector = Matrix.dot(pos_pass) % len(alphabet)
    res = ''
    for i in vector:
        res += alphabet[int(i)]
    return res


def mod_mat_inv(A,module):

    A = Matrix(A)
    A = A.inv_mod(module)
    return np.array(A).astype(np.int32)
