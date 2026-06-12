piso_actual = 1
piso_minimo = 1
piso_maximo = 3
destinos = []
direccion = "quieto"

def mostrar_edificio(m=""):
    print("\n###  EDIFICIO ###")
    if m: 
        print(f"-> {m}")
    print(f"  Piso actual: {piso_actual}")
    for p in range(piso_maximo, piso_minimo - 1, -1):
        Final = " F " if p in destinos else "   "
        if p == piso_actual:
            if direccion == "subiendo": 
                a = "[   /\\   ]"
            elif direccion == "bajando": 
                a = "[   \\/   ]"
            else: 
                a = "[  [[]]  ]" if p in destinos else "[   []   ]"
            print(f"  Piso {p:2} {Final}  {a}  << AQUI ESTOY")
        else:
            print(f"  Piso {p:2} {Final}  [       ]")
    print("#################\n")

def mover():  
    global piso_actual, direccion, destinos
    
    if direccion == "quieto":
        if destinos[0] > piso_actual:
            direccion = "subiendo"
        else:
            direccion = "bajando"
    
    sig = None
    if direccion == "subiendo":
        sup = [p for p in destinos if p > piso_actual]
        if sup: 
            sig = min(sup)
        else: 
            direccion = "bajando"
            inf = [p for p in destinos if p < piso_actual]
            if inf: 
                sig = max(inf)
    else:  
        inf = [p for p in destinos if p < piso_actual]
        if inf: 
            sig = max(inf)
        else: 
            direccion = "subiendo"
            sup = [p for p in destinos if p > piso_actual]
            if sup: 
                sig = min(sup)
                
    if sig is None and destinos:
        sig = piso_actual
        
    while piso_actual != sig:
        piso_actual += 1 if direccion == "subiendo" else -1
        mostrar_edificio(f"Yendo hacia el piso {sig}...")
        if piso_actual in destinos:
            break
    
    # Llegada al piso
    if piso_actual in destinos:
        print(f"Llegamos al piso {piso_actual}")
        destinos.remove(piso_actual)   
    
    if not destinos:
        direccion = "quieto"


# Inicio del código
print(" BIENVENIDO AL SIMULADOR DE ASCENSOR (3 PISOS)")

while True:
    mostrar_edificio()
    with open(r"C:\Users\nic_b\Desktop\MENU_PRINCIPAL.txt", "r") as menu1:
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
                if p not in destinos and p != piso_actual:
                    destinos.append(p)
            while destinos: 
                mover()
        else:
            print("No ingresaste ningún piso válido. Solo pisos 1, 2 o 3")
            
    elif i == 2:
        with open(r"C:\Users\nic_b\Desktop\Menu2.txt", "r") as menu2:
            contenido = menu2.read()
            print(contenido)
        
    elif i == 3:
        print("Simulacion finalizada")
        break
        
    else:
        print("Opcion no valida")
