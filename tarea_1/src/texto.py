import string

dictionario = {}
data = ''
with open("../texto.enc") as fileobj:
    data = fileobj.read()
    # whiteSpaces = ''.join(e for e in data if e.isalpha())
    # print(whiteSpaces)
    for line in data:
       for ch in line:
           if (ch in dictionario):
               dictionario[ch] += 1
           else:
               dictionario[ch] = 0

print(dictionario)

decipher = ''

for e in data:
    if (e == 'R'):
        decipher += 'A'
    elif e == 'G':
        decipher += 'E'
    elif e=='I':
        decipher += 'R'
    elif e=='P':
        decipher += 'H'
    elif e=='K':
        decipher += 'Y'
    elif e=='E':
        decipher += 'Z'
    elif e=='Ñ':
        decipher += 'P'
    elif e=='J':
        decipher += 'O'
    elif e=='H':
        decipher += 'S'
    elif e=='Y':
        decipher += 'U'
    elif e=='O':
        decipher += 'V'
    elif e=='C':
        decipher += 'B'
    elif e=='T':
        decipher += 'C'
    elif e=='A':
        decipher += 'N'
    elif e=='B':
        decipher += 'I'
    elif e=='D':
        decipher += 'M'
    elif e=='N':
        decipher += 'D'
    elif e=='W':
        decipher += 'F'
    elif e=='S':
        decipher += 'G'
    elif e=='Q':
        decipher += 'L'
    elif e=='L':
        decipher += 'T'
    elif e=='M':
        decipher += 'Q'
    elif e=='F':
        decipher += 'K'
    elif e=='X':
        decipher += 'W'
    elif e=='V':
        decipher += 'J'
    else:
        decipher += e

print("---------------------------------------------------------------")
print(decipher)
