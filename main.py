import pygame
from pygame import display
from random import randint
from func import sieve_flavius, ulam, even

pygame.init()
win = pygame.display.set_mode((1000, 720))

# statements
width = 40
height = 60
speed = 5
present_state = 0
score = 0
min_num = 1
max_num = 32
regime = 'ulam'
lives = 3
run_field = True

meteors = []

heart_img = pygame.image.load('images/life.png')
heart_img = pygame.transform.scale(heart_img, (30, 30))
loss_sound = pygame.mixer.Sound('audio/loss.wav')


def game_field():
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((1000, 720))

    # statements
    global width
    global height
    global speed
    global score
    global min_num
    global max_num
    global regime
    global lives
    global run_field

    # include graphic interface
    bg = pygame.image.load("images/bg.jpg")
    type_write = pygame.font.SysFont('PainterPersonalUseOnly-Br0w.ttf', 42)
    meteor_img = []
    for i in range(1, 11):
        meteor_img.append(pygame.image.load("images/meteor/meteor" + str(i)
                                            + ".png"))
    # flower_img = []
    # for i in range(1, 21):
    #     flower_img.append(pygame.image.load("images/flower/flower" + str(i)
    #                                         + ".png"))

    global meteors

    def add_meteor():
        global meteors
        global min_num
        global max_num
        """
        new_meteor[0] -> number on meteor
        new_meteor[1] -> frame number
        new_meteor[2] -> coordinate on the X-axis
        new_meteor[3] -> coordinate on the Y-axis
        new_meteor[4] -> image of number on meteor
        """
        meteor_num = randint(min_num, max_num)
        meteors_num_txt = type_write.render(str(meteor_num), True,
                                            (100, 100, 150))
        meteors.append(
            [meteor_num, 0, randint(100, 400), -80, meteors_num_txt])

    global heart_img
    global heart_img
    global loss_sound

    def show_lives():
        global lives
        show = 0
        x = 20
        while show != lives:
            win.blit(heart_img, (x, 20))
            x += 40
            show += 1

    def check_lives():
        """
        After mistake check, if user has enough lives to continue.
        """
        global lives
        lives -= 1
        if lives == 0:
            return False
        else:
            return True


    # def flower(meteor_num):
    # global flower_img
    # global win
    # x = meteors[meteor_num][2]
    # y = meteors[meteor_num][3]
    # for i in range(10):
    #     for frame in range(20):
    #         win.blit(flower_img[frame], (x + 30, y + i * 10 + frame))
    #     pygame.display.update()
    # pass

    # function witch say that is number correct or not
    def is_even(num: int) -> bool:
        if num in even():
            return True
        else:
            return False

    def is_lucky(num: int) -> bool:
        if num in sieve_flavius():
            return True
        else:
            return False

    def is_ulam(num: int) -> bool:
        if num in ulam():
            return True
        else:
            return False

    def what_type_nums(regime):
        if regime == 'ulam':
            return is_ulam
        if regime == 'even':
            return is_even
        if regime == 'lucky':
            return is_lucky

    def on_click_meteor(meteor_num: int, is_correct):
        global score
        global meteors
        x = meteors[meteor_num][2]
        y = meteors[meteor_num][3]
        if is_correct(meteors[meteor_num][0]):
            del meteors[meteor_num]
            score += 1
        elif check_lives():
            del meteors[meteor_num]
        else:
            game_over()

    def on_fall_meteor(meteor_num: int, is_correct):
        global score
        global meteors
        if is_correct(meteors[meteor_num][0]):
            game_over()
            # del meteors[meteor_num]
        else:
            # print('now flower')
            # flower(meteor_num)
            del meteors[meteor_num]
            score += 1

    def drawWindow():
        global meteor_num
        global meteors
        global win
        win.blit(bg, (0, 0))

        # draw lives
        show_lives()

        # draw score
        score_img = type_write.render(str(score), True, (100, 80, 100))
        win.blit(score_img, (28, 60))

        # draw meteors
        for i in range(len(meteors)):
            meteor_num = meteors[i][0]
            x_cord = meteors[i][2]
            y_cord = meteors[i][3]

            # draw meteor
            meteors[i][1] = (meteors[i][1] + 1) % 10
            win.blit(meteor_img[meteors[i][1]], (x_cord, y_cord))
            # draw meteor's num
            if meteor_num < 10:
                win.blit(meteors[i][4], (x_cord + 65, y_cord + 85))
            elif meteor_num < 100:
                win.blit(meteors[i][4], (x_cord + 57, y_cord + 85))
            else:
                win.blit(meteors[i][4], (x_cord + 49, y_cord + 85))

        pygame.display.update()
        if len(meteors) < 2:
            add_meteor()

    # body of game
    # run = True
    while run_field:
        clock.tick(30)

        # update meteors
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_field = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check if clicking is around meteor
                for i in range(len(meteors)):
                    x = round(meteors[i][2])
                    y = round(meteors[i][3])
                    exit_cycle = False
                    for d_x in range(45, 95):
                        for d_y in range(20, 123):
                            if event.pos == (x + d_x, y + d_y):
                                on_click_meteor(i, what_type_nums(regime))
                                pygame.display.update()
                                exit_cycle = True
                                break
                        if exit_cycle:
                            break
                    if exit_cycle:
                        break
                    meteors[i][2] = x
                    meteors[i][3] = y
        if not run_field:
            break
        for i in range(len(meteors)):
            x = meteors[i][2]
            y = meteors[i][3]
            meteors[i][2] = x
            meteors[i][3] = y
            y += speed
            if y >= 530:
                on_fall_meteor(i, what_type_nums(regime))
                break
            else:
                meteors[i][2] = x
                meteors[i][3] = y
        if not run_field:
            break

        speed = 5 + score / 10

        drawWindow()
        pygame.display.update()


