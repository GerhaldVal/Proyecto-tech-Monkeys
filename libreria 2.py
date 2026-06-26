import pygame

# ventana
pygame.init()
pantalla = pygame.display.set_mode((400, 600))
reloj = pygame.time.Clock()

# ascensor
y_ascensor = 500 # posicion inicial
velocidad = 5     # Corregido typo "velociadad"
destino = 500

# pisos
pisos = {1: 500, 2: 300, 3: 100}

# bucle principal
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        
        # teclas de pisos (Corregido: K en mayúscula)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1: destino = pisos[1]
            if evento.key == pygame.K_2: destino = pisos[2]
            if evento.key == pygame.K_3: destino = pisos[3]

    # --- TODO ESTO DEBE IR DENTRO DEL BUCLE WHILE (INDENTADO) ---
    
    # Lógica de movimiento (Evita el tembleque de la pantalla)
    if y_ascensor < destino: 
        y_ascensor = min(y_ascensor + velocidad, destino)
    elif y_ascensor > destino: 
        y_ascensor = max(y_ascensor - velocidad, destino)

    # Renderizado / Pantalla
    pantalla.fill((30, 30, 30))
    
    # Dibujar el ascensor (un cuadrado rojo)
    pygame.draw.rect(pantalla, (255, 0, 0), (150, y_ascensor, 100, 100))

    pygame.display.flip()
    reloj.tick(60) # 60 fps

# Fuera del bucle al cerrar el juego
pygame.quit()