import pygame
from pygame import *
import time


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = pygame.image.load(r'resources\board.png').convert_alpha()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.board, (0, 0))
        pygame.display.flip()


class Knight:
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.B = pygame.image.load('resources/knight_b.png').convert_alpha()
        self.W = pygame.image.load('resources/knight_w.png').convert_alpha()
        self.color = color
        self.x = (x-1) * 60
        self.y = (y-1) * 60

    def draw(self):
        if self.color == 'b':
            self.screen.blit(self.B, (self.x, self.y))
        if self.color == 'w':
            self.screen.blit(self.W, (self.x, self.y))
        pygame.display.flip()


class Pawn:
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.B = pygame.image.load('resources/pawn_b.png').convert_alpha()
        self.W = pygame.image.load('resources/pawn_w.png').convert_alpha()
        self.color = color
        self.x = (x-1) * 60
        self.y = (y-1) * 60

    def draw(self):
        if self.color == 'b':
            self.screen.blit(self.B, (self.x, self.y))
        if self.color == 'w':
            self.screen.blit(self.W, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((700, 485))
        self.board = Board(self.surface)
        self.wqk = Knight(self.surface, 'w', 2, 8)
        self.wAp = Pawn(self.surface, 'w', 1, 7)
        self.wBp = Pawn(self.surface, 'w', 2, 7)
        self.wCp = Pawn(self.surface, 'w', 3, 7)
        self.wDp = Pawn(self.surface, 'w', 4, 7)
        self.wEp = Pawn(self.surface, 'w', 5, 7)
        self.wFp = Pawn(self.surface, 'w', 6, 7)
        self.wGp = Pawn(self.surface, 'w', 7, 7)
        self.wHp = Pawn(self.surface, 'w', 8, 7)


    def draw_all(self):
        self.wAp.draw()
        self.wBp.draw()
        self.wCp.draw()
        self.wDp.draw()
        self.wEp.draw()
        self.wFp.draw()
        self.wGp.draw()
        self.wHp.draw()


    def run(self):
        self.board.draw()
        self.wqk.draw()
        self.draw_all()



if __name__ == '__main__':
    game = Game()
    game.run()
    time.sleep(5)
