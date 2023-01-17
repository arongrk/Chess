import pygame
from pygame import *
import time


def plist(screen, c):
    if c == 'w':
        return [Pawn(screen, c, i, 7) for i in range(1, 9)]
    if c == 'b':
        return [Pawn(screen, c, i, 2) for i in range(1, 9)]


def draw_figure(images, x, y, c, screen):
    if c == 'b':
        screen.blit(images[1], (x, y))
    if c == 'w':
        screen.blit(images[0], (x, y))
    pygame.display.flip()


class Board:
    def __init__(self, screen):
        self.screen = screen
        self.board = pygame.image.load(r'resources\board.png').convert_alpha()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.board, (0, 0))
        pygame.display.flip()


class Pawn:
    def __init__(self, screen, c, x, y):
        self.screen = screen
        self.B = pygame.image.load('resources/pawn_b.png').convert_alpha()
        self.W = pygame.image.load('resources/pawn_w.png').convert_alpha()
        self.color = c
        self.x = (x-1) * 60
        self.y = (y-1) * 60

    def draw(self):
        if self.color == 'b':
            self.screen.blit(self.B, (self.x, self.y))
        if self.color == 'w':
            self.screen.blit(self.W, (self.x, self.y))
        pygame.display.flip()


class Bishop:
    def __init__(self, screen, c, x, y):
        self.screen = screen
        self.B = pygame.image.load('resources/bishop_b.png').convert_alpha()
        self.W = pygame.image.load('resources/bishop_w.png').convert_alpha()
        self.color = c
        self.x = (x-1) * 60
        self.y = (y-1) * 60


    def draw(self):
        draw_figure([self.W, self.B], self.x, self.y, self.color, self.screen)


class Knight:
    def __init__(self, screen, c, x, y):
        self.screen = screen
        self.B = pygame.image.load('resources/knight_b.png').convert_alpha()
        self.W = pygame.image.load('resources/knight_w.png').convert_alpha()
        self.color = c
        self.x = (x-1) * 60
        self.y = (y-1) * 60

    def draw(self):
        draw_figure([self.W, self.B], self.x, self.y, self.color, self.screen)


class Game:
    surface = pygame.display.set_mode((700, 480))
    board = Board(surface)
    def __init__(self):
        self.wPawns = self.wA, self.wB, self.wC, self.wD, self.wE, self.wF, self.wG, self.wH = plist(self.surface, 'w')
        self.wKnights = self.wQk, self.wKk = [Knight(self.surface, 'w', i, 8) for i in [2, 7]]
        self.wBishops = self.wQb, self.wKb = [Bishop(self.surface, 'w', i, 8) for i in [3, 6]]
        self.wRooks = 0
        self.wQueen = 0
        self.wKing = 0
        self.wFigures = self.wPawns + self.wBishops + self.wKnights # + self.wRooks + self.wQueen + self.wKing
        self.bPawns = self.bA, self.bB, self.bC, self.bD, self.bE, self.bF, self.bG, self.bH = plist(self.surface, 'b')
        self.bKnights = self.bQk, self.bKk = [Knight(self.surface, 'b', i, 1) for i in [2, 7]]
        self.bBishops = self.bQb, self.bKb = [Bishop(self.surface, 'b', i, 1) for i in [3, 6]]
        self.bRooks = 0
        self.bQueen = 0
        self.bKing = 0
        self.bFigures = self.bPawns + self.bBishops + self.bKnights # + self.bRooks + self.bQueen + self.bKing

    def draw_all(self):
        for i in self.wFigures + self.bFigures:
            i.draw()

    def run(self):
        self.board.draw()
        self.draw_all()



if __name__ == '__main__':
    game = Game()
    gamer = Game()
    game.run()
    time.sleep(5)
