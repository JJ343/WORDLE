import pygame
import button
import random
from setting import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen =pygame.display.set_mode((Ancho,Alto))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.font= pygame.font.SysFont("arialblack", 40)
        self.number=0
        self.MARGIN_X=0
        self.MARGIN_Y=0
        self.create_word_list()
        self.word=""
    
    def create_word_list(self):
        with open("words_alpha.txt") as file:
            self.words_list =file.read().splitlines()
    def elegir_palabra(self):
        self.r=random.choice(self.words_list).upper()
        if len(self.r)!= self.number:
            self.elegir_palabra()
        self.word=self.r
       



    def new(self):
        self.text =""
        self.current_row=0
        self.tiles=[]
        self.flip=True
        self.not_enough_letters =False
        

    def create_tiles(self):
        for fila in range(6):
            self.tiles.append([])
            for col in range(self.number):
                self.tiles[fila].append(Tile((col*(TILESIZE+GAPSIZE))+self.MARGIN_X,(fila*(TILESIZE+GAPSIZE)+self.MARGIN_Y)))

    def draw_tiles(self):
        for fila in self.tiles:
            for tile in fila:
                tile.draw(self.screen)


    def draw_text(self, text, font, text_col, x, y):
        img= font.render(text,True,text_col)
        self.screen.blit(img,(x,y))

    def run(self):
        self.ejec=True
        self.menu=True
        
        while self.ejec:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            if self.menu == False:
                self.update()


    def update(self):
        self.add_letter()

    def add_letter(self):
        # empty all the letter in the current row
        for tile in self.tiles[self.current_row]:
            tile.letter = ""

        # add the letters typed to the current row
        for i, letter in enumerate(self.text):
            self.tiles[self.current_row][i].letter = letter
            self.tiles[self.current_row][i].create_font()
    def draw(self):
        
        self.screen.fill(Black)
        if self.menu==True:
            self.draw_text("Menu",self.font, White, 300, 15)
            if button_4.draw(self.screen):
                self.MARGIN_X=int((Ancho-(4*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=4
                self.menu=False
                self.create_tiles()
                self.elegir_palabra()
                
            if button_5.draw(self.screen):
                self.MARGIN_X=int((Ancho-(5*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=5
                self.menu=False
                self.create_tiles()
                self.elegir_palabra()
            if button_6.draw(self.screen):
                self.MARGIN_X=int((Ancho-(6*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=6
                self.menu=False
                self.create_tiles()
                self.elegir_palabra()
            if button_7.draw(self.screen):
                self.MARGIN_X=int((Ancho-(7*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=7
                self.menu=False
                self.create_tiles()
                self.elegir_palabra()
            if button_8.draw(self.screen):
                self.MARGIN_X=int((Ancho-(8*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=8
                self.menu=False
                self.create_tiles()
                self.elegir_palabra()
        else:
            self.draw_tiles()
            print(self.word)

        pygame.display.update()

    def row_animation(self):
        # row shaking if not enough letters is inputted
        self.not_enough_letters = True
        start_pos = self.tiles[0][0].x
        amount_move = 4
        move = 3
        screen_copy = self.screen.copy()
        screen_copy.fill(Black)
        for row in self.tiles:
            for tile in row:
                if row != self.tiles[self.current_row]:
                    tile.draw(screen_copy)

        while True:
            while self.tiles[self.current_row][0].x < start_pos + amount_move:
                self.screen.blit(screen_copy, (0, 0))
                for tile in self.tiles[self.current_row]:
                    tile.x += move
                    tile.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.flip()

            while self.tiles[self.current_row][0].x > start_pos - amount_move:
                self.screen.blit(screen_copy, (0, 0))
                for tile in self.tiles[self.current_row]:
                    tile.x -= move
                    tile.draw(self.screen)
                self.clock.tick(FPS)
                pygame.display.flip()

            amount_move -= 2
            if amount_move < 0:
                break



    def box_animation(self):
        # tile scale animation for every letter inserted
        for tile in self.tiles[self.current_row]:
            if tile.letter == "":
                screen_copy = self.screen.copy()
                for start, end, step in ((0, 6, 1), (0, -6, -1)):
                    for size in range(start, end, 2*step):
                        self.screen.blit(screen_copy, (0, 0))
                        tile.x -= size
                        tile.y -= size
                        tile.width += size * 2
                        tile.height += size * 2
                        surface = pygame.Surface((tile.width, tile.height))
                        surface.fill(Black)
                        self.screen.blit(surface, (tile.x, tile.y))
                        tile.draw(self.screen)
                        pygame.display.flip()
                        self.clock.tick(FPS)
                    self.add_letter()
                break
    
    def reveal_animation(self, tile, colour):
        # reveal colours animation when user input the whole word
        screen_copy = self.screen.copy()

        while True:
            surface = pygame.Surface((tile.width+5, tile.height+5 ))
            surface.fill(Black)
            screen_copy.blit(surface, (tile.x, tile.y))
            self.screen.blit(screen_copy, (0, 0))
            if self.flip:
                tile.y += 6
                tile.height -= 10
                tile.font_y += 4
                tile.font_height = max(tile.font_height - 8, 0)
            else:
                tile.colour = colour
                tile.y -= 6
                tile.height += 10
                tile.font_y -= 4
                tile.font_height = min(tile.font_height + 8, tile.font_size)
            if tile.font_height == 0:
                self.flip = False

            tile.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

            if tile.font_height == tile.font_size:
                self.flip = True
                break


