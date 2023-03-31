f = open('datos.txt', 'w')
lista = [
    'Pedro',
    'Manolo',
    'Paco'
]

for linea in lista:
    linea= linea + '\n'

    f.write(linea)

f.close()

g = open('datos.txt', 'a')

lista2 = [
    'Josefa',
    'Paquita',
    'Lola'
]

for linea in lista2:
    if not linea.endswith('/r'):
        linea = linea + '\n'
        g.write(linea)

g.close()


