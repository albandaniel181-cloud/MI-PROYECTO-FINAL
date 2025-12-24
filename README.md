# MI-PROYECTO-FINAL

Dentro de mi proyecto final tenemos un juego del ahorcado que en su primera instancia lo realizamos
en el programa RAPTOR, en el se puede visualizar cada una de las funcionalidades:

1️⃣ START (Inicio)
🔴 Función:
Marca el inicio del programa.
🧠 Qué hace: Le indica a RAPTOR dónde empieza a ejecutarse el diagrama.


2️⃣ ASSIGNMENT – PALABRA ← "FINAL"
🔵 Función: Asigna un valor a una variable.
🧠 Qué hace: Guarda la palabra secreta "FINAL" en la variable palabra.
📌 Por qué se usa: El programa necesita saber cuál es la palabra que el usuario debe adivinar.


3️⃣ ASSIGNMENT – INTENTOS ← 1
🔵 Función: Guarda un número en una variable.
🧠 Qué hace: Establece que el usuario tiene 1 intento para adivinar la letra.
📌 Por qué se usa: Permite controlar si el jugador gana o pierde.


4️⃣ OUTPUT – "INGRESE UNA LETRA DEL PROYECTO:"
🟣 Función: Muestra un mensaje en pantalla.
🧠 Qué hace: Le indica al usuario que debe ingresar una letra.
📌 Por qué se usa: Sin este mensaje, el usuario no sabría qué hacer.


5️⃣ INPUT – LETRA
🟢 Función: Recibe datos del usuario.
🧠 Qué hace: Guarda la letra que escribe el usuario en la variable letra.
📌 Por qué se usa: El programa necesita comparar lo que el usuario escribe con la letra correcta.


6️⃣ SELECTION (IF) – LETRA = "F"
🔶 Función: Toma una decisión lógica.
🧠 Qué hace: Compara la letra ingresada con la letra "S".
                 
                 Si SON IGUALES → ruta TRUE

                  Si NO SON IGUALES → ruta FALSE

📌 Por qué se usa: Permite saber si el usuario adivinó correctamente.


7️⃣ OUTPUT – "GANO SU PROYECTO FINAL RONY ALBAN" (Ruta TRUE)
🟣 Función: Muestra un mensaje si la condición es verdadera.
🧠 Qué hace: Indica que el usuario acertó la letra.
📌 Por qué se usa: Es la respuesta del programa cuando el jugador gana.


8️⃣ OUTPUT – "PERDIO SU PROYECTO RONY ALBAN" (Ruta FALSE)
🟣 Función: Muestra un mensaje si la condición es falsa.
🧠 Qué hace: Indica que el usuario no acertó la letra.
📌 Por qué se usa: Es la respuesta del programa cuando el jugador pierde.


9️⃣ END (Fin)
🔴 Función: Marca el final del programa.
🧠 Qué hace: RAPTOR detiene la ejecución del diagrama.

# Mi proyecto final programado con Phyton en Visual Studio Code

El presente trabajo consiste en el desarrollo del juego del Ahorcado utilizando el lenguaje de 
programación Python, en el cual se aplican conceptos fundamentales de programación como la 
declaración y uso de variables, estructuras de control de flujo, bucles repetitivos, condicionales, 
manejo de colecciones de datos y entrada y salida de información. El programa permite la interacción 
directa con el usuario mediante la introducción de letras por teclado, las cuales son evaluadas y 
comparadas con una palabra seleccionada de forma aleatoria, mostrando progresivamente el avance del
juego y controlando la cantidad de intentos disponibles. De esta manera, el sistema es capaz de 
determinar de forma lógica y automática si el jugador ha ganado o perdido, demostrando la correcta 
aplicación de los principios básicos de la programación estructurada y el uso eficiente de Python 
para la resolución de problemas sencillos de manera clara y organizada.

A continuación vamos a explicar su funcionamiento en Visual Studio Code, explicando cada uno
de sus comandos:

1️⃣ import random
🔹 Función: Importa la librería random.
🧠 Qué hace: Permite seleccionar una palabra al azar de una lista.
📌 Por qué se usa: Para que el juego no siempre tenga la misma palabra.

2️⃣ palabras = [...]
🔹 Función: Crea una lista de palabras.
🧠 Qué hace: Almacena todas las posibles palabras del juego.
📌 Por qué se usa: De aquí se selecciona la palabra secreta.

3️⃣ palabra = random.choice(palabras)
🔹 Función: Selecciona una palabra aleatoria.
🧠 Qué hace: Elige una palabra diferente cada vez que se ejecuta el programa.
📌 Por qué se usa: Hace el juego más interesante.

4️⃣ letras_adivinadas = set()
🔹 Función: Crea un conjunto vacío.
🧠 Qué hace: Guarda las letras que el usuario ya ingresó.
📌 Por qué se usa: Evita contar letras repetidas.

5️⃣ intentos = 6
🔹 Función: Define la cantidad de intentos.
🧠 Qué hace: Controla cuántos errores puede cometer el jugador.
📌 Por qué se usa: Para decidir cuándo el jugador pierde.

6️⃣ while intentos > 0:
🔹 Función: Bucle repetitivo.
🧠 Qué hace: El juego se repite mientras el jugador tenga intentos.
📌 Por qué se usa: Permite seguir jugando hasta ganar o perder.

7️⃣ for letra in palabra:
🔹 Función: Recorre la palabra letra por letra.
🧠 Qué hace: Compara cada letra con las letras adivinadas.
📌 Por qué se usa: Para mostrar la palabra con guiones.

8️⃣ Construcción de palabra_mostrada

if letra in letras_adivinadas:
    palabra_mostrada += letra
else:
    palabra_mostrada += "_"

🔹 Función: Decide qué mostrar.
🧠 Qué hace: Muestra la letra si fue adivinada, o un guion si no.
📌 Por qué se usa:Es la base visual del ahorcado.

9️⃣ print("Palabra:", palabra_mostrada)
🔹 Función: Muestra la palabra parcial.
🧠 Qué hace: Informa al jugador su progreso.

🔟 if "_" not in palabra_mostrada:
🔹 Función: Verifica victoria.
🧠 Qué hace: Si no quedan guiones, el jugador ganó.
📌 Por qué se usa: Para terminar el juego correctamente.

1️⃣1️⃣ input("INGRESA UNA LETRA: ")
🔹 Función: Recibe una letra del usuario.
🧠 Qué hace: Permite que el jugador interactúe.

1️⃣2️⃣ .lower()
🔹 Función: Convierte a minúsculas.
🧠 Qué hace: Evita errores por mayúsculas.

1️⃣3️⃣ if intento in letras_adivinadas:
🔹 Función: Evita repetir letras.
🧠 Qué hace: Si la letra ya fue usada, vuelve al inicio del ciclo.

1️⃣4️⃣ letras_adivinadas.add(intento)
🔹 Función: Guarda la letra.
🧠 Qué hace: Añade la letra al conjunto.

1️⃣5️⃣ if intento in palabra:
🔹 Función: Comprueba acierto.
🧠 Qué hace: Verifica si la letra pertenece a la palabra.

1️⃣6️⃣ intentos -= 1
🔹 Función: Resta un intento.
🧠 Qué hace: Penaliza errores.

1️⃣7️⃣ if intentos == 0:
🔹 Función: Verifica derrota.
🧠 Qué hace: Si no hay intentos, el juego termina.


🧩 RESUMEN FINAL

Usa listas para palabras

Usa conjuntos para letras

Usa bucles para repetir

Usa condiciones para decidir

Controla errores y victorias

