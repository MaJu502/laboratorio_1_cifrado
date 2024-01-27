'''
Universidad del valle de Guatemala
25-01-2024
author: Marco Jurado 20308
Cifrado de información

distribucion.py
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

# USO
texto = "hola mundo como estan hoy el dia de hoy vamos a ver, como se usa la distribucion de la buena araña"
distribucion = calcular_distribucion(texto)

for letra, porcentaje in distribucion.items():
    print(f"{letra}: {porcentaje:.2f}%")

