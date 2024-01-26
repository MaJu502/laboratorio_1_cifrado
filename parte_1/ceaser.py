'''
Universidad del valle de Guatemala
25-01-2024
author: Marco Jurado 20308
Cifrado de información

ceaser.py
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

'''
x (str): String to be encrypted.
y (int): Integer of the displacement applied for encryption.

Returns: encrypted message.
'''
def simple_ceaser_encrypt(x,y):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    x = no_special_signs(x.lower())
    result = ''

    for letra in x:
        if letra in alfabeto:
            posicion = (alfabeto.index(letra) + y) % len(alfabeto)
            result = result + alfabeto[posicion]

        else:
            result = result + letra

    return result

'''
x (str): String to be decrypted.
y (int): Integer of the displacement applied for encryption.

Returns: decrypted message.
'''
def simple_ceaser_decrypt(x, y):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    x = x.lower()
    result = ''

    for letra in x:
        if letra in alfabeto:
            posicion = (alfabeto.index(letra) - y) % len(alfabeto)
            result = result + alfabeto[posicion]
        else:
            result = result + letra

    return result

# Casos de uso para entrega
mensaje = 'hola mundo como estan zebra'
desplazamiento = 3
cifrado = simple_ceaser_encrypt(mensaje, desplazamiento)
print('mensaje original: ', mensaje)
print('desplazamiento: ', desplazamiento)
print('\nmensaje cifrado: ', cifrado)
print('\nmensaje descifrado: ', simple_ceaser_decrypt(cifrado, desplazamiento))