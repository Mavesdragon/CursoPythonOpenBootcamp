class Alumno:

    def isAbrobado(self, nota):
        if nota >= 5:
            print('Estas aprobado con una nota de ' + str(nota))
        else:
            print('Estas suspendido con una nota de ' + str(nota))

    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota

a = Alumno('Pedro', 5)

print(a.isAbrobado(10))

