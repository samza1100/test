import pygame
from constants import *

class Cell: # started the cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.width = SQUARE_SIZE
        self.height = SQUARE_SIZE
        self.selected = False
        self.sketched_value = 0
        self.user_edit = value == 0
    def set_cell_value(self, value):
        self.user_edit = True
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        # These are center coordinates
        x = self.width//2+self.width*self.col
        y = self.height//2+self.height*self.row
        if self.value > 0:
            num_font = pygame.font.Font(None, 100)
            num_surf = num_font.render(str(self.value), 0, BLUE)
            num_rect = num_surf.get_rect(center=(x, y))
            self.screen.blit(num_surf, num_rect)
        elif self.sketched_value != None and self.sketched_value > 0:
            num_font = pygame.font.Font(None, 50)
            num_surf = num_font.render(str(self.sketched_value), 0, BLUE)
            num_rect = num_surf.get_rect(center=(x-self.width//4, y-self.height//4))
            self.screen.blit(num_surf, num_rect)
        color = BLACK
        line_width = 2
        if self.selected:
            color = RED
            line_width = 5
        # Shifting coordinates to reach top left of square
        pygame.draw.rect(self.screen, color, (x-self.width//2,y-self.height//2, self.width, self.height), line_width)



