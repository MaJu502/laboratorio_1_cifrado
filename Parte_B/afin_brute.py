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

def calcular_distribucion(x):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    frecuencias = dict.fromkeys(alfabeto, 0)
    total_caracteres = 0

    for letra in x.lower():
        if letra in alfabeto:
            frecuencias[letra] += 1
            total_caracteres += 1

    if total_caracteres == 0:
        return {letra: 0 for letra in alfabeto}
    else:
        porcentajes = {letra: (freq / total_caracteres) * 100 for letra, freq in frecuencias.items()}
        return porcentajes

def diferencia_indices_max_probabilidad(distribucion):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

    # Encuentra las dos letras con mayor probabilidad
    letras_max_prob = sorted(distribucion, key=distribucion.get, reverse=True)[:2]

    # Encuentra los índices de esas letras en el alfabeto
    indice_letra1 = alfabeto.index(letras_max_prob[0])
    indice_letra2 = alfabeto.index(letras_max_prob[1])

    # Calcula la diferencia entre los índices
    diferencia = abs(indice_letra1 - indice_letra2)

    return diferencia, letras_max_prob[0], letras_max_prob[1]


def afin_brute_force_con_distribucion(file_path, max_line_length, inicio_a, inicio_b):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    with open(file_path, 'r') as file:
        cipher_text = file.read().lower()

    output_file_path = 'Parte_B/resultados_afin_brute_force_con_distribucion.txt'
    with open(output_file_path, 'w') as output_file:

        for a in range(inicio_a, len(alfabeto)):
            if es_coprimo(a, len(alfabeto)):
                for b in range(inicio_b, len(alfabeto)):
                    try:
                        decrypted_text = afin_descifrar(cipher_text, a, b)
                        output_file.write(f'Con las llaves a={a} y b={b}:\n\n')

                        for j in range(0, len(decrypted_text), max_line_length):
                            output_file.write('    ' + decrypted_text[j:j+max_line_length] + '\n')

                        output_file.write('\n')
                    except ValueError:
                        continue

max_line_length = 80
inicio_a = 23
inicio_b = 7
afin_brute_force_con_distribucion(file_path, max_line_length, inicio_a, inicio_b)


# observacion el brute force con distribucion no sirve del todo bien
