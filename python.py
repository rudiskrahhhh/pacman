import pygame
import sys
import random
import math

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
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Borders
border_width = 20

# Pacman properties
pacman_radius = 20
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Dot properties
dot_radius = 5
dot_gap = 50  # Gap between dots
dots = []

# Generate dots with even distribution
num_dots_per_row = math.floor((WIDTH - 2 * border_width) / dot_gap)
num_rows = math.floor((HEIGHT - 2 * border_width) / dot_gap)
for i in range(num_rows):
    y = border_width + i * dot_gap
    if i % 2 == 0:
        start_x = border_width + dot_gap / 2
    else:
        start_x = border_width
    for j in range(num_dots_per_row):
        x = start_x + j * dot_gap
        dots.append((x, y))

# Enemy properties
enemy_radius = 15
enemy_speed = 3

class Enemy:
    def __init__(self):
        self.x = random.randint(border_width + enemy_radius, WIDTH - border_width - enemy_radius)
        self.y = random.randint(border_width + enemy_radius, HEIGHT - border_width - enemy_radius)
        self.color = RED
    
    def move_towards_pacman(self):
        dx = pacman_x - self.x
        dy = pacman_y - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist != 0:
            self.x += enemy_speed * dx / dist
            self.y += enemy_speed * dy / dist

    def check_collision_with_pacman(self):
        dx = pacman_x - self.x
        dy = pacman_y - self.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist <= pacman_radius + enemy_radius:
            return True
        return False

enemies = [Enemy() for _ in range(3)]

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

    # Move enemies towards Pacman
    for enemy in enemies:
        enemy.move_towards_pacman()

        # Check for collision with Pacman
        if enemy.check_collision_with_pacman():
            print("Game Over!")
            running = False

    # Draw borders
    pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, border_width))  # Top border
    pygame.draw.rect(screen, BLUE, (0, 0, border_width, HEIGHT)) # Left border
    pygame.draw.rect(screen, BLUE, (WIDTH-border_width, 0, border_width, HEIGHT)) # Right border
    pygame.draw.rect(screen, BLUE, (0, HEIGHT-border_width, WIDTH, border_width)) # Bottom border

    # Draw Pacman
    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.circle(screen, enemy.color, (int(enemy.x), int(enemy.y)), enemy_radius)

    # Draw dots
    for dot in dots:
        pygame.draw.circle(screen, WHITE, dot, dot_radius)

    # Check for dot collection
    dots_to_remove = []
    for dot in dots:
        dx = dot[0] - pacman_x
        dy = dot[1] - pacman_y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist <= pacman_radius + dot_radius:
            dots_to_remove.append(dot)
    for dot in dots_to_remove:
        dots.remove(dot)

    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
