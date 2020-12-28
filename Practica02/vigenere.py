from utils import rand, encrypt, invert
import itertools


class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        self.password = password if not password == None else rand(alphabet)

    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        cipher = ''
        for (textIndex, textChar) in enumerate(message):
            # el índice de nuestro char para obtener el char clave correspondiente
            passIndex = textIndex % len(self.password)
            passChar = self.password[passIndex]

            # Cifra un char con char clave
            cipherCharacter = encrypt(self.alphabet,textChar, passChar)

            cipher += cipherCharacter

        return cipher


    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """

        invertPass = invert(self.alphabet, self.password)
        decipher = ''

        for (textIndex, textChar) in enumerate(ciphered):
            # el índice de nuestro char para obtener el char clave correspondiente
            passIndex = textIndex % len(invertPass)
            passChar = invertPass[passIndex]

            # Cifra un char con char clave
            decipherCharacter = encrypt(self.alphabet,textChar, passChar)

            decipher += decipherCharacter

        return decipher
