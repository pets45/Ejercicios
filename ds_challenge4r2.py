# Programa que pregunta por 10 colores que pueden ser iguales y los guarda
# y cuenta cuantos colores hay de cada uno


TOTAL_COL = 10
color_can = {}
count = 0

for i in range(TOTAL_COL):
	color = input(f'Ingresa el color {i + 1}: ').lower()
	if color == color:
		count += 1
	color_can[color] = count
print(color_can)
