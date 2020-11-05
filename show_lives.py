import pygame
pygame.init()

heart_img = pygame.image.load('images/life.png')
heart_img = pygame.transform.scale(heart_img, (30,30))

lives = 3

def show_lives():
    global lives
    show = 0
    x = 20
    while show != lives:
        display.blit(heart_img, (x,20))
        x += 40
        show += 1