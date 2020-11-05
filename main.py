import pygame
from random import randint
from time import sleep


pygame.init()
win = pygame.display.set_mode((1000, 720))
clock = pygame.time.Clock()

# statements
width = 40
height = 60
speed = 5
present_state = 0
score = 0
max_num = 100
regime = 'ulam'
lives = 3

# include graphic interface
bg = pygame.image.load("images/bg.jpg")
type_write = pygame.font.SysFont('PainterPersonalUseOnly-Br0w.ttf', 42)
meteor_img = []
for i in range(1, 11):
    meteor_img.append(pygame.image.load("images/meteor/meteor" + str(i)
                                        + ".png"))
flower_img = []
for i in range(1, 21):
    flower_img.append(pygame.image.load("images/flower/flower" + str(i)
                                        + ".png"))


meteors = []


def add_meteor():
    global meteors
    global max_num
    """
    new_meteor[0] -> number on meteor
    new_meteor[1] -> frame number
    new_meteor[2] -> coordinate on the X-axis
    new_meteor[3] -> coordinate on the Y-axis
    new_meteor[4] -> image of number on meteor
    """
    meteor_num = randint(1, max_num)
    meteors_num_txt = type_write.render(str(meteor_num), True, (100, 100, 150))
    meteors.append([meteor_num, 0, randint(100, 400), -80, meteors_num_txt])


heart_img = pygame.image.load('images/life.png')
heart_img = pygame.transform.scale(heart_img, (30, 30))
loss_sound = pygame.mixer.Sound('audio/loss.wav')


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
        pygame.mixer.Sound.play(loss_sound)
        # in production:
        game_over()
        return False
    else:
        return True


def game_over():
    sleep(2)
    pygame.quit()


def flower(meteor_num):
    global flower_img
    global win
    x = meteors[meteor_num][2]
    y = meteors[meteor_num][3]
    for i in range(10):
        for frame in range(20):
            win.blit(flower_img[frame], (x + 30, y + i * 10 + frame))
        pygame.display.update()


# function witch say that is number correct or not
def is_happy(num: int) -> bool:
    return True


def is_lucky(num: int) -> bool:
    return True


def is_ulam(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


def what_type_nums(regime):
    if regime == 'ulam':
        return is_ulam
    if regime == 'happy':
        return is_happy
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
    x = meteors[meteor_num][2]
    y = meteors[meteor_num][3]
    # print('on_fall_meteor')
    if is_correct(meteors[meteor_num][0]):
        game_over()
        del meteors[meteor_num]
    else:
        # print('now flower')
        flower(meteor_num)
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
    if len(meteors) < 2:
        add_meteor()
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
        else:
            win.blit(meteors[i][4], (x_cord + 57, y_cord + 85))
    pygame.display.update()


# body of game
run = True
while run:
    clock.tick(30)

    # update meteors
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if clicking is around meteor
            for i in range(len(meteors)):
                x = round(meteors[i][2])
                y = round(meteors[i][3])
                exit_cycle = False
                for d_x in range(45, 95):
                    for d_y in range(20, 123):
                        if event.pos == (x+d_x, y+d_y):
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
    for i in range(len(meteors)):
        x = meteors[i][2]
        y = meteors[i][3]
        meteors[i][2] = x
        meteors[i][3] = y
        keys = pygame.key.get_pressed()
        y += speed
        if y >= 530:
            on_fall_meteor(i, what_type_nums(regime))
            break
        else:
            meteors[i][2] = x
            meteors[i][3] = y

    speed = 5 + score / 10

    drawWindow()
    pygame.display.update()

pygame.quit()
