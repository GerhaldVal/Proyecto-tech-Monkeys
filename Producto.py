class Ascensor:
    piso_actual = 1
    piso_minimo = 1
    piso_maximo = 3
    destinos = []
    direccion = "quieto"
    
    def mostrar_edificio(self, m=""):
        print("\n###  EDIFICIO ###")
        if m: 
            print(f"-> {m}")
        print(f"  Piso actual: {self.piso_actual}")
        for p in range(self.piso_maximo, self.piso_minimo - 1, -1):
            Final= " F " if p in self.destinos else "   "
            if p == self.piso_actual:
                if self.direccion == "subiendo": 
                    a = "[   /\\   ]"
                elif self.direccion == "bajando": 
                    a = "[   \\/   ]"
                else: 
                    a = "[  [[]]  ]" if p in self.destinos else "[   []   ]"
                print(f"  Piso {p:2} {Final}  {a}  << AQUI ESTOY")
            else:
                print(f"  Piso {p:2} {Final}  [       ]")
        print("#################\n")

    def mover(self):  
        if self.direccion == "quieto":
            if self.destinos[0] > self.piso_actual:
                self.direccion = "subiendo"
            else:
                self.direccion = "bajando"
        
        sig = None
        if self.direccion == "subiendo":
            sup = [p for p in self.destinos if p > self.piso_actual]
            if sup: 
                sig = min(sup)
            else: 
                self.direccion = "bajando"
                inf = [p for p in self.destinos if p < self.piso_actual]
                if inf: 
                    sig = max(inf)
        else:  
            inf = [p for p in self.destinos if p < self.piso_actual]
            if inf: 
                sig = max(inf)
            else: 
                self.direccion = "subiendo"
                sup = [p for p in self.destinos if p > self.piso_actual]
                if sup: 
                    sig = min(sup)
                    
        if sig is None and self.destinos:
            sig = self.piso_actual
            
        while self.piso_actual != sig:
            self.piso_actual += 1 if self.direccion == "subiendo" else -1
            self.mostrar_edificio(f"Yendo hacia el piso {sig}...")
            if self.piso_actual in self.destinos:
                break
        
        # Llegada al piso
        if self.piso_actual in self.destinos:
            print(f"Llegamos al piso {self.piso_actual}")
            self.destinos.remove(self.piso_actual)   
        
        if not self.destinos:
            self.direccion = "quieto"


# Inicio del código
piso = Ascensor()
print(" BIENVENIDO AL SIMULADOR DE ASCENSOR (3 PISOS)")

while True:
    piso.mostrar_edificio()
    with open (r"C:\Users\nic_b\Desktop\MENU_PRINCIPAL.txt" , "r" ) as menu1:
        contenido = menu1.read()
        print(contenido)
    i = int(input("Que deseas hacer (1-3): "))

    if i == 1:
        print("Pisos disponibles: 1, 2, 3")
        e = input("A qué pisos quieres ir (ej: 1,2,3): ")
        pv = []
        for p in e.split(","):
            try: 
                pv.append(int(p.strip()))
            except: 
                continue
        
        
        pv_validos = [p for p in pv if 1 <= p <= 3]
        
        if pv_validos:
            for p in pv_validos:
                if p not in piso.destinos and p != piso.piso_actual:
                    piso.destinos.append(p)
            while piso.destinos: 
                piso.mover()
        else:
            print("No ingresaste ningún piso válido. Solo pisos 1, 2 o 3")
            
    elif i == 2:
            with open (r"C:\Users\nic_b\Desktop\Menu2.txt" , "r" ) as menu2:
                       contenido = menu2.read()
                       print(contenido)
        
    elif i == 3:
        print("Simulacion finalizada")
        break
        
    else:
        print("Opcion no valida")
