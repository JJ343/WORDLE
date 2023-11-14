import pygame
import button
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

    def new(self):
        self.word="AREPA"
        self.text =""
        self.current_row=0
        self.tiles=[]
        

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
            self.draw_text("Menu",self.font, White, 275, 15)
            if button_4.draw(self.screen):
                self.MARGIN_X=int((Ancho-(4*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=4
                self.menu=False
                self.create_tiles()
            if button_5.draw(self.screen):
                self.MARGIN_X=int((Ancho-(5*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=5
                self.menu=False
                self.create_tiles()
            if button_6.draw(self.screen):
                self.MARGIN_X=int((Ancho-(6*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=6
                self.menu=False
                self.create_tiles()
            if button_7.draw(self.screen):
                self.MARGIN_X=int((Ancho-(7*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=7
                self.menu=False
                self.create_tiles()
            if button_8.draw(self.screen):
                self.MARGIN_X=int((Ancho-(8*(TILESIZE+GAPSIZE)))/2)
                self.MARGIN_Y=int((Alto-(6*(TILESIZE+GAPSIZE)))/2)
                self.number=8
                self.menu=False
                self.create_tiles()
        else:
            self.draw_tiles()

        pygame.display.update()
    

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_RETURN:
                    if len(self.text)== self.number:
                        if self.text ==self.word or self.current_row +1 ==6:
                            #lose
                            if self.text!= self.word:
                                pass
                            #win
                            else:
                                pass
                            self.playing=False
                            break
                        self.current_row+=1
                        self.text=""
                    else:
                        #animaciones, en caso de falta de letras
                        pass

                elif event.key == pygame.K_BACKSPACE:
                    self.text =self.text[:-1]
                else:
                    if len(self.text)< self.number and event.unicode.isalpha():
                        self.text += event.unicode.upper()
game = Game()

while True:
    game.new()
    game.run()


