import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Borders
border_width = 20

# Pacman properties
pacman_radius = 20
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pacman_x > border_width + pacman_radius:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT] and pacman_x < WIDTH - border_width - pacman_radius:
        pacman_x += pacman_speed
    if keys[pygame.K_UP] and pacman_y > border_width + pacman_radius:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN] and pacman_y < HEIGHT - border_width - pacman_radius:
        pacman_y += pacman_speed

     # Prevent diagonal movement
    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
        pacman_speed = 0

    # Draw borders
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, border_width))  # Top border
    pygame.draw.rect(screen, BLUE, (0, 0, border_width, HEIGHT)) # Left border
    pygame.draw.rect(screen, BLUE, (WIDTH-border_width, 0, border_width, HEIGHT)) # Right border
    pygame.draw.rect(screen, BLUE, (0, HEIGHT-border_width, WIDTH, border_width)) # Bottom border

    # Draw Pacman
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)

    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
