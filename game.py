import pygame
import random
pygame.init()

sc = pygame.display.set_mode((900, 800))
pygame.display.set_caption("Love cursor")
background = pygame.image.load('sprites/ground.jpg').convert()
clock = pygame.time.Clock()
die = pygame.surface.Surface((900, 80))
var = 0
score = 0
heart_score = 3
heart = pygame.image.load('sprites/heart.bmp')
heart.set_colorkey((255,255,255))
heart_font = pygame.font.Font('sprites/minecraft.ttf', 40)
heart_text = heart_font.render(str(heart_score),1 ,(0,0,0))
score_font = pygame.font.Font('sprites/minecraft.ttf', 60)
score_text = score_font.render(str(score),1 ,(255,255,255))
hero_up = pygame.image.load("sprites/zombi_up.png")
hero_back = pygame.image.load("sprites/zombi_back.png")
hero_left = pygame.image.load("sprites/zombi_left.png")
hero_right = pygame.image.load("sprites/zombi_right.png")
hero_up.set_colorkey((255,255,255))
hero_right.set_colorkey((255,255,255))
hero_left.set_colorkey((255,255,255))
hero_back.set_colorkey((255,255,255))
hero = hero_right
hero_rect =  hero.get_rect()
y_hero = 250
x_hero = 250
up = False
left = False
back = False
right = False
mouse = 0
die.fill((0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse = event.pos


    if mouse[0] > x_hero:
        x_hero += 1
        hero = hero_right

    if mouse[0] < x_hero:
        x_hero -= 1
        hero = hero_left

    if mouse[1] > y_hero:
        y_hero += 1
        hero = hero_back

    if mouse[1] < y_hero:
        y_hero -= 1
        hero = hero_up

    # if abs(mouse[0] - x_hero) == 0:
    #     x_hero = random.randint(0, 900)
    #     y_hero = random.randint(0, 800)
    #     if heart_score != 0:
    #         heart_score -= 1
    #     else:
    #         exit()

    if mouse[0] == x_hero and mouse[1] == y_hero:
        x_hero = random.randint(0, 900)
        y_hero = random.randint(0, 800)
        if heart_score != 0:
            heart_score -= 1
        else:
            exit()




    if x_hero >= 850:
        x_hero = 850
    if x_hero <= 0:
        x_hero = 0
    if y_hero <= 50:
        y_hero = 50
    if y_hero >= 750:
        y_hero = 750

    var += 1

    if var == 60:
        score += 1
        var = 0

    sc.blit(background, (0,0))
    clock.tick(120)
    score_text = score_font.render(str(score), 1, (0, 200, 0))
    heart_text = heart_font.render(str(heart_score), 1, (0, 0, 0))
    sc.blit(die, (0,0))
    sc.blit(heart, (805, 2))
    sc.blit(heart_text, (842, 22))
    sc.blit(score_text,(15,15))
    sc.blit(hero, (x_hero,y_hero))
    pygame.display.update()
