import pygame
pygame.init()


def game_intro():
    display_width = 1000
    display_height = 720
    white = (255, 255, 255)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Menu')
    clock = pygame.time.Clock()
    # pygame.mixer.music.load('audio/music_lol.mp3')
    # pygame.mixer.music.play()
    img_2 = pygame.image.load('images/earth_1234.jpg')
    go_img = pygame.transform.scale(pygame.image.load('images/go_button.png'), (200, 200))
    help_img = pygame.transform.scale(pygame.image.load('images/help_button.png'), (200, 200))
    set_img = pygame.transform.scale(pygame.image.load('images/PixelArt.png'), (250, 75))
    ach_img = pygame.transform.scale(pygame.image.load('images/AchButton.png'), (250, 75))
    don_img = pygame.transform.scale(pygame.image.load('images/DonButton.png'), (250, 75))
    x_intro = 0
    y_intro = 0
    largeText = pygame.font.SysFont('arial', 69)
    logotype = largeText.render("Asteroid Danger", True, white)
    normText = pygame.font.SysFont('arial', 20)
    text_1 = "       It is an asteroid rain      "
    story_1 = normText.render(text_1, True, white)
    text_2 = "It is a common thing,  asteroids burn up in the atmosphere"
    story_2 = normText.render(text_2, True, white)
    text_3 = "But 'Ulam', 'Lucky' and 'Even' rocks do not have time to burn out"
    story_3 = normText.render(text_3, True, white)
    text_4 = "  The task of the Superhero is to find and destroy them  "
    story_4 = normText.render(text_4, True, white)
    text_5 = "   If he fails to get rid of one of them, the planet will come to an end"
    story_5 = normText.render(text_5, True, white)
    run = True
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                # pygame.quit()
                # quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= display_width/7.5 and position[1] >= display_height/2:
                    if position[0] <= (display_width/7.5)+200 and position[1] <= (display_height/2)+200:
                        # on click go
                        run = False
                        game_field()
                        # pygame.quit()
                        # quit()

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
        # pygame.display.update()
        clock.tick(30)


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
