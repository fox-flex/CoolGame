import pygame
pygame.init()


def game_intro():
    intro = True
    display_width = 1000
    display_height = 720
    white = (255, 255, 255)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Menu')
    clock = pygame.time.Clock()
    pygame.mixer.music.load('music_lol.mp3')
    pygame.mixer.music.play()
    img_2 = pygame.image.load('earth_1234.jpg')
    go_img = pygame.transform.scale(pygame.image.load('go_button.png'), (200, 200))
    help_img = pygame.transform.scale(pygame.image.load('help_button.png'), (200, 200))
    set_img = pygame.transform.scale(pygame.image.load('PixelArt.png'), (250, 75))
    ach_img = pygame.transform.scale(pygame.image.load('AchButton.png'), (250, 75))
    don_img = pygame.transform.scale(pygame.image.load('DonButton.png'), (250, 75))
    x_intro = 0
    y_intro = 0
    largeText = pygame.font.SysFont('arial', 69)
    logotype = largeText.render("Asteroid Danger", True, white)
    normText = pygame.font.SysFont('arial', 20)
    text_1 = "   На  землю  падають  метеорити   "
    story_1 = normText.render(text_1, True, white)
    text_2 = "Це звичайне явище, зазвичай метеорити згорають в атмосфері"
    story_2 = normText.render(text_2, True, white)
    text_3 = "Але метеорити типів “Улам”, “Хеппі” та “Лакі” не встигають догоріти"
    story_3 = normText.render(text_3, True, white)
    text_4 = "Завдання Супергероя знайти та знищити метеорити цих типів"
    story_4 = normText.render(text_4, True, white)
    text_5 = "Якщо він не встигне позбутися одного з них, то планеті настане кінець"
    story_5 = normText.render(text_5, True, white)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= display_width/7.5 and position[1] >= display_height/2:
                    if position[0] <= (display_width/7.5)+200 and position[1] <= (display_height/2)+200:
                        pygame.quit()
                        quit()
                if position[0] >= display_width/3.3 and position[1] >= display_height/2:
                    if position[0] <= (display_width/3.3)+200 and position[1] <= (display_height/2)+200:
                        pygame.quit()
                        quit()
                if position[0] >= display_width/1.8 and position[1] >= display_height/2.2:
                    if position[0] <= (display_width/1.8)+250 and position[1] <= (display_height/2.2)+75:
                        pygame.quit()
                        quit()
                if position[0] >= display_width/1.8 and position[1] >= display_height/1.8:
                    if position[0] <= (display_width/1.8)+250 and position[1] <= (display_height/1.8)+75:
                        pygame.quit()
                        quit()
                if position[0] >= display_width/1.8 and position[1] >= display_height/1.49:
                    if position[0] <= (display_width/1.8)+250 and position[1] <= (display_height/1.49)+75:
                        pygame.quit()
                        quit()
        gameDisplay.blit(img_2, (x_intro, y_intro))
        gameDisplay.blit(logotype, ((display_width/3.5), (display_height/20)))
        gameDisplay.blit(story_1, ((display_width/2.7), (display_height/6)))
        gameDisplay.blit(story_2, ((display_width/4.4), (display_height/5)))
        gameDisplay.blit(story_3, ((display_width/4.8), (display_height/4.2)))
        gameDisplay.blit(story_4, ((display_width/4.2), (display_height/3.65)))
        gameDisplay.blit(story_5, ((display_width/5.3), (display_height/3.2)))
        gameDisplay.blit(go_img, ((display_width/7.5), (display_height/2)))
        gameDisplay.blit(help_img, ((display_width/3.3), (display_height/2)))
        gameDisplay.blit(set_img, ((display_width/1.8), (display_height/2.2)))
        gameDisplay.blit(ach_img, ((display_width/1.8), (display_height/1.8)))
        gameDisplay.blit(don_img, ((display_width/1.8), (display_height/1.49)))
        pygame.display.update()
        clock.tick(15)


crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    game_intro()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
