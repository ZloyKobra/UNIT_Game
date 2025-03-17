import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 640, 640


# Функция для проигрывания анимации
def play_animation(screen, current_frame):
    frame = pygame.image.load(f"image/pink_cat/pink_cat{current_frame}.png")  # Загружаем кадры анимации
    screen.blit(frame, (WIDTH // 2 - frame.get_width() // 3, HEIGHT // 2 - frame.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(100)  # Задержка между кадрами



