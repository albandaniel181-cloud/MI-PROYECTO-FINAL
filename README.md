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


