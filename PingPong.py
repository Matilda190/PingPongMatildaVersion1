import pygame

pygame.init()

# Crear ventana
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("PingPong")

# Reloj del juego
clock = pygame.time.Clock()

# Ciclo principal
game = True

while game:

    # Revisar eventos
    for event in pygame.event.get():

        # Cerrar ventana
        if event.type == pygame.QUIT:
            game = False

    # Color de fondo
    window.fill((216, 209, 219))

    # Actualizar pantalla
    pygame.display.update()

    # 60 FPS
    clock.tick(60)

pygame.quit()