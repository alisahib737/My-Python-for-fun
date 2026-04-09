import time
import random
import pygame

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((666, 900))

pygame.display.set_caption(r"Flappy Birds")
pygame.display.set_icon(pygame.image.load(r"Flappy_Bird.png"))

background = pygame.image.load(r'flappy bird wallpaper.jpg').convert_alpha()
background = pygame.transform.scale(background, (666, 900))
game_limit = pygame.image.load(r'flappy bird wallpaper.jpg').convert_alpha()
game_limit = pygame.transform.scale(game_limit, (666, 900))
game_limit_rec = game_limit.get_rect(bottomleft = (-200,0))
flappy_bird = pygame.image.load(r'Flappy_Bird.png').convert_alpha()
flappy_bird = pygame.transform.scale(flappy_bird, (50, 50))

start_button = pygame.image.load(r'start button.png').convert_alpha()
start_button = pygame.transform.scale(start_button, (220, 100))
start_button_rect = start_button.get_rect(center = (333,450))

play_again_button = start_button.copy()
play_again_button = pygame.transform.scale(play_again_button,(200, 90))
play_again_button_rect = play_again_button.get_rect(center = (333,-100))

font_style = pygame.font.Font(r'Minecraft.ttf',10)
my_information = font_style.render("Made by Duketo",True,'Black')

flappy_bird_logo = pygame.image.load(r'flappybird logo.png').convert_alpha()
flappy_bird_logo_rec = flappy_bird_logo.get_rect(topleft = (120,200))

score_screen = pygame.image.load(r'score screen.png').convert_alpha()
score_screen = pygame.transform.scale(score_screen,(500,250))
score_screen_rec = score_screen.get_rect(center = (333,500))


game_over_screen = pygame.image.load(r'game over.png').convert_alpha()
game_over_screen = pygame.transform.scale(game_over_screen,(500,100))
game_over_screen_rec = game_over_screen.get_rect(center = (333,200))

game_over_sound = pygame.mixer.Sound(r'game over.wav')
score_gained_sound = pygame.mixer.Sound(r'score gained.flac')
score_screen_sound = pygame.mixer.Sound(r'score screen whoosh.mp3')


flappy_bird_pillar_upper_1= pygame.image.load(r'flappy birds pillar(1).png').convert_alpha()
flappy_bird_pillar_upper_1 = pygame.transform.scale(flappy_bird_pillar_upper_1, (76, 500))
flappy_bird_pillar_upper_rec_1 = flappy_bird_pillar_upper_1.get_rect(topleft = (800,-20))
flappy_bird_pillar_upper_2 = flappy_bird_pillar_upper_1.copy()
flappy_bird_pillar_upper_rec_2 = flappy_bird_pillar_upper_2.get_rect( topleft = (1065,-50))
flappy_bird_pillar_upper_3 = flappy_bird_pillar_upper_1.copy()
flappy_bird_pillar_upper_rec_3 = flappy_bird_pillar_upper_3.get_rect( topleft = (1330,-90))
flappy_bird_pillar_upper_4 = flappy_bird_pillar_upper_1.copy()
flappy_bird_pillar_upper_rec_4 = flappy_bird_pillar_upper_4.get_rect(topleft= (1595,-30))

flappy_bird_pillar_lower_1 = pygame.image.load(r'flappy birds pillar(2).png').convert_alpha()
flappy_bird_pillar_lower_1 = pygame.transform.scale(flappy_bird_pillar_lower_1, (76, 500))
flappy_bird_pillar_lower_rec_1 = flappy_bird_pillar_lower_1.get_rect(topleft = (800,650))
flappy_bird_pillar_lower_2 = flappy_bird_pillar_lower_1.copy()
flappy_bird_pillar_lower_rec_2 = flappy_bird_pillar_lower_2.get_rect(topleft = (1065,620))
flappy_bird_pillar_lower_3 = flappy_bird_pillar_lower_1.copy()
flappy_bird_pillar_lower_rec_3 = flappy_bird_pillar_lower_3.get_rect( topleft =(1330,580))
flappy_bird_pillar_lower_4 = flappy_bird_pillar_lower_1.copy()
flappy_bird_pillar_lower_rec_4 = flappy_bird_pillar_lower_4.get_rect(topleft = (1595,640))


speedbar1 = pygame.image.load(r'SpeedBar.jpg').convert_alpha()
speedbar1 = pygame.transform.scale(speedbar1, (666, 146))
speedbar1_rect = speedbar1.get_rect(topleft=(-666,754))
speedbar2 = speedbar1.copy()
speedbar2_rect = speedbar2.get_rect(topleft=(0,754))
speedbar3 = speedbar1.copy()
speedbar3_rect = speedbar3.get_rect(topleft=(666,754))

angle = 20

