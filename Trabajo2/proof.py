import hashlib
# Librería para usar SHA-256

import json
# Librería para crear el archivo proof.json

# Leer dataset del .txt
with open("dataset_128.txt", "r", encoding="utf-8") as f:
    # Abre el archivo donde están las 128 palabras
    words = [x.strip() for x in f if x.strip()]
    # Crea una lista con cada palabra
    # strip() elimina espacios y saltos de línea
    # if x.strip() evita líneas vacías

index = 85  # Ultimos numeros de mi DNI

leaf_word = words[index]
# Guarda palabra

def h(b):
    return hashlib.sha256(b).digest()
    # Función que recibe bytes y devuelve el hash SHA-256 en formato binario

# Construir hojas
levels = []
# Lista donde guardaremos todos los niveles del árbol

current = [h(w.encode("utf-8")) for w in words]
# Hashea cada palabra del dataset
# Este es el nivel más bajo (las hojas del árbol)

levels.append(current)
# Guarda el nivel de hojas como primer nivel del árbol

# Construir árbol completo
while len(current) > 1:
    # Mientras haya más de un hash (mientras no lleguemos al root)

    next_level = []
    # Lista para guardar el siguiente nivel del árbol

    for i in range(0, len(current), 2):
        # Recorre los hashes de 2 en 2

        parent = h(current[i] + current[i+1])
        # Concatena hash izquierdo + hash derecho
        # Les aplica SHA-256
        # Ese es el hash del nodo padre

        next_level.append(parent)
        # Guarda el hash padre en el siguiente nivel

    levels.append(next_level)
    # Guarda ese nivel en la lista general

    current = next_level
    # Ahora el nivel actual pasa a ser el siguiente
    # Y el ciclo continúa hasta que quede solo 1 hash (el root)

# Construir proof
proof = []
# Aquí guarda los pasos del Merkle Proof

cur_index = index
# Empezamos en la posición de tu palabra

for level in levels[:-1]:
    # Recorre todos los niveles EXCEPTO el último (el root)

    if cur_index % 2 == 0:
        # Si el índice es par → eres hijo izquierdo

        sibling = level[cur_index + 1]
        # Tu hermano está a la derecha

        proof.append(["SELF", sibling.hex()])
        # SELF va a la izquierda
        # El hash del hermano va a la derecha

    else:
        # Si el índice es impar → eres hijo derecho

        sibling = level[cur_index - 1]
        # Tu hermano está a la izquierda

        proof.append([sibling.hex(), "SELF"])
        # El hash del hermano va a la izquierda
        # SELF va a la derecha

    cur_index //= 2
    # Subimos un nivel en el árbol
    # División entera por 2 para encontrar la nueva posición

# Crear json
output = {
    "leaf": leaf_word,
    # La palabra exacta del dataset

    "path": proof
    # La lista con los 7 pasos del proof
}

with open("proof.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
    # Crea el archivo proof.json con formato bonito

print("proof.json generado")
# Mensaje para confirmar que el archivo se creó
