import pygame
from pygame import display

pygame.init()

def ulam_num():
    size = [700,220]

    font = pygame.font.SysFont('Comic Sans MS', 21)
    follow = font.render('Стандартна послідовність Уляма(або (1, 2)-числа Уляма)',1,(255,0,0))
    follow1 = font.render('починається з U1 = 1 и U2 = 2.При n > 2, Un визначається',1,(255,0,0))
    follow2 = font.render('як найменше ціле число більше за Un-1, яке єдиним чином ',1,(255,0,0))
    follow3 = font.render('розкладається в суму двох різних попередніх членів послідовності.',1,(255,0,0))

    screen = win.set_mode(size)
    pygame.display.set_caption('Ulam')
    fon_image = pygame.image.load('synfon.jpg')
    button_ok = pygame.image.load('ok.png')

    run = True
    while run:
        screen.blit(fon_image, (0, 0))
        screen.blit(button_ok,(650,170))
        screen.blit(follow,(0,0))
        screen.blit(follow1,(0,30))
        screen.blit(follow2,(0,60))
        screen.blit(follow3,(0,90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= 650 and position[1] >= 170:
                    run = False
        pygame.display.update()
    pygame.quit()

def happy_num():
    size = [700,220]

    font = pygame.font.SysFont('Comic Sans MS', 21)
    follow = font.render('Натуральне число називається щасливим числом, якщо ',1,(255,0,0))
    follow1 = font.render('послідовність, яка починається з цього числа, і кожен',1,(255,0,0))
    follow2 = font.render('наступний член якої є сумою квадратів цифр попереднього,',1,(255,0,0))
    follow3 = font.render('містить член рівний одиниці.',1,(255,0,0))

    screen = win.set_mode(size)
    pygame.display.set_caption('Happy')
    fon_image = pygame.image.load('synfon.jpg')
    button_ok = pygame.image.load('ok.png')

    run = True
    while run:
        screen.blit(fon_image, (0, 0))
        screen.blit(button_ok,(650,170))
        screen.blit(follow,(0,0))
        screen.blit(follow1,(0,30))
        screen.blit(follow2,(0,60))
        screen.blit(follow3,(0,90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= 650 and position[1] >= 170:
                    run = False
        pygame.display.update()
    pygame.quit()

def lucky_num():
    size = [700,220]

    font = pygame.font.SysFont('Comic Sans MS', 21)
    follow = font.render('Натуральне число називається щасливим числом, якщо ',1,(255,0,0))
    follow1 = font.render('послідовність, яка починається з цього числа, і кожен',1,(255,0,0))
    follow2 = font.render('наступний член якої є сумою квадратів цифр попереднього,',1,(255,0,0))
    follow3 = font.render('містить член рівний одиниці.',1,(255,0,0))

    screen = win.set_mode(size)
    pygame.display.set_caption('Lucky')
    fon_image = pygame.image.load('synfon.jpg')
    button_ok = pygame.image.load('ok.png')

    run = True
    while run:
        screen.blit(fon_image, (0, 0))
        screen.blit(button_ok,(650,170))
        screen.blit(follow,(0,0))
        screen.blit(follow1,(0,30))
        screen.blit(follow2,(0,60))
        screen.blit(follow3,(0,90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= 650 and position[1] >= 170:
                    run = False
        pygame.display.update()
    pygame.quit()
ulam_num()