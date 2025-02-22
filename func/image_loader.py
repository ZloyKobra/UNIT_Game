import pygame


# Функция для загрузки изображений
def load_image(path):
    """
    Загружает изображение из файла.
    :param path: Путь к файлу изображения.
    :return: Загруженное изображение (Surface) или None, если файл не найден.
    """
    try:
        image = pygame.image.load(path)
        return image
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не найден.")
        return None
