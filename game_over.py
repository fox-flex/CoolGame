import pygame
import game_field

pygame.init()


run = True
win = pygame.display.set_mode((1000, 720))
meteors = []
lives = 3


def game_over():
    global run
    global win
    global meteors
    global lives
    display_width = 1000
    display_height = 720
    go_bckgr = pygame.image.load('images/earth_1234.jpg')

    over_font_1 = pygame.font.SysFont('arial', 69)
    over_font_2 = pygame.font.SysFont('arial', 20)

    over_text_1 = over_font_1.render('GAME OVER', True, (255, 255, 255))
    over_text_2 = over_font_2.render(
        'Press SPACE to restart,press M to return to menu', True,
        (255, 255, 255))

    win.blit(go_bckgr, (0, 0))
    win.blit(over_text_1, ((display_width / 2), (display_height / 3)))
    win.blit(over_text_2, ((display_width / 4), (display_height / 2)))

    pygame.display.update()

    run0 = True
    while run0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run0 = False
                break
                # pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    # open run game function
                    run0 = False
                    run = False
                    meteors = []
                    lives = 3

                    game_field.game_field()
                elif event.key == pygame.K_m:
                    # open menu function
                    run0 = False
                    run = False
    pygame.display.update()


game_over()
