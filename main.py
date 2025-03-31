import pygame
import sys

from classes.scrollbar import HorizontalScrollBar
from func.click_zones import create_circle_zone
from func.transitions import fade_transition, transition_with_animation
from func.image_loader import load_image
from func.animations import play_animation

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (203, 172, 102)




# Шрифт
font = pygame.font.Font(None, 74)


# Основной цикл
def main_menu():
    # Создаем зону, которая реагирует на нажатие мыши
    zone_x, zone_y = 0, 0
    zone_width, zone_height = 200, 150
    circle_center_x, circle_center_y = 64, 566  # центр кнопки настроек(шестерёнка)
    circle_radius = 47  # радиус шестерёнки
    # Координаты и размеры кнопок
    button_width, button_height = 220, 90
    button_x = 0  # середина меню WIDTH // 2 - button_width // 2
    button_radius = 20
    play_y = 200
    about_y = 300
    info_y = 400
    exit_x = 420
    exit_y = 525
    # Переменные для анимации
    current_frame = 1
    frame_rate = 30  # Количество кадров в секунду
    clock = pygame.time.Clock()
    current_screen = "menu"
    animations = True
    language = "rus"
    # Загружаем изображение
    image = load_image("image/menu_image.png")
    buttons_settings = [load_image("image/settings/background_settings.png"),
                        load_image("image/settings/buttons_settings.png"),
                        load_image("image/settings/language_eng.png"),
                        load_image("image/settings/language_rus.png"),
                        load_image("image/settings/left_cross_language.png"),
                        load_image("image/settings/left_cross_animation.png"),
                        load_image("image/settings/right_cross_language.png"),
                        load_image("image/settings/right_cross_animation.png"),
                        load_image("image/settings/off.png"),
                        load_image("image/settings/on.png")]

    scrollbar_sound = HorizontalScrollBar(120, 85, 399, 20, 0, 100, 50, WHITE, (86, 153, 128))  # true_width 410, третий аргумент
    scrollbar_music = HorizontalScrollBar(120, 174, 399, 20, 0, 100, 50, WHITE, (86, 153, 128))  # true_width 410, третий аргумент

    # Потом переделать для вызовов ошибок
    if image:
        image_rect = image.get_rect(topleft=(zone_x, zone_y))
    if buttons_settings:
        buttons_settings_rect = []
        for button in buttons_settings:
            buttons_settings_rect.append(button.get_rect(topleft=(zone_x, zone_y)))
    while True:
        # Отрисовка кнопок
        # draw_rounded_button(screen, GREEN, button_x, play_y, button_width, button_height, button_radius, "Играть", BLACK)
        # draw_rounded_button(screen, BLUE, button_x, about_y, button_width, button_height, button_radius, "Об игре", BLACK)
        # draw_rounded_button(screen, BLUE, button_x, info_y, button_width, button_height, button_radius, "Инфа", BLACK)
        # draw_rounded_button(screen, RED, button_x, exit_y, button_width, button_height, button_radius, "Выход", BLACK)
        if current_screen == "menu":
            play_animation(screen, current_frame)
            current_frame = (current_frame + 1) % 14
            if image:
                screen.blit(image, image_rect)
        if current_screen == "settings":
            screen.fill(BLACK)
            if buttons_settings:
                screen.blit(buttons_settings[0], buttons_settings_rect[0])
                screen.blit(buttons_settings[1], buttons_settings_rect[1])
                screen.blit(buttons_settings[3], buttons_settings_rect[3])
                screen.blit(buttons_settings[4], buttons_settings_rect[4])
                screen.blit(buttons_settings[5], buttons_settings_rect[5])
                screen.blit(buttons_settings[6], buttons_settings_rect[6])
                screen.blit(buttons_settings[7], buttons_settings_rect[7])
                screen.blit(buttons_settings[9], buttons_settings_rect[9])
            scrollbar_sound.draw(screen)
            scrollbar_music.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Получение позиции мыши и состояния кнопок
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    # Обновление ScrollBar
                    scrollbar_sound.update(mouse_pos, mouse_pressed)
                    scrollbar_music.update(mouse_pos, mouse_pressed)
                    # Проверка нажатия на кнопки
                    if create_circle_zone(circle_center_x, circle_center_y, circle_radius, mouse_pos[0], mouse_pos[1]) and current_screen == "settings":
                        fade_transition(screen, BLACK, 750)  # Плавное затемнение
                        transition_with_animation(screen)  # Проигрываем анимацию
                        fade_transition(screen, YELLOW, 750)  # Плавное затемнение
                        current_screen = "menu" if current_screen == "settings" else "settings"
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                # Проверка нажатия на кнопки
                if create_circle_zone(circle_center_x, circle_center_y, circle_radius, mouse_pos[0], mouse_pos[1]) and current_screen == "menu":
                    fade_transition(screen, BLACK, 750)  # Плавное затемнение
                    transition_with_animation(screen)  # Проигрываем анимацию
                    fade_transition(screen, BLACK, 750)  # Плавное затемнение
                    current_screen = "settings" if current_screen == "menu" else "menu"
                # elif в зоне стрелки то switch_language
                elif exit_x <= mouse_pos[0] <= exit_x + button_width:
                    if exit_y <= mouse_pos[1] <= exit_y + button_height:
                        pygame.quit()
                        sys.exit()

        # Ограничение FPS
        clock.tick(frame_rate)
        # Обновление экрана
        pygame.display.flip()


# Запуск меню
if __name__ == '__main__':
    main_menu()
