import pygame
import random

pygame.init()

score_y = 20
score_x = 220
score_int = 0


def score(score):
    score_text = font.render(str(score), True, black)
    win.blit(score_text, [score_x, score_y])


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

win = pygame.display.set_mode((500, 800))

pygame.display.set_caption("Color Rain")

listValue = 0

walkRight = [pygame.image.load('1_B.png'), pygame.image.load('2_B.png'), pygame.image.load('3_B.png'),
             pygame.image.load('4_B.png'), pygame.image.load('5_B.png'), pygame.image.load('6_B.png'),
             pygame.image.load('7_B.png'), pygame.image.load('8_B.png'), pygame.image.load('9_B.png')]
walkLeft = [pygame.image.load('9_B.png'), pygame.image.load('8_B.png'), pygame.image.load('7_B.png'),
            pygame.image.load('6_B.png'), pygame.image.load('5_B.png'), pygame.image.load('4_B.png'),
            pygame.image.load('3_B.png'), pygame.image.load('2_B.png'), pygame.image.load('1_B.png')]
still_ball = pygame.image.load('0_B.png')
homebg = [pygame.image.load('Home_red.png'), pygame.image.load('Home_green.png'), pygame.image.load('Home_yellow.png'),
          pygame.image.load('Home_blue.png')]
playbg = [pygame.image.load('50p_yellow.png'), pygame.image.load('50p_green.png'), pygame.image.load('50p_red.png'),
          pygame.image.load('50p_blue.png')]
gameoverbg = [pygame.image.load('Yellow_Background.png'), pygame.image.load('Green_Background.png'),
              pygame.image.load('Red_Background.png'), pygame.image.load('Blue_Background.png')]
pixelpos = [pygame.image.load('50p_yellow.png'), pygame.image.load('100p_yellow.png'),
            pygame.image.load('150p_yellow.png'), pygame.image.load('200p_yellow.png'),
            pygame.image.load('250p_yellow.png'), pygame.image.load('300p_yellow.png'),
            pygame.image.load('350p_yellow.png'), pygame.image.load('400p_yellow.png'),
            pygame.image.load('450p_yellow.png'), pygame.image.load('500p_yellow.png')]

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 80)

text_x = 130
text_y = 230


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [text_x, text_y])


ball_x = 200
ball_y = 700
ball_width = 60
ball_height = 60
ball_vel = 13
ball_left = False
ball_right = False
ball_walkCount = 0

colors = [green, red, yellow, blue]
rain_x_pos_1 = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
rain_y_pos_1 = [20, -20, -60, -100, -140, -200, -260, -300]

rain_y = 20
rain_vel = 20
rain_width = 0
rain_radius = 10


def drawball():
    global ball_walkCount

    if ball_walkCount + 1 >= 27:
        ball_walkCount = 0

    if ball_left:
        win.blit(walkLeft[ball_walkCount // 3], (ball_x, ball_y))
        ball_walkCount += 1
    elif ball_right:
        win.blit(walkRight[ball_walkCount // 3], (ball_x, ball_y))
        ball_walkCount += 1
    else:
        win.blit(still_ball, (ball_x, ball_y))

    pygame.display.update()


gameExit = False
gameOver = False
homeScreen = True

rain_y = random.choice(rain_y_pos_1)
rain_color = random.choice(colors)
rain_x = random.choice(rain_x_pos_1)

while not gameExit:
    clock.tick(27)
    random_homebg = random.choice(homebg)
    random_gameoverbg = random.choice(gameoverbg)

    while homeScreen:
        random_playbg = random.choice(playbg)
        win.blit(random_homebg, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                homeScreen = False
                gameOver = False
                gameExit = False
                score_int = 0
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
                homeScreen = False
                score_int = 0
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_q:
                    gameExit = True
                    gameOver = False
                    homeScreen = False
                    score_int = 0

    screenDisplay = win.blit(pixelpos[listValue], (0, 0))
    score(score_int)
    pygame.display.update()
    if rain_y >= 750:
        rain_y = random.choice(rain_y_pos_1)
        rain_color = random.choice(colors)
        rain_x = random.choice(rain_x_pos_1)

    pygame.draw.circle(win, rain_color, [rain_x, rain_y], rain_radius, rain_width)
    drawball()
    pygame.display.update()

    if rain_y >= 740 and rain_x >= ball_x and rain_x < (ball_x + ball_width):
        if rain_color == blue:
            gameExit = False
            gameOver = False
            score_int = score_int + 1
        if rain_color != blue:
            if ball_y <= 300:
                gameOver = True
                gameExit = False
                homeScreen = False
            listValue = listValue + 1
            screenDisplay = win.blit(pixelpos[listValue], (0, 0))
            ball_y -= 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ball_x > ball_vel + 65:
        ball_x -= ball_vel
        ball_left = True
        ball_right = False

    elif keys[pygame.K_RIGHT] and ball_x < 500 - ball_width - ball_vel - 65:
        ball_x += ball_vel
        ball_right = True
        ball_left = False

    else:
        ball_right = False
        ball_left = False
        ball_walkCount = 0

    rain_y += rain_vel

    while gameOver:
        score_y = 350
        score_x = 240
        ball_y = 700
        win.blit(random_gameoverbg, (0, 0))
        score(score_int)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
                homeScreen = False
                score_int = 0
                score_y = 20
                score_x = 220
                listValue = 0
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                homeScreen = False
                gameOver = False
                gameExit = False
                listValue = 0
                score_y = 20
                score_x = 220
                score_int = 0

pygame.quit()