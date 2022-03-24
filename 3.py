from random import randint as rd

def fechaAleatoria(año_minimo):
    año = str(rd(año_minimo, 2022))
    mes = rd(1, 12)
    if mes < 10:
        mes = "0" + str(mes)
    dia = rd(0, 30)
    if dia < 10:
        dia = "0" + str(dia)
    date = año + str(mes) + str(dia)

    return int(date)

class cuentaNormal:
    def __init__(self, ID, nombre, saldo):
        self.fecha_apertura = fechaAleatoria(1930)
        self.numero_cuenta = rd(100000000000, 999999999999)
        self.id = int(ID)
        self.nombre_appellido = nombre
        self.saldo = float(saldo)

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
        else:
            print("No puedes retirar tanto dinero")
    
    def transferir(self, recept, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            recept.saldo = recept.saldo + cantidad
        else:
            print("No puede transferir tanta cantidad")


class cuentaPlazoFijo:
    def __init__(self, ID, nombre, saldo):
        self.fecha_apertura = fechaAleatoria(1930)
        self.fechaComision = fechaAleatoria((self.fecha_apertura + 1) // 10000)
        self.numero_cuenta = rd(100000000000, 999999999999)
        self.id = int(ID)
        self.nombre_appellido = nombre
        self.saldo = float(saldo)

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad, fechaActual):
        if fechaActual < self.fechaComision:
            cantidad = cantidad - (cantidad * 5 / 100)

        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
        else:
            print("No puedes retirar tanto dinero")
    
    def transferir(self, recept, cantidad, fechaActual):
        if fechaActual < self.fechaComision:
            cantidad = cantidad - (cantidad * 5 / 100)

        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            recept.saldo = recept.saldo + cantidad
        else:
            print("No puede transferir tanta cantidad")

class cuentaVip:
    def __init__(self, ID, nombre, saldo):
        self.fecha_apertura = fechaAleatoria(1930)
        self.numero_cuenta = rd(100000000000, 999999999999)
        self.maximaDeuda = -5000
        self.id = int(ID)
        self.nombre_appellido = nombre
        self.saldo = float(saldo)

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
        else:
            if self.saldo - cantidad >= self.maximaDeuda:
                self.saldo = self.saldo - cantidad
            else:
                print("No puede transferir tanta cantidad")
    
    def transferir(self, recept, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            recept.saldo = recept.saldo + cantidad
        else:
            if self.saldo - cantidad >= self.maximaDeuda:
                self.saldo = self.saldo - cantidad
                recept.saldo = recept.saldo + cantidad
            else:
                print("No puede transferir tanta cantidad")


cuenta1 = cuentaNormal(1, "Pepe", 10000)
cuenta2 = cuentaPlazoFijo(2, "Juan", 10000)
cuenta3 = cuentaVip(3, "Maria", 10000)

cuenta1.transferir(cuenta2, 2000)
cuenta1.ingresar(500)
cuenta2.retirar(750, 20210323)
cuenta3.retirar(12000)
