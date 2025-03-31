import pygame


class HorizontalScrollBar:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value, bg_color, thumb_color):
        self.rect = pygame.Rect(x, y, width, height)  # Прямоугольник для фона ScrollBar
        self.min_value = min_value
        self.max_value = max_value
        self.delta = width / max_value
        self.value = self.delta * initial_value
        self.bg_color = bg_color
        self.thumb_color = thumb_color
        self.thumb_width = 12  # Ширина бегунка
        self.thumb_rect = pygame.Rect(x + width // 2, y, self.thumb_width, height)  # Прямоугольник для бегунка
        self.dragging = False

    def update(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.thumb_rect.x = mouse_pos[0]
            # pygame.draw.rect(screen, self.thumb_color, self.thumb_rect)
        # if self.thumb_rect.collidepoint(mouse_pos):
        #     if mouse_pressed[0]:  # Левая кнопка мыши
        #         self.dragging = True
        #
        # if not mouse_pressed[0]:
        #     self.dragging = False
        #
        # if self.dragging:
        #     # Перемещаем бегунок по горизонтали
        #     self.thumb_rect.x = mouse_pos[0]
        #     # Вычисляем значение ScrollBar
        #     self.value = 0
        # pygame.draw.rect(screen, self.thumb_color, self.thumb_rect)

    def draw(self, screen):
        # Отрисовываем бегунок
        pygame.draw.rect(screen, self.thumb_color, self.thumb_rect)

    def get_value(self):
        return self.value

    def set_thumb_color(self, color):
        self.thumb_color = color

