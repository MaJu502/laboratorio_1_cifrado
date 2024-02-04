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

def generar_claves_vigenere(alfabeto, max_longitud):
    from itertools import product
    for clave_longitud in range(1, max_longitud + 1):
        for clave in product(alfabeto, repeat=clave_longitud):
            yield ''.join(clave)

def descifrado_brute_force_vigenere_to_file(texto_cifrado, longitud_clave_estimada, output_file_path, max_line_length):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    texto_cifrado = texto_cifrado.lower()

    with open(output_file_path, 'w') as file_output:
        for clave_longitud in range(longitud_clave_estimada, 2 * longitud_clave_estimada + 1):
            posibles_claves = generar_claves_vigenere(alfabeto, clave_longitud)

            for clave in posibles_claves:
                posible_texto = descifrar_vigenere(texto_cifrado, clave)
                file_output.write(f"Clave: {clave} - Texto descifrado: {posible_texto[:max_line_length]}\n")
                for j in range(max_line_length, len(posible_texto), max_line_length):
                    file_output.write(f"{' ' * 4}{posible_texto[j:j+max_line_length]}\n")
                file_output.write('\n')

output_file_path = 'Parte_B/resultados_vigenere_brute_force.txt'


file_path = 'textos_cifrados/cipher3.txt'
with open(file_path, 'r') as file:
    cipher_text = file.read().lower()

from collections import defaultdict
import itertools
import re

def encontrar_secuencias_repetidas(texto_cifrado, secuencia_tam):
    secuencias = defaultdict(list)
    for i in range(len(texto_cifrado) - secuencia_tam + 1):
        secuencia = texto_cifrado[i:i+secuencia_tam]
        if secuencia.isalpha():
            secuencias[secuencia].append(i)
    return {seq: posiciones for seq, posiciones in secuencias.items() if len(posiciones) > 1}

def calcular_distancias(secuencias_repetidas):
    distancias = defaultdict(list)
    for seq, posiciones in secuencias_repetidas.items():
        for a, b in itertools.combinations(posiciones, 2):
            distancias[seq].append(b - a)
    return distancias

def obtener_factores_comunes(distancias):
    factores = defaultdict(int)
    for distancia in distancias:
        for factor in range(2, distancia//2 + 1):
            if distancia % factor == 0:
                factores[factor] += 1
    return factores

def kasiski_examinacion(texto_cifrado):
    secuencias_repetidas = encontrar_secuencias_repetidas(texto_cifrado, 3)  # 3 es la longitud mínima de la secuencia
    distancias = calcular_distancias(secuencias_repetidas)
    todos_los_factores = []
    for secuencia, ds in distancias.items():
        factores = obtener_factores_comunes(ds)
        todos_los_factores.extend(factores)

    longitud_clave_estimada = max(set(todos_los_factores), key=todos_los_factores.count)
    return longitud_clave_estimada


max_line_length = 80
longitud_clave = kasiski_examinacion(cipher_text)
print('La longitud estimada de la clave es:', longitud_clave)
descifrado_brute_force_vigenere_to_file(cipher_text, longitud_clave, output_file_path, max_line_length)
