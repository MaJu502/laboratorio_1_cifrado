'''
Universidad del valle de Guatemala
01-02-2024
author: Marco Jurado 20308
Cifrado de información

cesar_brute.py
'''

file_path = 'textos_cifrados/cipher1.txt'
with open(file_path, 'r') as file:
    cipher_text = file.read().lower()


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

def bruteForce_cesar_to_file(text, max_line_length):
    output_file_path = 'Parte_B/resultados_cesar_brute_force.txt'
    with open(output_file_path, 'w') as output_file:
        for i in range(28):
            decrypted_text = simple_ceaser_decrypt(text, i)
            output_file.write('Con la llave ' + str(i) + ':\n\n')

            for j in range(0, len(decrypted_text), max_line_length):
                output_file.write('    ' + decrypted_text[j:j+max_line_length] + '\n')

            output_file.write('\n')  # Espacio extra entre cada resultado

# Supongamos que quieres un salto de línea cada 80 caracteres
max_line_length = 80
bruteForce_cesar_to_file(cipher_text, max_line_length)