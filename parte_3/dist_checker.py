'''
Universidad del valle de Guatemala
25-01-2024
author: Marco Jurado 20308
Cifrado de información

dist_checker.py
'''

'''
x (str): String to check the distribution in.

Returns: probs for each letter of the language.
'''
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

probabilidades_definidas = {
    'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69,
    'g': 1.01, 'h': 0.70, 'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97,
    'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68, 'p': 2.51, 'q': 0.88,
    'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.01,
    'x': 0.22, 'y': 0.90, 'z': 0.52
}
# USO
texto = "hola mundo como estan hoy el dia de hoy vamos a ver, como se usa la distribucion de la buena araña"
texto_cifrado = ""
distribucion = calcular_distribucion(texto)

def encontrar_mas_cercano(distribucion_texto, probabilidades_imagen):
    resultado_comparacion = {}
    for letra_texto, probabilidad_texto in distribucion_texto.items():
        letra_cercana = min(probabilidades_imagen.keys(), key=lambda x: abs(probabilidad_texto - probabilidades_imagen[x]))
        resultado_comparacion[letra_texto] = letra_cercana
    return resultado_comparacion

comparacion = encontrar_mas_cercano(distribucion, probabilidades_definidas)

for letra, letra_cercana in comparacion.items():
    print(f"La letra '{letra}' del texto esta cerca en probabilidad a la letra '{letra_cercana}' de la imagen.")


def sustituir_por_cercania(texto_cifrado, comparacion):
    texto_descifrado = ''
    for letra in texto_cifrado:
        if letra in comparacion:
            texto_descifrado += comparacion[letra]
        else:
            texto_descifrado += letra
    return texto_descifrado

texto_descifrado_por_cercania = sustituir_por_cercania(texto_cifrado, comparacion)

print('Texto cifrado:', texto_cifrado)
print('Texto descifrado por cercanía:', texto_descifrado_por_cercania)
