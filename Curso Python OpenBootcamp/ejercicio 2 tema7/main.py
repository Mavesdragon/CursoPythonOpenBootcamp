import datetime as tm
import pprint

def main():

    pprint.pprint(dir(tm))
    hora_actual = tm.datetime.now()


    if hora_actual.hour>=19 and hora_actual.minute>=0 and hora_actual.second>=0:
        print("Vete a casa empanao!")

    else:
        horas_que_quedan = 19 - int(hora_actual.hour)
        print('Te quedan ', horas_que_quedan, 'para irte a casa')






if __name__ == '__main__':
    main()