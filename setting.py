import pygame
import button


Black= (0,0,0)
White=(255,255,255)
Grey= (100, 100, 100)
Green=(0, 255,0 )
Yellow=(255, 255, 255)

Ancho= 800
Alto = 700

title= "wordle"
FPS=60

let_4_img= pygame.image.load("images/4 letras.png")
let_5_img= pygame.image.load("images/5 letras.png")
let_6_img= pygame.image.load("images/6 letras.png")
let_7_img= pygame.image.load("images/7 letras.png")
let_8_img= pygame.image.load("images/8 letras.png")

button_4= button.Button (300,75, let_4_img,1)
button_5= button.Button (300,175, let_5_img,1)
button_6= button.Button (300,275, let_6_img,1)
button_7= button.Button (300,375, let_7_img,1)
button_8= button.Button (300,475, let_8_img,1)

TILESIZE =80
GAPSIZE =15



