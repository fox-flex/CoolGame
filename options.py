import pygame
from pygame import display

pygame.init()


def Settings():
    size = [700,520]

    screen = display.set_mode(size)
    pygame.display.set_caption('Settings')

    image1 = pygame.image.load('settings.jpg')
    pygame.display.set_icon(image1)
    
    fon_image = pygame.image.load('synfon.jpg')
    button_happy = pygame.image.load('happy.png')
    button_lucky = pygame.image.load('lucky.png')
    button_ulam = pygame.image.load('Ulam.png')
    button_easy = pygame.image.load('easy.png')
    button_medium = pygame.image.load('mediums.png')
    button_hard = pygame.image.load('hard.png')
    button_gal = pygame.image.load('galochka.png')
    button_ok = pygame.image.load('ok.png')
    button_regym = pygame.image.load('regym.png')
    button_level = pygame.image.load('emh.png')
    button_znak = pygame.image.load('znakpyt.png')

    dod_op_ul = pygame.image.load('options.png')
    button_znak = pygame.transform.scale(button_znak,(40,40))
    #startcordinates
    x = 100
    y = 50
    x_lev = 550-x
    #cordinates
    y_ulam = y + 100
    but_height = 40
    y_lucky = y_ulam + but_height + 60
    y_happy = y_lucky + but_height + 60
    
    run = True
    ulam = False
    lucky = False
    happy = False
    easy = False
    medium = False
    hard = False
    ulam_number = False
    happy_number = False
    lucky_number = False
    while run:
        screen.blit(fon_image, (0, 0))

        screen.blit(button_znak,(30,y_happy+5))
        screen.blit(button_znak,(30,y_lucky+5))
        screen.blit(button_znak,(30,y_ulam+3))
        screen.blit(button_regym,(x,y))
        screen.blit(button_ulam,(x,y+100))
        screen.blit(button_lucky,(x-10,y+200))
        screen.blit(button_happy,(x,y + 300))

        screen.blit(button_level,(x_lev,y))
        screen.blit(button_easy,(550-x,y+100))
        screen.blit(button_medium,(550-x,y+200))
        screen.blit(button_hard,(550-x,y+300))

        screen.blit(button_ok,(650,470))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position_mouse = pygame.mouse.get_pos()
                #regym
                if position_mouse[0] >= x and position_mouse[1] >= y_ulam:
                    if position_mouse[0] <= x + 150 and position_mouse[1] <= y_ulam + but_height:
                        ulam = True
                        lucky = False
                        happy = False
                if position_mouse[0] >= x and position_mouse[1] >= y_lucky:
                    if position_mouse[0]<= x + 130 and position_mouse[1] <= y_lucky + but_height:
                        ulam = False
                        lucky = True
                        happy = False
                if position_mouse[0] >= x and position_mouse[1] >= y_happy:
                    if position_mouse[0]<= x + 150 and position_mouse[1] <= y_happy + but_height:
                        ulam = False
                        lucky = False
                        happy = True
                #level
                if position_mouse[0] >= x_lev and position_mouse[1] >= y_ulam:
                    if position_mouse[0] <= x_lev + 95 and position_mouse[1] <= y_ulam + but_height:
                        easy = True
                        medium = False
                        hard = False
                if position_mouse[0] >= x_lev and position_mouse[1] >= y_lucky:
                    if position_mouse[0]<= x_lev + 120 and position_mouse[1] <= y_lucky + but_height:
                        easy = False
                        medium = True
                        hard = False
                if position_mouse[0] >= x_lev and position_mouse[1] >= y_happy:
                    if position_mouse[0]<= x_lev + 120 and position_mouse[1] <= y_happy + but_height:
                        easy = False
                        medium = False
                        hard = True     
                #dod_info
                if position_mouse[0] >= 30 and position_mouse[1] >= y_happy:
                    if position_mouse[0]<= 60 and position_mouse[1] <= y_happy + but_height:
                        happy_number = True
                if position_mouse[0] >= 30 and position_mouse[1] >= y_lucky:
                    if position_mouse[0]<= 60 and position_mouse[1] <= y_lucky + but_height:
                        lucky_number = True
                if position_mouse[0] >= 30 and position_mouse[1] >= y_ulam:
                    if position_mouse[0]<= 60 and position_mouse[1] <= y_ulam + but_height:
                        ulam_number = True
        if ulam:
            screen.blit(button_gal,(250,140))
        if lucky:
            screen.blit(button_gal,(250,250))
        if happy:
            screen.blit(button_gal,(250,350))
        if easy:
            screen.blit(button_gal,(570,145))
        if medium:
            screen.blit(button_gal,(570,245))
        if hard:
            screen.blit(button_gal,(570,345))
        pygame.display.update()
    pygame.quit()

Settings()