loop_starter = True
game_start = True
game_over = False
with open('highscore.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    highscore_str = content
    file.close()
highscore = int(highscore_str)
x= 0
var1=0
this=True
eventcollector = []
def speedbar(var1,var2):
    x = 0
    while x<5:
        var1.x -= 1
        if var1.x < -666:
            var1.x = var2.x + 585
        x+=1

score = 0
score_font = pygame.font.Font(r'Minecraft.ttf',50)
player_score = score_font.render(str(score),True,'Black')



def pillars(var1,var2):
    var1.x -=5
    var2.x -=5
    if var1.x < -200:
        var1.x = 900
        var2.x = 900
        random_var = random.randint(1, 10)
        if random_var == 1:
            var1.y = -50
            var2.y = 670
        elif random_var == 2:
            var1.y = -330
            var2.y = 390
        elif random_var == 3:
            var1.y = -100
            var2.y = 620
        elif random_var == 4:
            var1.y = -400
            var2.y = 320
        elif random_var == 5:
            var1.y = -220
            var2.y = 500
        elif random_var == 6:
            var1.y = -420
            var2.y = 300
        elif random_var == 7:
            var1.y = -280
            var2.y = 440
        elif random_var == 8:
            var1.y = -25
            var2.y = 695
        elif random_var == 9:
            var1.y = -360
            var2.y = 360
        elif random_var == 10:
            var1.y = -160
            var2.y = 560
var2 = True
var3 = 0
var4 = 0
var5 = 0
something = True
high_score_font = score_font.render(str(highscore), True, 'Black')

while loop_starter:

    player_score = score_font.render(str(score), True, 'Black')
    rotated_flappy_bird = pygame.transform.rotate(flappy_bird, angle)
    if var2:
        rotated_flappy_bird_rect = rotated_flappy_bird.get_rect(midbottom=(100, 440))
        var2 = False
    flappy_bird_pillar_upper_rec_1_hb = flappy_bird_pillar_upper_rec_1.inflate(
        -flappy_bird_pillar_upper_rec_1.width * 0.3, 0)
    flappy_bird_pillar_upper_rec_2_hb = flappy_bird_pillar_upper_rec_2.inflate(
        -flappy_bird_pillar_upper_rec_2.width * 0.3, 0)
    flappy_bird_pillar_upper_rec_3_hb = flappy_bird_pillar_upper_rec_3.inflate(
        -flappy_bird_pillar_upper_rec_3.width * 0.3, 0)
    flappy_bird_pillar_upper_rec_4_hb = flappy_bird_pillar_upper_rec_4.inflate(
        -flappy_bird_pillar_upper_rec_4.width * 0.3, 0)
    flappy_bird_pillar_lower_rec_1_hb = flappy_bird_pillar_lower_rec_1.inflate(-flappy_bird_pillar_lower_rec_1.width * 0.3, 0)
    flappy_bird_pillar_lower_rec_2_hb = flappy_bird_pillar_lower_rec_2.inflate(
        -flappy_bird_pillar_lower_rec_2.width * 0.3, 0)
    flappy_bird_pillar_lower_rec_3_hb = flappy_bird_pillar_lower_rec_3.inflate(
        -flappy_bird_pillar_lower_rec_3.width * 0.3, 0)
    flappy_bird_pillar_lower_rec_4_hb = flappy_bird_pillar_lower_rec_4.inflate(
        -flappy_bird_pillar_lower_rec_4.width * 0.3, 0)
    rotated_flappy_bird_rect_hb = rotated_flappy_bird_rect.inflate(-rotated_flappy_bird_rect.width * 0.2, -rotated_flappy_bird_rect.height * 0.4)

    obstacles = [
        flappy_bird_pillar_upper_rec_1_hb, flappy_bird_pillar_upper_rec_2_hb,
        flappy_bird_pillar_upper_rec_3_hb, flappy_bird_pillar_upper_rec_4_hb,
        flappy_bird_pillar_lower_rec_1_hb, flappy_bird_pillar_lower_rec_2_hb,
        flappy_bird_pillar_lower_rec_3_hb, flappy_bird_pillar_lower_rec_4_hb,
        speedbar1_rect, speedbar2_rect, speedbar3_rect,
        game_limit_rec
    ]

    for event in pygame.event.get():
        eventcollector.append(event)
    speedbar(speedbar1_rect, speedbar3_rect)
    speedbar(speedbar2_rect, speedbar1_rect)
    speedbar(speedbar3_rect, speedbar2_rect)

    for event in eventcollector:
        if event.type == pygame.QUIT:
            loop_starter = False

    if rotated_flappy_bird_rect_hb.collidelist(obstacles) != -1:
        game_over = True
        if var5 == 0:
            var5+=1
            game_over_sound.play()
    if game_over == False:
        if game_start == True:
            pillars(flappy_bird_pillar_upper_rec_1,flappy_bird_pillar_lower_rec_1)
            pillars(flappy_bird_pillar_upper_rec_2,flappy_bird_pillar_lower_rec_2)
            pillars(flappy_bird_pillar_upper_rec_3,flappy_bird_pillar_lower_rec_3)
            pillars(flappy_bird_pillar_upper_rec_4,flappy_bird_pillar_lower_rec_4)
            x=x+1
            if x>15:
                rotated_flappy_bird_rect.y +=12
                if angle>-60:
                    angle -= 3
            elif x>20:
                rotated_flappy_bird_rect.y += 7
                if angle > -60:
                    angle -= 2
            else:
                rotated_flappy_bird_rect.y +=3
                angle-=1

            if flappy_bird_pillar_upper_rec_1.x ==15:
                score +=1
                score_gained_sound.play()
            elif flappy_bird_pillar_upper_rec_2.x ==15:
                score +=1
                score_gained_sound.play()
            elif flappy_bird_pillar_upper_rec_3.x ==15:
                score +=1
                score_gained_sound.play()
            elif flappy_bird_pillar_upper_rec_4.x ==15:
                score +=1
                score_gained_sound.play()

            for event in eventcollector:
                if event.type == pygame.MOUSEBUTTONDOWN :
                    if event.button == 1 :
                        rotated_flappy_bird_rect.y -= 75
                        score_screen_sound.play()
                        x=0
                        if angle<20:
                            while angle < 20:
                                angle = angle + 1
                                if angle ==20:
                                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        rotated_flappy_bird_rect.y -= 75
                        score_screen_sound.play()
                        x = 0
                        if angle < 20:
                            while angle < 20:
                                angle = angle + 1
                                if angle == 20:
                                    break

        if game_start == False:
            if something == True:
                for event in eventcollector:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_start = True
                            something = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if start_button_rect.collidepoint(event.pos):
                            game_start = True
                            start_button_rect = None
                            something = False
        eventcollector = []

    if not start_button_rect == None:
        window.blit(start_button, start_button_rect)
        window.blit(flappy_bird_logo, flappy_bird_logo_rec)
    if flappy_bird_logo_rec.y >=200 and var1 >=0:
        flappy_bird_logo_rec.y +=1
        var1+=1
        if var1 == 20:
            var1 = -20
        time.sleep(0.03)

    elif flappy_bird_logo_rec.y <=220 and var1<0:
        flappy_bird_logo_rec.y -=1
        var1+=1
        time.sleep(0.02)
    window.blit(background, (0, 0))
    if game_start == True:
        window.blit(flappy_bird_pillar_upper_1, flappy_bird_pillar_upper_rec_1)
        window.blit(flappy_bird_pillar_upper_2, flappy_bird_pillar_upper_rec_2)
        window.blit(flappy_bird_pillar_upper_3, flappy_bird_pillar_upper_rec_3)
        window.blit(flappy_bird_pillar_upper_4, flappy_bird_pillar_upper_rec_4)
        window.blit(flappy_bird_pillar_lower_1, flappy_bird_pillar_lower_rec_1)
        window.blit(flappy_bird_pillar_lower_2, flappy_bird_pillar_lower_rec_2)
        window.blit(flappy_bird_pillar_lower_3, flappy_bird_pillar_lower_rec_3)
        window.blit(flappy_bird_pillar_lower_4, flappy_bird_pillar_lower_rec_4)
        if game_over == False:
            window.blit(player_score,(333,100))
    if game_over == True:
        this = False
        if score >= highscore:
            highscore = score
            high_score_font = score_font.render(str(highscore), True, 'Black')
        window.blit(score_screen, score_screen_rec)
        window.blit(game_over_screen, game_over_screen_rec)
        if var3 <= 5:
            score_screen_rec.y += 2
            game_over_screen_rec.y += 2
            var3 +=1
        else:
            window.blit(player_score, (313, 465))
            window.blit(high_score_font, (313, 560))
        var4 +=1
        if var4 >= 10:
            if play_again_button_rect.y <= 260:
                play_again_button_rect.y += 30
        for event in eventcollector:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button_rect.collidepoint(event.pos):
                    game_over = False
                    this = True
                    var4 =0
                    play_again_button_rect.y = -100
                    rotated_flappy_bird_rect.y = 440
                    score = 0
                    flappy_bird_pillar_lower_rec_1.x=800
                    flappy_bird_pillar_lower_rec_2.x=1065
                    flappy_bird_pillar_lower_rec_3.x=1330
                    flappy_bird_pillar_lower_rec_4.x=1595
                    flappy_bird_pillar_upper_rec_1.x = 800
                    flappy_bird_pillar_upper_rec_2.x = 1065
                    flappy_bird_pillar_upper_rec_3.x = 1330
                    flappy_bird_pillar_upper_rec_4.x = 1595
    window.blit(speedbar1, speedbar1_rect)
    window.blit(speedbar2, speedbar2_rect)
    window.blit(speedbar3, speedbar3_rect)

    if this == True:
        window.blit(rotated_flappy_bird, rotated_flappy_bird_rect)
    window.blit(play_again_button,play_again_button_rect)
    window.blit(my_information,(570,880))
    clock.tick(60)


    highscore_string = str(highscore)
    with open('highscore.txt', 'w', encoding='utf-8') as file:
        file.write(highscore_string)
        file.close()
    pygame.display.update()

