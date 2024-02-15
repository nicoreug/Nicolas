def hablar():
    # esta funcion sirve para communicarse con el robot
    hab1 = print("Que quieres que diga el robot?")
    print("Pulse Q para que diga HOLA, W para que diga ADIOS y E para que diga QUE TAL. ")
    hola = input()
    if hola == "Q" or hola == "q":
        print("Hola soy el robot")
    if hola == "W" or hola == "w":
        print("Adios humano")
    if hola == "E" or hola == "e":
        print("Que tal estas?")
    Conversacion = input()

#Esta función calcula operaciones
def calculadora():
    contador = 1
    while contador==1:
        print("Bienvenido a la calculadora")
        print("Si desea sumar ponga 1, si desea restar ponga 2, si desea multiplicar ponga 3 y si desea dividir ponga 4")
        operacion = int(input())
        print("Ahora pon los numeros que desea clacular")
        primero = int(input())
        segundo = int(input())
        if operacion == 1:
            print(primero + segundo)
        elif operacion == 2:
            print(primero - segundo)
        elif operacion == 3:
            print(primero * segundo)
        elif operacion == 4:
            print(primero/segundo)
        print("Si quieres volver a calcular pon 1 y si quieres salir pon 0")
        contador = int(input())
    print("ADIOS")

#Esta función reproduce música 
def musica():
 print("¿Que canción desea escuchar?")
 musica= input()
 print("reproduciendo", musica)
 contador = 1
 while contador == 1:    
    print("¿Desea cambiar la canción?")
    print("Pulse 1 cambiar o 0 para dejar")
    contador = int(input())
    if contador == 1:
      print("Indique la canción")
      cancion = input()

#Esta función activa el movimiento del robot hacia adelante y hacia atrás
def movimiento():
    adelante = 1
    atrás = 2
    contador = 1
    while(contador == 1):
     print("Si desea que el robot vaya para adelante, pulse 1, si desea que vaya para atrás, pulse 2")
     respuesta = int(input())
     if respuesta == 1:
      print("El robot está avanzando correctamente")
      print("Si desea volver a interactuar con el robot pulse 1 sino pulse 0")
      decisión = int(input())
      if decisión == 0:
        print("Se ha cerrado correctamente")
     if respuesta == 2:
      print("El robot está retrocediendo correctamente")
      print("Si desea volver a interactuar con el robot pulse 1 sino pulse 0")
      decisión = int(input())
      if decisión == 0:
       print("Se ha cerrado correctamente")
        