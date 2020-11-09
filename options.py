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

        #dodinfo_ulam
        font = pygame.font.SysFont('Comic Sans MS', 21)
        follow = font.render('Стандартна послідовність Уляма(або (1, 2)-числа Уляма)',1,(255,0,0))
        follow1 = font.render('починається з U1 = 1 и U2 = 2.При n > 2, Un визначається',1,(255,0,0))
        follow2 = font.render('як найменше ціле число більше за Un-1, яке єдиним чином ',1,(255,0,0))
        follow3 = font.render('розкладається в суму двох різних попередніх членів послідовності.',1,(255,0,0))
        #dodinfo_lucky
        follow_l = font.render('Щасливе число - це натуральне число в наборі, яке',1,(255,0,0))
        follow1_l = font.render('генерується певним "ситом". Це сито схоже на сито Ератосфена,',1,(255,0,0))
        follow2_l = font.render('яке генерує прості числа, але воно виключає числа на основі',1,(255,0,0))
        follow3_l = font.render('їх положення в решті набору, а не їх значення (або положення',1,(255,0,0))
        follow4_l = font.render(' початковому наборі натуральних чисел)',1,(255,0,0))
        #dodinfo_happy
        follow_h = font.render('Натуральне число називається щасливим числом, якщо ',1,(255,0,0))
        follow1_h = font.render('послідовність, яка починається з цього числа, і кожен',1,(255,0,0))
        follow2_h = font.render('наступний член якої є сумою квадратів цифр попереднього,',1,(255,0,0))
        follow3_h = font.render('містить член рівний одиниці.',1,(255,0,0))
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
                if position_mouse[0] >= 310 and position_mouse[1] >= 470:
                    if position_mouse[0]<= 350 and position_mouse[1] <= 520:
                        ulam_number = False
                        happy_number = False
                        lucky_number = False
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
        if ulam_number:
            screen.blit(fon_image,(0,0))
            screen.blit(fon_image, (0, 0))
            screen.blit(button_ok,(310,470))
            screen.blit(follow,(0,0))
            screen.blit(follow1,(0,30))
            screen.blit(follow2,(0,60))
            screen.blit(follow3,(0,90))
        if lucky_number:
            screen.blit(fon_image, (0, 0))
            screen.blit(button_ok,(310,470))
            screen.blit(follow_l,(0,0))
            screen.blit(follow1_l,(0,30))
            screen.blit(follow2_l,(0,60))
            screen.blit(follow3_l,(0,90))
            screen.blit(follow4_l,(0,120))
        if happy_number:
            screen.blit(fon_image, (0, 0))
            screen.blit(button_ok,(310,470))
            screen.blit(follow_h,(0,0))
            screen.blit(follow1_h,(0,30))
            screen.blit(follow2_h,(0,60))
            screen.blit(follow3,(0,90))    
        pygame.display.update()
    pygame.quit()

Settings()
