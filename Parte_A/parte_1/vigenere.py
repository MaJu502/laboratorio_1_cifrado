'''
Universidad del valle de Guatemala
25-01-2024
author: Marco Jurado 20308
Cifrado de información

vigenere.py
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


def cifrar_vigenere(texto, clave):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    texto = no_special_signs(texto.lower())
    clave = no_special_signs(clave.lower())
    result = ''
    clave_index = 0

    for letra in texto:
        if letra in alfabeto:
            desplazamiento = alfabeto.index(clave[clave_index])
            posicion = (alfabeto.index(letra) + desplazamiento) % len(alfabeto)
            result += alfabeto[posicion]

            clave_index = (clave_index + 1) % len(clave)
        else:
            result += letra

    return result

def descifrar_vigenere(texto_cifrado, clave):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    texto_cifrado = texto_cifrado.lower()
    clave = no_special_signs(clave.lower())
    result = ''
    clave_index = 0

    for letra in texto_cifrado:
        if letra in alfabeto:
            desplazamiento = alfabeto.index(clave[clave_index])
            posicion = (alfabeto.index(letra) - desplazamiento) % len(alfabeto)
            result += alfabeto[posicion]

            clave_index = (clave_index + 1) % len(clave)
        else:
            result += letra

    return result

# Ejemplo de uso
clave = "clave"
mensaje = "hola mama me haces hotceiks"
mensaje_cifrado = cifrar_vigenere(mensaje, clave)
mensaje_descifrado = descifrar_vigenere(mensaje_cifrado, clave)

print('Mensaje original:', mensaje)
print('Mensaje cifrado:', mensaje_cifrado)
print('Mensaje descifrado:', mensaje_descifrado)
