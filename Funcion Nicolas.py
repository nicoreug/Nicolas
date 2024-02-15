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