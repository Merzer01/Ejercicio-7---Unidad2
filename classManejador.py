import csv
from classViajeroFrecuente import viajerofrecuente

class Manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def readArchivo (self):         #lectura del arcchivo y carga
        with open ("viajerofrecuente.csv") as archivo:
            lector = csv.reader(archivo, delimiter=',')
            next(lector)

            for row in lector:
                num = row[0]
                doc = row[1]
                nomb = row[2]
                ap = row[3]
                mill = int(row[4])
                vf = viajerofrecuente(num, doc, nomb, ap, mill)
                self.__lista.append(vf)
    def buscar(self, num):          #busca y evalua el viajero frecuente
        p=0
        band=False
        while p < len(self.__lista) and band == False:
            dato = int(self.__lista[p].numviajero())
            if dato == num:
                band = True
            else: p = p+1
        return p
    def options(self, p):
        op = int(input("Ingrese opcion: "))
        while True:
            if op == 1:
                dato = int(input("Ingrese cantidad de millas a comparar: "))
                if (dato == self.__lista[p]) and (self.__lista[p] == dato):
                    print("LAS MILLAS SON IGUALES AL VALOR INGRESADO")
                else: print("LOS VALORES SON DISTINTOS")
                print("------------------------------")
            elif op == 2:
                dato = int(input("Ingrese la cantidad a acumular: "))
                self.__lista[p] = dato + self.__lista[p]
                print("Se acumularon {} millas. Millas actuales -> {}".format(dato, self.__lista[p].cantidadTotaldeMillas()))
                print("------------------------------")
            elif op == 3:
                dato = int(input("Ingrese las millas a canjear: "))
                if dato <= self.__lista[p].cantidadTotaldeMillas():
                    self.__lista[p] = dato - self.__lista[p]
                    print("Se canjearon {} millas. Millas actuales -> {}".format(dato, self.__lista[p].cantidadTotaldeMillas()))
                    print("------------------------------")
                else:
                    print("ERROR AL CANJEAR MILLAS (Millas insuficientes)")
                    print("------------------------------")
            elif op == 0:
                print("-----FIN-----")
                break
            else:
                print("Opcion invalida")
            op = int(input("Ingrese opcion: "))
    def mostrar(self):              #imprime los datos (evaluar eliminacion o no)
        for i in range(len(self.__lista)):
            print(self.__lista[i])