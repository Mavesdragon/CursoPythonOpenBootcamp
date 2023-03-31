anno_introducido = int(input('Escribe un año'))

def comprobar_bisiesto(a):
    if a % 4 == 0:
        print('es un año bisiesto')
    else:
        print('es un año no bisiesto')


comprobar_bisiesto(anno_introducido)