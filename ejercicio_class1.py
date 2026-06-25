class Elevador:
    def __init__(self, marca, modelo, piso,piso_bloqueado):
        self.marca = marca
        self.modelo = modelo
        self.piso = piso
        self.piso_bloqueado = piso_bloqueado

    def seleccionar_piso(self):
        self.piso = int(input("Ingrese el piso al que quiere llegar: "))

        if 1 <= self.piso <= 3:
            print(f"Usted ha llegado al piso: {self.piso}")
        else:
            print("Piso no válido")
    def bloqueo_de_piso(self):
        self.piso_bloqueado = int(input("Ingrese el piso al que quiere llegar: "))
        if self.piso_bloqueado == self.piso:
            print("Piso bloqueado (Usted esta aqui).")
        elif 1<= self.piso_bloqueado <= 3:
            print("Ha llegado al piso.")
        else:
            print("Piso inexistente.")

AlturaSegura = Elevador("Samsung", "V4", 1,8)
AlturaSegura.seleccionar_piso()
AlturaSegura.bloqueo_de_piso()

 
