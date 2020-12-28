from random import randint
from random import randrange
from operator import mul
import functools
import math


def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    number = ''
    if size is None or size < 100:
        size = randrange(100, 150)
    for i in range(size):
        number += str(randint(0, 9))
    return int(number)


def factorial(number):
    '''
    Esta funcíon toma un argumento y
    regresa el factorial de ese numero.
    Esta funcion se basa en que se puede reducir el numero de multiplicaciones a la mitad,
    si es un numero par

    La multiplicacion es una operacion muy pesada, si remplzamos la multiplicacion con la suma,
    reducimos ese costo.

    Por ejemplo: 8!

    8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    8! = (8 * 1) * (7 * 2) * (6 * 3) * (5 * 4)
    8! = 8 * (8 + 6 = 14) * (14 + 4 = 18) * (18 + 2)
    El número impar también sigue el mismo patrón hasta que solo maneja el caso de un número impar
    '''

    if number == 1 or number == 0:
        return 1

    handle_odd = False
    upto_number = number

    if number & 1 == 1:
        upto_number -= 1
        handle_odd = True

    next_sum = upto_number
    next_multi = upto_number
    factorial = 1

    while next_sum >= 2:
        factorial *= next_multi
        next_sum -= 2
        next_multi += next_sum

    if handle_odd:
        factorial *= number

    return factorial


def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(1):
        a = randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    r = factorial(n - 1) + 1
    v = r % n
    if (v == 0):
        print(n, " es es primo")
        return True
    else:
        return False
