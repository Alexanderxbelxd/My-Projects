#juego Del Ahorcado 
#@AlexanderEsquivel
"""
Explicacion
1. Elegir aleatoriamente una palabra
de una lista de palabras.
2. Mostrar el dibujo de una horca.
3. Mostrar un guion bajo por cada letra 
de la palabra.
4. Pedir al usuario que introduzca una letra 
letra: si no es una unica letra indicarlo.
Y si ya se ha dicho indicarlo.
5. Comprobar si esa letra esta contenida en la palabra
elegida.
6. Si esta: volver a mostrar el dibujo de la horca como la ultima vez.
Sustituir el guion correspondiente por la letra dicha.
7. Si no esta: Mostrar el dibujo de la horca al que se añade una parte.
8. Si se falla 6 veces: se completa el dibujo del ahorcado.
9. Si se acierta todas las letras de la palabra: Gano!
"""
import random 
import os

palabras = ["Colombia", "Ecuador", "Venezuela", "Brasil",
          "Argentina", "chile" , "Peru", "Paraguay",
          "Uruguay", "Bolivia"]
palabra = random.choice(palabras)

fallo0 = """
          !===N
              N
              N
              N
      =========
"""
fallo1 = """
          !===N
          0   N
              N
              N
      =========
"""
fallo2 = """
          !===N
          _0  N
              N
              N
      =========
"""
fallo3 = """
          !===N
          _0_ N
              N
              N
      =========
"""
fallo4 = """
          !===N
          _0_ N
           |  N
              N
      =========
"""
fallo5 = """
          !===N
          _0_ N
           |  N
          /   N
      =========
"""
fallo6 = """
          !===N
          _0_ N
           |  N
          / \ N
      =========
"""
letras_correctas = "" #letras correctas dichas por el usuario
letras_todas = "" #Todas las letras dichas por el usuario
fallos = 0

while True: 
  os.system("cls")
  print("--------------------")
  print("--Juego Del Ahorcado--")
  print("--------------------")
  if fallos == 0: 
    print(fallo0)
  elif fallos == 1:
    print(fallo1)
  elif fallos ==2:
    print(fallo2)
  elif fallos == 3:
    print(fallo3)
  elif fallos == 4:
    print(fallo4)
  elif fallos == 5:
    print(fallo5)
  elif fallos ==6: 
    print(fallo6)

    print()

    #Mostramos las letras acertadas y guiones bajos en las no acertadas 

    resultado = ""

    for letra in palabra: 
      if letra in letras_correctas:
        resultado += letra 
      else:
        resultado += "_"
    print("       {}".format(resultado))
    print()
    print()

      #Comprobamos si se ha acertado la palabra, o se han terminados los intentos.

    if resultado==palabra:
      print("*** Has Ganado ***")
      break 
    if fallos>5:
      print(" La palabra es: " , palabra )
      print("*** Has perdido ***")
      break

       #Bucle para que el usuario teclee una letra que cumpla los requisitos
  while True:
    letra_usuario_sin_formato =input ("Dime Una Letra:")
    letra_usuario=letra_usuario_sin_formato.upper()
    if len(letra_usuario)<1 or len(letra_usuario)>1:
      print("Introduce Una Letra")
    elif letra_usuario in letras_todas:
      print("Esa Letra Ya la Has Mencionado")
    elif not letra_usuario.isalpha():
      print("Introduce Una Letra")
    else: 
      letras_todas+=letra_usuario
      break 

      #comprobamos si la letra dicah por el usuario esta en la palabra
  if letra_usuario not in palabra:
    fallos+=1
  else:
    letras_correctas+=letra_usuario
    
            

      

