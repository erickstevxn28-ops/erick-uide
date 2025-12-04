# -------------------------------------------
# JUEGO DEL AHORCADO - AVANCE DE DESARROLLO
# Autor: [Tu nombre]
# -------------------------------------------

# Lista de palabras disponibles
palabra = "PYTHON" 

# Convertimos la palabra en una lista de letras
palabra_lista = list(palabra)

# Crear la palabra oculta con guiones
progreso = ["_" for _ in palabra_lista]

# Letras que ya intentó el usuario
letras_usadas = []

# Variable para controlar el juego
juego_activo = True

print("=== JUEGO DEL AHORCADO (AVANCE) ===")
print("Palabra oculta:")
print(" ".join(progreso))   # Mostrar guiones al inicio

# Bucle principal del juego (estructura repetitiva)
while juego_activo:

    letra = input("\nIngresa una letra: ").upper()

    # Validación (estructura lógica)
    if len(letra) != 1 or not letra.isalpha():
        print("⚠ Debes ingresar solo UNA letra válida.")
        continue

    # Verificamos si la letra ya fue usada
    if letra in letras_usadas:
        print("⚠ Ya ingresaste esa letra antes.")
        continue

    letras_usadas.append(letra)

    # Verificar si la letra está dentro de la palabra
    if letra in palabra_lista:
        print(f"✔ ¡Correcto! La letra '{letra}' está en la palabra.")

        # Usamos un bucle FOR para reemplazar en los guiones
        for i in range(len(palabra_lista)):
            if palabra_lista[i] == letra:
                progreso[i] = letra
    else:
        print(f"✖ La letra '{letra}' NO está en la palabra.")

    # Mostrar el progreso actualizado
    print("\nProgreso actual:")
    print(" ".join(progreso))

    # Verificar si ya se completó la palabra
    if "_" not in progreso:
        print("\n ¡Felicidades! Completaste la palabra.")
        juego_activo = False
