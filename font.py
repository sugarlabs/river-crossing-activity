import pygame

class Font:
    def __init__(self):
        self.sm = None
        self.md = None
        self.lg = None

    def intialize(self, file):
        self.sm = self.load_font(file, 10)
        self.md = self.load_font(file, 16)
        self.lg = self.load_font(file, 20)
        self.xl = self.load_font(file, 26)

    def load_font(self, file, size):
        return pygame.font.Font(file, size)
