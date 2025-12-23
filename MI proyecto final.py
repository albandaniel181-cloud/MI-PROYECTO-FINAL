import random

# Palabras del juego
palabras = [
    "satisfecho", "final", "proyecto",
    "vida", "sueño", "inteligencia", "artificial"
]

# Dibujos del ahorcado según intentos
ahorcado = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

# Selección de palabra
palabra = random.choice(palabras)
letras_adivinadas = set()
intentos = 6

print("     ESTE ES MI PROYECTO FINAL")

print("🎯 BIENVENIDO AL JUEGO DEL AHORCADO 🎯")

print("    ¡¡¡ QUE EMPIECE EL JUEGO !!!    ")

while intentos > 0:
    print(ahorcado[6 - intentos])

    # Mostrar palabra
    palabra_mostrada = " ".join(
        letra if letra in letras_adivinadas else "_"
        for letra in palabra
    )
    print("\nPALABRA:", palabra_mostrada)

    # Mostrar letras usadas
    print("LETRAS QUE VAS USANDO:", " ".join(sorted(letras_adivinadas)))

    # Verificar victoria
    if "_" not in palabra_mostrada:
        print("\n🎉 ¡GANASTE! EL JUEGO DEL AHORCADO RONY ALBAN. LA PALABRA ES: ", palabra)
        break

    # Entrada del usuario
    letra = input("\nINGRESA UNA LETRA: ").lower()

    # Validaciones
    if len(letra) != 1 or not letra.isalpha():
        print("⚠️ INGRESA SOLO UNA LETRA QUE SEA VALIDA")
        continue

    if letra in letras_adivinadas:
        print("⚠️ YA USASTE ESTA LETRA.")
        continue

    letras_adivinadas.add(letra)

    # Comprobar letra
    if letra in palabra:
        print("✔️ CORRECTO.")
    else:
        intentos -= 1
        print("❌ INCORRECTO. TE QUEDAN: ", intentos)

# Si pierde
if intentos == 0:
    print(ahorcado[-1])
    print("\n💀 PERDISTE AMIGO MIO. LA PALABRA ERA: ", palabra)
