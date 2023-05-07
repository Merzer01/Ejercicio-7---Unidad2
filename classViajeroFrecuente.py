class viajerofrecuente:
    __nro_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, nro, doc, nomb, ape, mill):      #CONTRUCTOR
        self.__nro_viajero = nro
        self.__dni = doc
        self.__nombre = nomb
        self.__apellido = ape
        self.__millas_acum = mill
    def __str__(self):
        return("{} {} - {}| Nro: {} - Millas Acumuladas: {}".format(self.__apellido, self.__nombre, self.__dni, self.__nro_viajero, self.__millas_acum))
    def numviajero(self):
        return self.__nro_viajero
    def __eq__(self, other):
        if isinstance (other, int):
            return self.__millas_acum == other
        elif isinstance (other, viajerofrecuente):
            return self.__millas_acum == other.__millas_acum
        else:
            return False
    def __radd__(self, other):
        if isinstance (other, int):
            return viajerofrecuente(self.__nro_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + other)
    def __rsub__(self, other):
        if isinstance(other, int):
            return viajerofrecuente(self.__nro_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - other)
    def cantidadTotaldeMillas(self):
        return self.__millas_acum