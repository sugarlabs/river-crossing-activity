import pygame
import config

class Button:
    def __init__(self, x, y, label, action, w = None, h = None, scale_factor = 0.05, font = None):
        image = config.images.get("button")

        if h is not None:
            m_w = int(image.get_width() * (h / image.get_height()))
            image = pygame.transform.scale(image, (m_w, int(h)))
        if w is not None:
            m_h = int(image.get_height() * (w / image.get_width()))
            image = pygame.transform.scale(image, (int(w), m_h))

        self.rect = image.get_rect()

        self.graphic_default = image
        self.graphic_hovered = pygame.transform.scale(
            image, (int(self.rect.width * (1 + scale_factor)), int(self.rect.height * (1 + scale_factor))))
        
        self.x = x - self.rect.width // 2
        self.y = y - self.rect.height // 2
        self.rect.x = self.x
        self.rect.y = self.y

        if font is None:
            font = config.font_primary.md

        text_color = config.colors["text"]
        self.label = font.render(label, True, text_color)
        self.gameDisplay = pygame.display.get_surface()

        self.action = action
        self.scale_factor = scale_factor

        self.press = False
        self.draw()

    def draw(self):
        if self.hovered():
            m_x = self.x - self.rect.width * (self.scale_factor / 2)
            m_y = self.y - self.rect.height * (self.scale_factor / 2)
            self.gameDisplay.blit(self.graphic_hovered, (m_x, m_y))
        else:
            self.gameDisplay.blit(self.graphic_default, (self.x, self.y))

        label_rect = self.label.get_rect()
        m_x = self.x + self.rect.width // 2 - label_rect.width // 2
        m_y = self.y + self.rect.height // 2 - int(label_rect.height * 0.7)
        self.gameDisplay.blit(self.label, (m_x, m_y))

    def hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        self.draw()
        pressed_btn = pygame.mouse.get_pressed()[0]
        if self.press and self.hovered() and pressed_btn != 1:
            self.action()

        if self.hovered() and pressed_btn == 1:
            self.press = True
        else:
            self.press = False