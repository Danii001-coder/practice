print('Sistema de calculo')

nombre = input('Cual es tu nombre?: ')
matematicas = int(input(nombre + ' Cual es tu calificacion de matematicas? '))
quimica = int(input(nombre + ' Cual es tu calificacion de quimica '))
biologia = int(input(nombre + ' Cual es tu calificacion de biologia '))

promedio = (matematicas + quimica+ biologia) / 3
promedio = int(promedio)

if promedio >= 6:
  print('Felicidades ' + nombre + ' "Aprobaste" con una media de: ', promedio)

if promedio <= 6:
  print(nombre + ' No aprobaste :(')
print('Fin.')
