import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 640, 640


# Функция для плавного перехода
def fade_transition(screen, color, duration):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill(color)
    for alpha in range(0, 255, 5):  # Увеличиваем прозрачность
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration // 50)


# Функция для проигрывания анимации
def transition_with_animation(screen):
    frames = [
        pygame.image.load(f"image/pink_cat/pink_cat{i}.png") for i in range(0, 14)  # Загружаем кадры анимации
    ]
    for frame in frames:
        screen.fill(BLACK)  # Очищаем экран
        screen.blit(frame, (WIDTH // 2 - frame.get_width() // 2, HEIGHT // 2 - frame.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(100)  # Задержка между кадрами
