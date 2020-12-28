import string
from random import randint

CRED = '\033[91m'
CEND = '\033[0m'
CBLUE = '\33[34m'
CYEL = '\033[93m'
CREDBG    = '\33[41m'

alphabet = {
0:'a',
1:'b',
2:'c',
3:'d',
4:'e',
5:'f',
6: 'g',
7:'h',
8:'i',
9:'j',
10:'k',
11:'l',
12:'m',
13:'n',
14:'o',
15:'p',
16:'q',
17:'r',
18:'s',
19:'t',
20:'u',
21:'v',
22:'w',
23:'x',
24:'y',
25:'z'
}

stringToNumber = {
'a': 0,
'b': 1,
'c': 2,
'd':3,
'e':4,
'f':5,
'g':6,
'h':7,
'i':8,
'j':9,
'k':10,
'l':11,
'm':12,
'n':13,
'o':14,
'p':15,
'q':16,
'r':17,
's':18,
't':19,
'u':20,
'v':21,
'w':22,
'x':23,
'y':24,
'z':25
}

'''
To do so with python you need the ord,
isalpha and chr methods
and as an argument
you pass a character or a number.

This method is a mapping to alphabet object
'''
def cesarWithAlpabhet(number,string):
    newString = ''
    for c in string:
        map = stringToNumber[c]
        newString += str(alphabet[(map-number) % 26])
    return newString

def main(s):
    counter = 0
    whiteSpaces = s.translate(None,string.whitespace)
    displacement = randint(0, 25)
    newString = ''
    for c in whiteSpaces:
        map = stringToNumber[c]
        algo = (displacement + map) % 26
        newString += str(alphabet[algo])

    while(True):
        print(CRED + '________________________________' + CEND)
        print(CRED + 'Cadena Cifrada:  ' + CEND + newString)
        try:
            number = int(raw_input(CYEL+'Desplazamiento:  '+ CEND))
            print(CBLUE + "Posible respuesta:  " + CEND + cesarWithAlpabhet(number,newString ))
            print(CRED + '________________________________' + CEND)
        except ValueError:
            print(CREDBG + 'Ingresa un numero valido, por favor' + CEND)
            continue
        counter +=1
        if(counter > 26):
            print(displacement)
            break

#string1 = 'SLYDPYQCGLQNGPYBMPY'.lower() #unafraseinspiradora
#main(string1)

string2 = 'CVVCEMVJGKORNGOGPVCVKQP'.lower() #unafraseinspiradora
main(string2)
