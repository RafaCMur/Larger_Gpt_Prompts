import pyperclip

texto = open('data.txt', encoding='utf-8').read()
texto = ' '.join(texto.split('\n')) # Elimina los saltos de línea
texto = ' '.join(texto.split('\t')) # Elimina los tabuladores

size = 1024 * 16 # 16192 caracteres
conjuntos = []

for i in range(0, len(texto), size):
    conjuntos.append(texto[i:i+size])

while conjuntos:
    data = conjuntos.pop(0)
    pyperclip.copy(data)
    input(data)