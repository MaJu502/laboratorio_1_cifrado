'''
Universidad del valle de Guatemala
01-02-2024
author: Marco Jurado 20308
Cifrado de información

afin_brute.py
'''
import math

file_path = 'textos_cifrados/cipher2.txt'
with open(file_path, 'r') as file:
    cipher_text = file.read().lower()

def inverso_multiplicativo(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

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

def es_coprimo(a, b):
    return math.gcd(a, b) == 1

def bruteForce_afin_to_file(text, max_line_length):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    output_file_path = 'Parte_B/resultados_afin_brute_force.txt'
    with open(output_file_path, 'w') as output_file:
        for a in range(len(alfabeto)):
            if es_coprimo(a, len(alfabeto)):  # a debe ser coprimo con la longitud del alfabeto
                for b in range(len(alfabeto)):
                    try:
                        decrypted_text = afin_descifrar(text, a, b)
                        output_file.write('Con las llaves a=' + str(a) + ' y b=' + str(b) + ':\n\n')

                        for j in range(0, len(decrypted_text), max_line_length):
                            output_file.write('    ' + decrypted_text[j:j+max_line_length] + '\n')

                        output_file.write('\n')  # Espacio extra entre cada resultado
                    except ValueError as e:
                        # Si no hay inverso multiplicativo, simplemente continuamos con el siguiente b
                        continue

# Supongamos que quieres un salto de línea cada 80 caracteres
max_line_length = 80
bruteForce_afin_to_file(cipher_text, max_line_length)
