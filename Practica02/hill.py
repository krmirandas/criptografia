from utils import *
from sympy import *
import numpy as np
import math
import string


class Hill():

    def __init__(self, alphabet, n, key=None):
        """
        Constructor de clase, recibiendo un alfabeto completamente necesario pero
        podría no recibir una llave de cifrado, en cuyo caso, hay que generar una,
        para el caso del tamañHo de la llave, hay que asegurarse que tiene raíz entera.
        :param alphabet: una cadena con todos los elementos del alfabeto.
        :param n: el tamaño de la llave, obligatorio siempre.
        :param key: una cadena que corresponde a la llave, en caso de ser una llave inválida
        arrojar una CryptographyException.
        """
        self.alphabet = alphabet

        root = math.sqrt(n)
        if not int(root + 0.5) ** 2 == n:
            raise CryptographyException
        else:
            self.n = n
        if key is not None:
            if inverse(round(np.linalg.det(generateMatrix(key, alphabet)) % len(self.alphabet)), len(alphabet)):
                self.key = key
            else:
                raise CryptographyException
        else:
            key = randKey(alphabet,n)
            while not inverse(round(np.linalg.det(generateMatrix(key, alphabet)) % len(self.alphabet)), len(alphabet)):
                key = randKey(alphabet,n)
            self.key = key

    def cipher(self, message):
        """
        Aplica el algoritmo de cifrado con respecto al criptosistema de Hill, el cual recordando
        que todas las operaciones son mod |alphabet|.
        :param message: El mensaje a enviar que debe ser cifrado.
        :return: Un criptotexto correspondiente al mensaje, este debe de estar en representación de
        cadena, no lista.
        """
        message = message.translate({ord(c): None for c in string.whitespace})
        cipher = ''
        seg = ''
        matrix = generateMatrix(self.key, self.alphabet)
        for i in range(0, len(message), int(sqrt(self.n))):
            seg += message[i:i + int(sqrt(self.n))]
            if len(seg) != int(sqrt(self.n)):
                seg += 'A'
            cipher += dot_matrix(matrix, self.alphabet, seg)
            seg = ''
        return cipher

    def decipher(self, ciphered):
        """
        Usando el algoritmo de decifrado, recibiendo una cadena que se asegura que fue cifrada
        previamente con el algoritmo de Hill, obtiene el texto plano correspondiente.
        :param ciphered: El criptotexto de algún mensaje posible.
        :return: El texto plano correspondiente a manera de cadena.
        """
        message = ''
        seg = ''
        matrix = generateMatrix(self.key, self.alphabet)
        mat_inv = mod_mat_inv(matrix, len(self.alphabet))
        for i in range(0, len(ciphered), int(sqrt(self.n))):
            seg += ciphered[i:i + int(sqrt(self.n))]
            message += dot_matrix(mat_inv, self.alphabet, seg)
            seg = ''
        return message
