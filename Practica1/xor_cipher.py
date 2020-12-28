def cipher(message):
    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """
    cipher = ""
    for ch in message:
        cipher += chr(ord(ch) ^ 1)
    return cipher

def decipher(criptotext):
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
    message = ""
    for ch in criptotext:
        message += chr(ord(ch) ^ 1)
    return message
