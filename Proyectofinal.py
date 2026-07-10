import pygame
from collections import deque

class Elevador:
    def __init__(self, marca, modelo, piso_inicial):
        self.marca = marca
        self.modelo = modelo
        self.piso = piso_inicial
        self.pisos_disponibles = {1: 500, 2: 300, 3: 100}  # Coordenadas Y
        self.destino = self.pisos_disponibles[piso_inicial]
        self.cola_pisos = deque()  # Cola para almacenar pisos pendientes
        self.en_movimiento = False
        
    def seleccionar_piso(self, piso):
        """Agrega un piso a la cola de destinos"""
        if 1 <= piso <= 3:
            # Evitar agregar el piso actual si ya está en la cola o es el destino actual
            if piso != self.piso:
                # Verificar si el piso ya está en la cola
                if piso not in self.cola_pisos:
                    self.cola_pisos.append(piso)
                    print(f"Piso {piso} agregado a la cola")
                    return True
                else:
                    print(f"Piso {piso} ya está en la cola")
                    return False
            else:
                print(f"Ya estás en el piso {piso}")
                return False
        else:
            print("Piso no válido")
            return False
    
    def procesar_cola(self):
        """Procesa el siguiente piso en la cola"""
        if self.cola_pisos and not self.en_movimiento:
            siguiente_piso = self.cola_pisos.popleft()
            self.destino = self.pisos_disponibles[siguiente_piso]
            self.piso = siguiente_piso
            self.en_movimiento = True
            print(f"Ascensor en camino al piso {siguiente_piso}")
            return True
        return False
    
    def llegar_destino(self):
        """Se llama cuando el ascensor llega a su destino"""
        self.en_movimiento = False
        print(f"Ascensor llegó al piso {self.piso}")
        # Procesar siguiente piso en la cola
        self.procesar_cola()
    
    def obtener_posicion_y(self):
        """Devuelve la posición Y actual del elevador"""
        return self.destino

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Simulador de Ascensor")
reloj = pygame.time.Clock()

# Crear el elevador
elevador = Elevador("Samsung", "V4", 1)

# Variables para el movimiento
y_ascensor = 500  # Posición inicial
velocidad = 3      # Velocidad de movimiento
umbral_llegada = 5  # Margen para considerar que llegó al destino

# Bucle principal
running = True
while running:
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        
        if evento.type == pygame.KEYDOWN:
            # Usar la clase Elevador para seleccionar piso
            if evento.key == pygame.K_1:
                elevador.seleccionar_piso(1)
            elif evento.key == pygame.K_2:
                elevador.seleccionar_piso(2)
            elif evento.key == pygame.K_3:
                elevador.seleccionar_piso(3)
    
    # Lógica de movimiento
    destino_y = elevador.destino
    
    # Verificar si hay cola y el ascensor no está en movimiento
    if not elevador.en_movimiento and elevador.cola_pisos:
        elevador.procesar_cola()
        # Actualizar destino después de procesar la cola
        destino_y = elevador.destino
    
    # Movimiento del ascensor
    if elevador.en_movimiento:
        if y_ascensor < destino_y:
            y_ascensor = min(y_ascensor + velocidad, destino_y)
        elif y_ascensor > destino_y:
            y_ascensor = max(y_ascensor - velocidad, destino_y)
        
        # Verificar si llegó al destino
        if abs(y_ascensor - destino_y) < umbral_llegada:
            y_ascensor = destino_y
            elevador.llegar_destino()
    
    # Renderizado
    pantalla.fill((30, 30, 30))
    
    # Dibujar el edificio
    pygame.draw.rect(pantalla, (135, 206, 235), (0, 0, 120, 600))
    pygame.draw.rect(pantalla, (135, 206, 235), (120, 0, 300, 50))
    pygame.draw.rect(pantalla, (135, 206, 235), (260, 0, 400, 600))
    pygame.draw.rect(pantalla, (128, 128, 128), (10, 30, 130, 600))
    pygame.draw.rect(pantalla, (128, 128, 128), (260, 30, 130, 600))
    pygame.draw.rect(pantalla, (128, 128, 128), (140, 30, 170, 50))
    pygame.draw.rect(pantalla, (50, 50, 50), (5, 20, 390, 25))
    
    # Ventanas
    pygame.draw.rect(pantalla, (130, 200, 250), (90, 520, 30, 60))
    pygame.draw.line(pantalla,(224, 255, 255),(90,565),(119,520),10)
    pygame.draw.line(pantalla,(224, 255, 255),(90,550),(110,520),5)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 520, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (120, 520, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 520, 40, 5), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 575, 40, 5), 2)
    
    pygame.draw.rect(pantalla, (130, 200, 250), (90, 320, 30, 60))
    pygame.draw.line(pantalla,(224, 255, 255),(90,365),(119,320),10)
    pygame.draw.line(pantalla,(224, 255, 255),(90,350),(110,320),5)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 320, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (120, 320, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 320, 40, 5), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 375, 40, 5), 2)
    
    pygame.draw.rect(pantalla, (130, 200, 250), (90, 120, 30, 60))
    pygame.draw.line(pantalla,(224, 255, 255),(90,165),(119,120),10)
    pygame.draw.line(pantalla,(224, 255, 255),(90,150),(110,120),5)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 120, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (120, 120, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 120, 40, 5), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (85, 175, 40, 5), 2)
    
    pygame.draw.rect(pantalla, (130, 200, 250), (280, 520, 30, 60))
    pygame.draw.line(pantalla,(224, 255, 255),(280,565),(309,520),10)
    pygame.draw.line(pantalla,(224, 255, 255),(280,550),(300,520),5)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 520, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (310, 520, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 520, 40, 5), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 575, 40, 5), 2)
    
    pygame.draw.rect(pantalla, (130, 200, 250), (280, 320, 30, 60))
    pygame.draw.line(pantalla,(224, 255, 255),(280,365),(309,320),10)
    pygame.draw.line(pantalla,(224, 255, 255),(280,350),(300,320),5)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 320, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (310, 320, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 320, 40, 5), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 375, 40, 5), 2)
    
  
    pygame.draw.rect(pantalla, (130, 200, 250), (280, 120, 30, 60))
    pygame.draw.line(pantalla,(224, 255, 255),(280,165),(309,120),10)
    pygame.draw.line(pantalla,(224, 255, 255),(280,150),(300,120),5)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 120, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (310, 120, 5, 60), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 120, 40, 5), 2)
    pygame.draw.rect(pantalla, (255, 255, 255), (275, 175, 40, 5), 2)
    
    # Dibujar el ascensor
    pygame.draw.rect(pantalla, (255, 0, 0), (150, int(y_ascensor), 100, 100))
    pygame.draw.rect(pantalla, (200, 200, 200), (150, int(y_ascensor), 100, 100), 3)  # Borde
    
    fuente = pygame.font.Font(None, 36)
    texto_piso = fuente.render(f"Piso: {elevador.piso}", True, (255, 255, 255))
    pantalla.blit(texto_piso, (170, 20))
    
    fuente_pequena = pygame.font.Font(None, 24)
    if elevador.cola_pisos:
        cola_texto = f"Cola: {list(elevador.cola_pisos)}"
        texto_cola = fuente_pequena.render(cola_texto, True, (0, 255, 0))
        pantalla.blit(texto_cola, (170, 60))
  
    instrucciones = fuente_pequena.render("Presiona 1, 2 o 3 para llamar al ascensor", True, (200, 200, 0))
    pantalla.blit(instrucciones, (20, 50))
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