def game_over():
    pygame.mixer.Sound.play(loss_sound)
    global run_field
    global win
    global meteors
    global lives
    global score

    run_field = False
    meteors = []
    lives = 3
    score = 0
    del win
    win = pygame.display.set_mode((1000, 720))

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

    funct = None
    contin = True
    run_over = True
    while run_over:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_over = False
                contin = False
                break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    # open run game function
                    run_over = False
                    run_field = True
                    funct = game_field
                    # game_field()
                elif event.key == pygame.K_m:
                    # open menu function
                    run_over = False
                    funct = game_intro
                    # game_intro()
        # pygame.display.update()
    if contin:
        funct()


def Settings():
    global win
    del win
    size = [700, 520]

    screen = display.set_mode(size)
    pygame.display.set_caption('Settings')

    image1 = pygame.image.load('images/options/settings.jpg')
    pygame.display.set_icon(image1)

    fon_image = pygame.image.load('images/options/synfon.jpg')
    button_happy = pygame.image.load('images/options/happy.png')
    button_lucky = pygame.image.load('images/options/lucky.png')
    button_ulam = pygame.image.load('images/options/Ulam.png')
    button_easy = pygame.image.load('images/options/easy.png')
    button_medium = pygame.image.load('images/options/mediums.png')
    button_hard = pygame.image.load('images/options/hard.png')
    button_gal = pygame.image.load('images/options/galochka.png')
    button_ok = pygame.image.load('images/options/ok.png')
    button_regym = pygame.image.load('images/options/regym.png')
    button_level = pygame.image.load('images/options/emh.png')
    button_znak = pygame.image.load('images/options/znakpyt.png')

    # dod_op_ul = pygame.image.load('images/options/options.png')
    button_znak = pygame.transform.scale(button_znak, (40, 40))
    # startcordinates
    x = 100
    y = 50
    x_lev = 550 - x
    # cordinates
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
    ok_button = False
    while run:
        screen.blit(fon_image, (0, 0))

        screen.blit(button_znak, (30, y_happy + 5))
        screen.blit(button_znak, (30, y_lucky + 5))
        screen.blit(button_znak, (30, y_ulam + 3))
        screen.blit(button_regym, (x, y))
        screen.blit(button_ulam, (x, y + 100))
        screen.blit(button_lucky, (x - 10, y + 200))
        screen.blit(button_happy, (x, y + 300))

        screen.blit(button_level, (x_lev, y))
        screen.blit(button_easy, (550 - x, y + 100))
        screen.blit(button_medium, (550 - x, y + 200))
        screen.blit(button_hard, (550 - x, y + 300))

        screen.blit(button_ok, (650, 470))

        # dodinfo_ulam
        font = pygame.font.SysFont('Comic Sans MS', 21)
        follow = font.render(
            'Стандартна послідовність Уляма(або (1, 2)-числа Уляма)', 1,
            (255, 0, 0))
        follow1 = font.render(
            'починається з U1 = 1 и U2 = 2.При n > 2, Un визначається', 1,
            (255, 0, 0))
        follow2 = font.render(
            'як найменше ціле число більше за Un-1, яке єдиним чином ', 1,
            (255, 0, 0))
        follow3 = font.render(
            'розкладається в суму двох різних попередніх членів послідовності.',
            1, (255, 0, 0))
        # dodinfo_lucky
        follow_l = font.render(
            'Щасливе число - це натуральне число в наборі, яке', 1,
            (255, 0, 0))
        follow1_l = font.render(
            'генерується певним "ситом". Це сито схоже на сито Ератосфена,', 1,
            (255, 0, 0))
        follow2_l = font.render(
            'яке генерує прості числа, але воно виключає числа на основі', 1,
            (255, 0, 0))
        follow3_l = font.render(
            'їх положення в решті набору, а не їх значення (або положення', 1,
            (255, 0, 0))
        follow4_l = font.render(' початковому наборі натуральних чисел)', 1,
                                (255, 0, 0))
        # dodinfo_happy
        follow_h = font.render(
            'Натуральне число називається щасливим числом, якщо ', 1,
            (255, 0, 0))
        follow1_h = font.render(
            'послідовність, яка починається з цього числа, і кожен', 1,
            (255, 0, 0))
        follow2_h = font.render(
            'наступний член якої є сумою квадратів цифр попереднього,', 1,
            (255, 0, 0))
        follow3_h = font.render('містить член рівний одиниці.', 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position_mouse = pygame.mouse.get_pos()
                # regime
                if position_mouse[0] >= x and position_mouse[1] >= y_ulam:
                    if position_mouse[0] <= x + 150 and position_mouse[1] <= y_ulam + but_height:
                        ulam = True
                        lucky = False
                        happy = False
                if position_mouse[0] >= x and position_mouse[1] >= y_lucky:
                    if position_mouse[0] <= x + 130 and position_mouse[1] <= y_lucky + but_height:
                        ulam = False
                        lucky = True
                        happy = False
                if position_mouse[0] >= x and position_mouse[1] >= y_happy:
                    if position_mouse[0] <= x + 150 and position_mouse[1] <= y_happy + but_height:
                        ulam = False
                        lucky = False
                        happy = True
                # level
                if position_mouse[0] >= x_lev and position_mouse[1] >= y_ulam:
                    if position_mouse[0] <= x_lev + 95 and position_mouse[1] <= y_ulam + but_height:
                        easy = True
                        medium = False
                        hard = False
                if position_mouse[0] >= x_lev and position_mouse[1] >= y_lucky:
                    if position_mouse[0] <= x_lev + 120 and position_mouse[1] <= y_lucky + but_height:
                        easy = False
                        medium = True
                        hard = False
                if position_mouse[0] >= x_lev and position_mouse[1] >= y_happy:
                    if position_mouse[0] <= x_lev + 120 and position_mouse[1] <= y_happy + but_height:
                        easy = False
                        medium = False
                        hard = True
                        # dod_info
                if position_mouse[0] >= 30 and position_mouse[1] >= y_happy:
                    if position_mouse[0] <= 60 and position_mouse[1] <= y_happy + but_height:
                        happy_number = True
                if position_mouse[0] >= 30 and position_mouse[1] >= y_lucky:
                    if position_mouse[0] <= 60 and position_mouse[1] <= y_lucky + but_height:
                        lucky_number = True
                if position_mouse[0] >= 30 and position_mouse[1] >= y_ulam:
                    if position_mouse[0] <= 60 and position_mouse[1] <= y_ulam + but_height:
                        ulam_number = True
                if position_mouse[0] >= 310 and position_mouse[1] >= 470:
                    if position_mouse[0] <= 350 and position_mouse[1] <= 520:
                        ulam_number = False
                        happy_number = False
                        lucky_number = False
                # ok
                if position_mouse[0] >= 650 and position_mouse[1] >= 470:
                    if position_mouse[0] <= 700 and position_mouse[1] <= 520:
                        ok_button = True
        global regime
        global min_num
        global max_num
        if ulam:
            screen.blit(button_gal, (250, 140))
            regime = 'ulam'
        if lucky:
            screen.blit(button_gal, (250, 250))
            regime = 'ulam'
        if happy:
            screen.blit(button_gal, (250, 350))
            regime = 'ulam'
        if easy:
            screen.blit(button_gal, (570, 145))
            min_num = 1
            max_num = 32
        if medium:
            screen.blit(button_gal, (570, 245))
            min_num = 33
            max_num = 64
        if hard:
            screen.blit(button_gal, (570, 345))
            min_num = 65
            max_num = 128
        if ulam_number:
            screen.blit(fon_image, (0, 0))
            screen.blit(fon_image, (0, 0))
            screen.blit(button_ok, (310, 470))
            screen.blit(follow, (0, 0))
            screen.blit(follow1, (0, 30))
            screen.blit(follow2, (0, 60))
            screen.blit(follow3, (0, 90))
        if lucky_number:
            screen.blit(fon_image, (0, 0))
            screen.blit(button_ok, (310, 470))
            screen.blit(follow_l, (0, 0))
            screen.blit(follow1_l, (0, 30))
            screen.blit(follow2_l, (0, 60))
            screen.blit(follow3_l, (0, 90))
            screen.blit(follow4_l, (0, 120))
        if happy_number:
            screen.blit(fon_image, (0, 0))
            screen.blit(button_ok, (310, 470))
            screen.blit(follow_h, (0, 0))
            screen.blit(follow1_h, (0, 30))
            screen.blit(follow2_h, (0, 60))
            screen.blit(follow3, (0, 90))
        if ok_button:
            run = False
            win = pygame.display.set_mode((1000, 720))
        pygame.display.update()
        if ok_button:
            game_intro()


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
    run_intro = True
    while run_intro:
        pygame.display.update()
        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.QUIT:
                # pygame.quit()
                # quit()
                run_intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                if position[0] >= display_width/7.5 and position[1] >= display_height/2:
                    if position[0] <= (display_width/7.5)+200 and position[1] <= (display_height/2)+200:
                        # on click go
                        run_intro = False
                        global run_field
                        run_field = True
                        game_field()
                if position[0] >= display_width/3.3 and position[1] >= display_height/2:
                    if position[0] <= (display_width/3.3)+200 and position[1] <= (display_height/2)+200:
                        # on click help
                        pygame.mixer.Sound.play(loss_sound)
                        # pygame.quit()
                        # quit()
                if position[0] >= display_width/1.8 and position[1] >= display_height/2.2:
                    if position[0] <= (display_width/1.8)+250 and position[1] <= (display_height/2.2)+75:
                        # on click settings
                        Settings()
                        pygame.quit()
                        quit()
                if position[0] >= display_width/1.8 and position[1] >= display_height/1.8:
                    if position[0] <= (display_width/1.8)+250 and position[1] <= (display_height/1.8)+75:
                        # on click achievements
                        pygame.mixer.Sound.play(loss_sound)
                        # pygame.quit()
                        # quit()
                if position[0] >= display_width/1.8 and position[1] >= display_height/1.49:
                    if position[0] <= (display_width/1.8)+250 and position[1] <= (display_height/1.49)+75:
                        # on click donations
                        pygame.mixer.Sound.play(loss_sound)
                        # pygame.quit()
                        # quit()
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


game_intro()
