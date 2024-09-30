import pygame
import sys

pygame.init()

# Definición de tamaño de pantalla
pantalla_x = 800
pantalla_y = 600
size = (pantalla_x, pantalla_y)

# Posición inicial del jugador
player_pos = pygame.Vector2(pantalla_x / 2, pantalla_y / 2)

# Configuración del juego
screen = pygame.display.set_mode(size)
fondo = pygame.image.load("imagenes/fondo.jpg")
jugador = pygame.image.load("Sprites/player.jpg")

# Configuración del reloj para controlar la tasa de fotogramas
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar fondo
    screen.blit(fondo, (0, 0))

    # Dibujar el jugador (corregido)
    screen.blit(jugador, player_pos)

    # Manejo del movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 50 * dt
    if keys[pygame.K_s]:
        player_pos.y += 50 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 50 * dt
    if keys[pygame.K_d]:
        player_pos.x += 50 * dt

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la tasa de fotogramas
    dt = clock.tick(60) / 1000
