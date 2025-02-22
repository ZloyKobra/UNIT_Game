import pygame

from func.text import draw_text


# Функция для создания кнопок
def draw_button(surface, color, x, y, width, height, text, text_color, font):
    pygame.draw.rect(surface, color, (x, y, width, height))
    draw_text(text, font, text_color, surface, x + width // 2, y + height // 2)


# Функция для создания кнопок с закругленными углами
def draw_rounded_button(surface, color, x, y, width, height, radius, text, text_color, font):
    # Рисуем прямоугольник с закругленными углами
    pygame.draw.rect(surface, color, (x + radius, y, width - 2 * radius, height))
    pygame.draw.rect(surface, color, (x, y + radius, width, height - 2 * radius))
    # Рисуем круги для закругленных углов
    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + width - radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + radius, y + height - radius), radius)
    pygame.draw.circle(surface, color, (x + width - radius, y + height - radius), radius)
    # Рисуем текст на кнопке
    draw_text(text, font, text_color, surface, x + width // 2, y + height // 2)
