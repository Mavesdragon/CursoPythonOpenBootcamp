import operaciones.operaciones as opb


def main():
    suma = opb.sumar(2, 5)
    resta = opb.restar(2, 5)
    multiplicacion = opb.multiplicar(2, 5)
    division = opb.dividir(2, 5)

    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)


if __name__ == '__main__':
    main()
