import pygame

pygame.init()

# Fuente
font = pygame.font.SysFont("Arial", 35)

texto_jugador1 = font.render("Jugador 1 Gana", True, (157, 0, 255))
texto_jugador2 = font.render("Jugador 2 Gana", True, (157, 0, 255))

# Crear ventana
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("PingPong")

# Reloj del juego
clock = pygame.time.Clock()

# Colores
fondo = (216, 209, 219)
morado = (145, 120, 170)

# Barreras
barra_1 = pygame.Rect(40, 180, 25, 140)
barra_2 = pygame.Rect(735, 180, 25, 140)

# Velocidad de las barreras
velocidad_barra = 6

# Pelota
pelota = pygame.image.load("pelota.png").convert_alpha()
pelota = pygame.transform.scale(pelota, (40, 40))

pelota_rect = pelota.get_rect()
pelota_rect.center = (400, 250)

# Velocidad de la pelota
velocidad_x = 4
velocidad_y = 4

# Ganador
ganador = 0

# Ciclo principal
game = True

while game:

    # Revisar eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    # El juego solo funciona si nadie ha ganado
    if ganador == 0:

        # Teclas
        teclas = pygame.key.get_pressed()

        # Jugador 1 - W y S
        if teclas[pygame.K_w]:
            barra_1.y -= velocidad_barra

        if teclas[pygame.K_s]:
            barra_1.y += velocidad_barra

        # Jugador 2 - Flechas
        if teclas[pygame.K_UP]:
            barra_2.y -= velocidad_barra

        if teclas[pygame.K_DOWN]:
            barra_2.y += velocidad_barra

        # Evitar que las barras salgan
        if barra_1.top < 0:
            barra_1.top = 0

        if barra_1.bottom > 500:
            barra_1.bottom = 500

        if barra_2.top < 0:
            barra_2.top = 0

        if barra_2.bottom > 500:
            barra_2.bottom = 500

        # Mover pelota
        pelota_rect.x += velocidad_x
        pelota_rect.y += velocidad_y

        # Rebote arriba
        if pelota_rect.top <= 0:
            pelota_rect.top = 0
            velocidad_y *= -1

        # Rebote abajo
        if pelota_rect.bottom >= 500:
            pelota_rect.bottom = 500
            velocidad_y *= -1

        # Rebote con barra 1
        if pelota_rect.colliderect(barra_1) and velocidad_x < 0:
            pelota_rect.left = barra_1.right
            velocidad_x *= -1

        # Rebote con barra 2
        if pelota_rect.colliderect(barra_2) and velocidad_x > 0:
            pelota_rect.right = barra_2.left
            velocidad_x *= -1

        # Si la pelota sale por la derecha
        if pelota_rect.left > 800:
            ganador = 1

        # Si la pelota sale por la izquierda
        if pelota_rect.right < 0:
            ganador = 2

    # Dibujar fondo
    window.fill(fondo)

    # Dibujar barras
    pygame.draw.rect(window, morado, barra_1, border_radius=10)
    pygame.draw.rect(window, morado, barra_2, border_radius=10)

    # Dibujar pelota
    window.blit(pelota, pelota_rect)

    # Mostrar ganador
    if ganador == 1:
        window.blit(texto_jugador1, (290, 220))

    if ganador == 2:
        window.blit(texto_jugador2, (290, 220))

    # Actualizar pantalla
    pygame.display.update()

    # 60 FPS
    clock.tick(60)

pygame.quit()