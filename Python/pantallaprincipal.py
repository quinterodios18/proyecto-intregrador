import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir tamaño de pantalla
pantalla_x = 800
pantalla_y = 600
size = (pantalla_x, pantalla_y)

# Configurar la pantalla
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sea Life")

# Cargar imagen de fondo
fondo = pygame.image.load("imagenes/menu.jpg").convert()

# Definir colores
color_jugar = (173, 216, 230)  # Color azul claro
color_ajustes = (255, 255, 153)  # Color amarillo claro
color_desarrolladores = (144, 238, 144)  # Color verde claro
color_texto = (0, 0, 0)  # Color negro

# Fuente del texto
fuente = pygame.font.Font(None, 50)

# Crear textos
texto_jugar = fuente.render("JUGAR", True, color_texto)
texto_ajustes = fuente.render("AJUSTES", True, color_texto)
texto_desarrolladores = fuente.render("DESARROLLADORES", True, color_texto)

# Definir rectángulos para los botones
boton_jugar = pygame.Rect(300, 200, 200, 60)
boton_ajustes = pygame.Rect(300, 300, 200, 60)
boton_desarrolladores = pygame.Rect(300, 400, 200, 60)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detectar clics en los botones
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar.collidepoint(event.pos):
                print("Jugar")
            elif boton_ajustes.collidepoint(event.pos):
                print("Ajustes")
            elif boton_desarrolladores.collidepoint(event.pos):
                print("Desarrolladores")

    # Dibujar fondo
    screen.blit(fondo, (0, 0))

    # Dibujar botones
    pygame.draw.rect(screen, color_jugar, boton_jugar)
    pygame.draw.rect(screen, color_ajustes, boton_ajustes)
    pygame.draw.rect(screen, color_desarrolladores, boton_desarrolladores)

    # Dibujar textos sobre los botones
    screen.blit(texto_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
    screen.blit(texto_ajustes, (boton_ajustes.x + 40, boton_ajustes.y + 10))
    screen.blit(texto_desarrolladores, (boton_desarrolladores.x + 10, boton_desarrolladores.y + 10))

    # Actualizar la pantalla
    pygame.display.update()
