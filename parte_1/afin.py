'''
Universidad del valle de Guatemala
25-01-2024
author: Marco Jurado 20308
Cifrado de información

afin.py
'''


'''
x (str): String to check and remove for special characters.

Returns: clean string with no special characters.
'''
def no_special_signs(x):
    special_signs = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ü': 'u', 'Ü': 'U'
    }

    return ''.join(special_signs.get(letra, letra) for letra in x)


def inverso_multiplicativo(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

def afin_cifrar(x, a, b):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    x = no_special_signs(x.lower())
    result = ''

    for letra in x:
        if letra in alfabeto:
            posicion = (alfabeto.index(letra) * a + b) % len(alfabeto)
            result += alfabeto[posicion]
        else:
            result += letra

    return result

def afin_descifrar(x, a, b):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    x = x.lower()
    result = ''

    a_inv = inverso_multiplicativo(a, len(alfabeto))
    if a_inv is None:
        raise ValueError("No existe inverso multiplicativo para 'a' en modulo longitud del alfabeto.")

    for letra in x:
        if letra in alfabeto:
            posicion = (a_inv * (alfabeto.index(letra) - b)) % len(alfabeto)
            result += alfabeto[posicion]
        else:
            result += letra

    return result

# Ejemplo de uso
a = 5  # Clave para multiplicación, debe ser coprimo con la longitud del alfabeto
b = 8  # Clave para desplazamiento
mensaje = 'hola mundo como estan zebra'
mensaje_cifrado = afin_cifrar(mensaje, a, b)
mensaje_descifrado = afin_descifrar(mensaje_cifrado, a, b)

print('mensaje original: ', mensaje)
print('mensaje cifrado: ', mensaje_cifrado)
print('mensaje descifrado: ', mensaje_descifrado)
