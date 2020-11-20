import pygame
from pygame import draw
from pygame import display
from pygame import mixer
import sys

pygame.init()

def help_window():
    size = [1000,720]
    screen = display.set_mode(size)
    display.set_caption("Help")
    display.set_icon(pygame.image.load("images/help/help.png"))
    
    clock = pygame.time.Clock()
    fps  = 60
        
    x = 880
    y = 600
    image_ok_global = pygame.image.load("images/help/ok.png")
    image_ok = pygame.transform.scale(image_ok_global, (110, 110))

    # mixer.music.load("images/audio/music.mp3")
    # mixer.music.play()


    image_global = pygame.image.load("images/help/asteroid.jpg")
    image = pygame.transform.scale(image_global, (size))

    font = pygame.font.SysFont("arial", 20)
    text1 = font.render("Hello. The rules of the game are as follows:", True, (255,255,255))
    text2 = font.render("1. You have 3 lives", True, (255,255,255))
    text3 = font.render("2. You have to catch meteorites with the numbers you choose", True, (255,255,255))
    text4 = font.render("3. To catch, left-click on the meteorite", True, (255,255,255))
    text5 = font.render("4. If not guessed, the planet explodes, if a meteorite with the correct number falls to earth, it also explodes", True, (255,255,255))
    text6 = font.render("5. each correct answer +1 point", True, (255,255,255))
    run = True
    while run:
        screen.blit(image, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= x and position[1] >= y:
                    if position[0] <= x + 110 and position[1] <= y + 110:
                        run = False
        screen.blit(text1, (0,0))
        screen.blit(text2, (0,30))
        screen.blit(text3, (0,60))
        screen.blit(text4, (0,90))
        screen.blit(text5, (0,120))
        screen.blit(text6, (0,150))
        screen.blit(image_ok, (x,y))
        clock.tick(fps)
        display.update()
        

help_window()