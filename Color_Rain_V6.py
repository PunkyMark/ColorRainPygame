import pygame
from pygame.locals import *
import random

pygame.init()

FPS = 27

pixelpos_list = 0

rain_y_catch_pos = 740
rain_y_dis_pos = 750

amount_Rain = 1

score_y = 20
score_x = 220
score_int = 0


def score(score):
    score_text = font.render(str(score), True, black)
    fake_win.blit(score_text, [score_x, score_y])


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

colors = [green, red, yellow, blue]
rain_x_pos = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
rain_y_pos = [20, -20, -60, -100, -140, -200, -260, -300]

win = pygame.display.set_mode((500, 800))
fake_win = win.copy()
pygame.display.set_caption("Color Rain")
listValue = 0

walkRight = [pygame.image.load('1_B.png'), pygame.image.load('2_B.png'), pygame.image.load('3_B.png'),
             pygame.image.load('4_B.png'), pygame.image.load('5_B.png'), pygame.image.load('6_B.png'),
             pygame.image.load('7_B.png'), pygame.image.load('8_B.png'), pygame.image.load('9_B.png')]

walkLeft = [pygame.image.load('9_B.png'), pygame.image.load('8_B.png'), pygame.image.load('7_B.png'),
            pygame.image.load('6_B.png'), pygame.image.load('5_B.png'), pygame.image.load('4_B.png'),
            pygame.image.load('3_B.png'), pygame.image.load('2_B.png'), pygame.image.load('1_B.png')]

still_ball = pygame.image.load('0_B.png')

homebg = [pygame.image.load('Home_red_2.png'), pygame.image.load('Home_green_2.png'),
          pygame.image.load('Home_yellow_2.png'),
          pygame.image.load('Home_blue_2.png')]

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
    fake_win.blit(screen_text, [text_x, text_y])


class Ball(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.walkCount = 0
        self.still_ball = True
        self.left = False
        self.right = False


    def draw(self, fake_win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            fake_win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.right:
            fake_win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        else:
            fake_win.blit(still_ball, (self.x, self.y))

        pygame.display.update()


class Rain(object):
    def __init__(self, x, y, radius, color):
        self.y = random.choice(rain_y_pos)
        self.x = random.choice(rain_x_pos)
        self.radius = radius
        self.color = random.choice(colors)
        self.vel = 10

    def draw(self, fake_win):
        pygame.draw.circle(fake_win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    fake_win.blit(pixelpos[pixelpos_list], (0, 0))
    score(score_int)
    for rain in rains:
        rain.draw(fake_win)
    ball.draw(fake_win)

    pygame.display.update()


# mainloop
ball = Ball(200, 700, 60, 60)
rains = []

gameExit = False
homeScreen = True
gameOver = False

while not gameExit:
    clock.tick(FPS)
    random_homebg = random.choice(homebg)
    random_gameoverbg = random.choice(gameoverbg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            homeScreen = False
            gameOver = False
        if event.type == VIDEORESIZE:
            size = event.dict['size']
            screen = pygame.display.set_mode(size,RESIZABLE)

    while homeScreen:
        random_playbg = random.choice(playbg)
        fake_win.blit(random_homebg, (0, 0))
        win.blit(pygame.transform.scale(fake_win, size), (0, 0))
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

    for rain in rains:
        rain.y += rain.vel
        if rain.y > rain_y_catch_pos and rain.y <= rain_y_dis_pos and rain.x >= ball.x and rain.x < (ball.x + ball.width):
          if rain.color == blue:
            score_int += 1
            amount_Rain += 1
          if rain.color != blue:
            pixelpos_list += 1
            ball.y -= 50
            rain_y_dis_pos -= 50
            rain_y_catch_pos -= 50
          if ball.y <= 300:
            gameExit = False
            homeScreen = False
            gameOver = True
        elif rain.y > rain_y_dis_pos:
            rains.pop(rains.index(rain))

    if len(rains) < amount_Rain:
        rains.append(Rain(random.choice(rain_x_pos), (random.choice(rain_y_pos)), 10, (random.choice(colors))))

    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    if mouse[0] < size[0]/2 and ball.x > ball.vel + 65:
        if click[0] == 1:
            ball.x -= ball.vel
            ball.left = True
            ball.right = False
        else:
            ball.right = False
            ball.left = False
            ball.walkCount = 0

    if mouse[0] > size[0]/2 and ball.x < 500 - ball.width - ball.vel - 65:
        if click[0] == 1:
            ball.x += ball.vel
            ball.right = True
            ball.left = False

        else:
            ball.right = False
            ball.left = False
            ball.walkCount = 0


    redrawGameWindow()

    win.blit(pygame.transform.scale(fake_win, size), (0, 0))
    pygame.display.update()

    while gameOver:
        del rains[:]
        rain_y_catch_pos = 740
        rain_y_dis_pos = 750
        score_y = 350
        score_x = 240
        ball.y = 700
        amount_Rain = 1
        fake_win.blit(random_gameoverbg, (0, 0))
        score(score_int)
        win.blit(pygame.transform.scale(fake_win, size), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
                homeScreen = False
                score_int = 0
                score_y = 20
                score_x = 220
                pixelpos_list = 0
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                homeScreen = False
                gameOver = False
                gameExit = False
                pixelpos_list = 0
                score_y = 20
                score_x = 220
                score_int = 0

pygame.quit()
