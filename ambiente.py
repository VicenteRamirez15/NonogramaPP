import pygame
from enum import Enum

class AmbienteEnum(Enum):
    pos_botones = []
    INVIERNO = "invierno"
    MONTAÑA = "montaña"
    PRADO = "prado"

class Ambiente:
    def __init__(self, tipo: AmbienteEnum, fondo, musica, niveles):
        self.tipo = tipo
        self.fondo = pygame.image.load(fondo)
        self.musica = musica
        self.niveles = niveles
        self.pos_botones = []

    def get_pos_botones(self):
        if self.tipo == AmbienteEnum.INVIERNO:
            return [
                (15, 470),
                (67, 525),
                (162, 502),
                (245, 540),
                (341, 510),
                (420, 540),
                (283, 455),
                (387, 464),
                (495, 483),
                (470, 510),
                (453, 330)
            ]

    def cargar_musica(self, volumen=0.1):  
        try:
            pygame.mixer.music.load(self.musica)
            pygame.mixer.music.set_volume(volumen)  
            pygame.mixer.music.play(-1)  
        except pygame.error as e:
            print(f"Error al cargar la música: {e}")

    def get_fondo(self):
        return self.fondo

    def get_niveles(self):
        return self.niveles
    
    def get_tipo(self):
        return self.tipo
    