from utils import *
from random import randint
class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        try:
            if key:
                if not str(key).isnumeric():
                    raise CryptographyException
        except CryptographyException as error:
            print(error.message)
        self.key = key or randint(0, len(alphabet))
        self.alphabet = alphabet
        self.length = len(alphabet)
        print(alphabet)
        self.space = ' ' in alphabet

    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        newString = ''
        if not self.space:
            for c in message:
                if (c in self.alphabet):
                    try:
                        index = self.alphabet.index(c)
                        displacement = (self.key + index) % self.length
                        newString += str(self.alphabet[displacement])
                    except ValueError:
                        print("The message has characters that they dont belong to the alphabet")
                else:
                    if flag:
                        newString += c
                    else:
                        continue
        else:
            for c in message:
                try:
                    print("________________________")
                    index = self.alphabet.index(c)
                    displacement = (self.key + index) % self.length
                    newString += str(self.alphabet[displacement])
                except ValueError:
                    print("The message has characters that they dont belong to the alphabet")

        return newString

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        newString = ''
        if (not self.space):
            for c in criptotext:
                if c in self.alphabet:
                    try:
                        index = self.alphabet.index(c) + 1
                        newString += str(self.alphabet[((index-self.key) % self.length)])
                    except ValueError:
                        print("The message has characters that they dont belong to the alphabet")

                else:
                    if flag:
                        newString += c
                    else:
                        continue
        else:
            for c in criptotext:
                try:
                    index = self.alphabet.index(c)
                    newString += str(self.alphabet[((index-self.key) % self.length)])
                except ValueError:
                    print("The message has characters that they dont belong to the alphabet")

        return newString
