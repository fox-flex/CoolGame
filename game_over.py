import pygame
pygame.init()

def game_over():
    display_width = 1000
    display_height = 720
    go_bckgr = pygame.image.load('earth_1234.jpg')

    over_font_1 = pygame.font.SysFont('arial', 69)
    over_font_2 = pygame.font.SysFont('arial', 20)

    over_text_1 = over_font_1.render('GAME OVER', True, (255,255,255))
    over_text_2 = over_font_2.render('Press SPACE to restart,press M to return to menu')

    display.blit(go_bckgr, (0,0))
    display.blit(over_text_1, ((display_width/2), (display_height/3)))
    display.blit(over_text_2, ((display_width/4), (display_height/2)))

    display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                #open run game function
                pass
            elif event.key == pygame.K_m:
                #open menu function
                pass
