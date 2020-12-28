from utils import *
class Affine():

    def __init__(self, alphabet, A=None, B=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado afín.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            A -- El coeficiente A que necesita el cifrado.
            B -- El coeficiente B de desplazamiento.
        """
        try:
            if (A != None and B != None):
                if not (str(A).isnumeric() or str(B).isnumeric()):
                    raise CryptographyException
        except CryptographyException as error:
            print(error.message)
        self.alphabet = alphabet
        self.n = len(alphabet)
        self.A = A or 1
        self.B = B or 0

    def cipher(self, message):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado afín, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        result = ''

        for l in message:
            try:
                i = (self.A * self.alphabet.index(l) + self.B) % self.n
                result += self.alphabet[i]
            except ValueError:
                result += l
        return result


    def decipher(self, criptotext):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el cifrado afín.
        Parámetro:
            criptotext -- el mensaje a descifrar.
        """
        result = ''
        inv = inverse(self.A, self.n)
        for l in criptotext:
            try:
                i = (inv * self.alphabet.index(l) - inv * self.B) % self.n
                result += self.alphabet[i]
            except ValueError:
                result += l
        return result
