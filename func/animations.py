import pygame
from func.image_loader import load_image
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 640, 640


def fade_animation(screen, color, duration):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)
    for alpha in range(0, 255, 5):  # Увеличиваем прозрачность
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration // 50)

# Основной цикл
def play_animation(screen, current_frame,zone_x, zone_y):
    # Example implementation
    animation_frames = [load_image(f"image/pink_cat/pink_cat{i}.png") for i in range(14)]
    if 0 <= current_frame < len(animation_frames):
        screen.blit(animation_frames[current_frame], (zone_x, zone_y))
