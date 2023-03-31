
class Vehiculo:
    marca = ''
    modelo = ''
    cilindrada = 0

    def __init__(self,marca,modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

v1 = Vehiculo('Volvo', 'Penta', 2000)

