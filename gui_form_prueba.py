import pygame
from pygame.locals import *
from gui_button import *
from gui_slider import *
from gui_textbox import *
from gui_label import *
from gui_form import * 

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        self._slave = pygame.Surface((w,h))
        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()


        pygame.mixer.music.load("images\music\\01-Level1.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def render(self):
        self._slave.fill(self.color_background)