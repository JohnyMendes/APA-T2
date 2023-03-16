"""
Johny Silva Mendes

"""

def esPrimo(numero):
    """
    Devuelve `True` si su argumento es primo, y `False` si no lo es.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2, int(numero**0.5)+1):
        if numero % prueba == 0: return False 

    return True     
def  primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])

def descompon(numero): 

    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    factores = []
    for factor in primos(numero):
        while numero % factor == 0: 
            factores.append(factor)
            numero //= factor
    if numero > 1:
        factores.append(numero)        
    return tuple(factores)


def mcm(numero1, numero2):

    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(36, 30)
    180

    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = []
    for i in factores1:
        if i in factores2:
            factores_comunes.append(i)
            factores2 = list(factores2)
            factores2.remove(i)
            factores2 = tuple(factores2)
    factores_totales = factores_comunes + list(factores1) + list(factores2)
    mcm = 1
    for i in set(factores_totales):
        mcm *= i ** max(factores1.count(i), factores2.count(i))
    return mcm


def mcd(numero1, numero2):

    """

    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(924, 780)
    12
    
    
    """

    factores1 = list(descompon(numero1))
    factores2 = list(descompon(numero2))
    factores_comunes = set(factores1) & set(factores2)
    if not factores_comunes:
        return 1
    else:
        mcd = 1
        for i in factores_comunes:
            mcd *= i ** min(factores1.count(i), factores2.count(i))
        return mcd

import doctest 
doctest.testmod()