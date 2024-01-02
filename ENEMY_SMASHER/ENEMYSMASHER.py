import pygame
import random

class Button:
    def __init__(self,text,width,height,pos,elevation):

        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]


        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'

        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):

        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(pencere, self.bottom_color,self.bottom_rect, border_radius=12)
        pygame.draw.rect(pencere, self.top_color, self.top_rect,border_radius=12)
        pencere.blit(self.text_surf, self.text_rect)
        self.check_click()
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77' 

pygame.init()
genislik = 1280
yukseklik = 720
pencere = pygame.display.set_mode((genislik, yukseklik), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
started = False
pressed = False
score = 0
sb = True
cd = True
hp = 100
bar = 100
game_over = False
gui_font = pygame.font.Font(None,30)
creditstext = False
ct = False
font = pygame.font.SysFont("arialblack",40)
font3 = pygame.font.SysFont("arialblack",20)
font2 = pygame.font.SysFont("arialblack",60)
game_over_font = pygame.font.SysFont("arialblack",60)

class HeatlthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw2(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(pencere, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(pencere, "green", (self.x, self.y, self.w * ratio, self.h))

class Bar():
    def __init__(self, x, y, w, h, max_bar):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bar = max_bar
        self.max_bar = max_bar

    def draw3(self, surface):
        ratio = self.bar / self.max_bar
        pygame.draw.rect(pencere, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(pencere, "orange", (self.x, self.y, self.w * ratio, self.h))

yazi = font.render("YAPIMCI: Emir Hamza Paspal",True,(255,255,255))
yazi_koordinat = yazi.get_rect()
yazi_koordinat.topleft = (400,200)

yazi2 = font2.render("ENEMY SMASHER",True,(255,255,255))
yazi2_koordinat = yazi2.get_rect()
yazi2_koordinat.topleft = (370, 100)

button1 = Button('Start',200,40,(540,300),6)

button2 = Button('Credits',200,40,(540,400),6)

button3 = Button('Exit', 100,20,(1000,600),6)

button4 = Button('Quit', 200,40,(540,500),6)

player = pygame.image.load("player.png")
player_pos = player.get_rect()
player_pos.topleft = (pencere.get_width() / 2, pencere.get_height() / 2)

health_bar = HeatlthBar(100,40,200,20,100)

tsa_bar = Bar(1000,40,200,20,100)    

bullet = pygame.image.load("bullet.png")
bullet_pos = bullet.get_rect()
bullet_pos.topleft = (300, 300)

sword = pygame.image.load("sword.png")
sword_pos = sword.get_rect()
sword_pos.topleft = (player_pos.x + 40, player_pos.y + 10)

sword_attack = pygame.image.load("sword_attack.png")
sword_attack_pos = sword_attack.get_rect()
sword_attack_pos.topleft = (sword_pos.x, sword_pos.y)

healthplus = pygame.image.load("healthplus.png")
healthplus_pos = healthplus.get_rect()
healthplus_pos.topleft = (100, 500)

barplus = pygame.image.load("barplus.png")
barplus_pos = barplus.get_rect()
barplus_pos.topleft = (100, 300)

playerup = pygame.image.load("playerup.png")
playerup_pos = playerup.get_rect()
playerup_pos.topleft = (player_pos.x, player_pos.y)

playerright = pygame.image.load("playerright.png")
playerright_pos = playerright.get_rect()
playerright_pos.topleft = (player_pos.x, player_pos.y)

playerleft = pygame.image.load("playerleft.png")
playerleft_pos = playerup.get_rect()
playerleft_pos.topleft = (player_pos.x, player_pos.y)

ghost = pygame.image.load("ghost.png")
ghost_pos = ghost.get_rect()
ghost_pos.topleft = (100,100)

enemy = pygame.image.load("enemy.png")
enemy_pos = enemy.get_rect()
enemy_pos.topleft = (pencere.get_width() -200 , pencere. get_height() - 400)

while running:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            running = False
            pygame.quit()
    pencere.fill((0,200,255))
    if started == False:
        button1.draw()
        button2.draw()
        button4.draw()
        pencere.blit(yazi2, yazi2_koordinat)
        player_pos.topleft = (pencere.get_width() / 2, pencere.get_height() / 2)
        enemy_pos.topleft = (pencere.get_width() -200 , pencere. get_height() - 400)
        sword_pos.topleft = (player_pos.x + 40, player_pos.y + 10)
        sword_attack_pos.topleft = (sword_pos.x, sword_pos.y)
        playerup_pos.topleft = (player_pos.x, player_pos.y)
        playerright_pos.topleft = (player_pos.x, player_pos.y)
        playerleft_pos.topleft = (player_pos.x, player_pos.y)
        ghost_pos.topleft = (100,100)
    if button2.pressed:
        creditstext = True
    if creditstext == True:
        pencere.fill((0,200,255))
        button3.draw()
        pencere.blit(yazi,yazi_koordinat)
        ct = True
    if button3.pressed:
        creditstext = False
    if button1.pressed:
        started = True
    if button4.pressed:
        pygame.quit()

    keys = pygame.key.get_pressed()
    if started == True:
        if hp > 100:
            hp = 100
        if bar > 100:
            bar = 100
        if hp > 0:
            pencere.blit(healthplus, healthplus_pos)
            pencere.blit(barplus, barplus_pos)
            yazi3 = font.render("SCORE:"+str(score),True,(0,0,0))
            yazi3_pos = yazi3.get_rect()
            yazi3_pos.topleft = (500, 50)
            health_bar.draw2(pencere)
            health_bar.hp = hp
            tsa_bar.draw3(pencere)
            tsa_bar.bar = bar
            pencere.blit(yazi3, yazi3_pos)
            if keys[pygame.K_w]:
                player_pos.y -= 2
                playerleft_pos.y -= 2
                playerup_pos.y -= 2
                playerright_pos.y -= 2
                sword_pos.y -= 2
                sword_attack_pos.y -= 2
                pencere.blit(playerup, playerup_pos)
                sb = True
                if keys[pygame.K_SPACE]:
                    pencere.blit(sword_attack, sword_attack_pos)
                    pencere.blit(playerup, playerup_pos)
                    bar = bar -  0.1
                    sb = False
            elif keys[pygame.K_s]:
                player_pos.y += 2
                playerup_pos.y += 2
                playerleft_pos.y += 2
                playerright_pos.y += 2
                sword_pos.y += 2
                sword_attack_pos.y += 2
                sb = True
                pencere.blit(player, player_pos)
                if keys[pygame.K_SPACE]:
                    pencere.blit(sword_attack, sword_attack_pos)
                    pencere.blit(player, player_pos)
                    bar = bar -  0.1
                    sb = False
            elif keys[pygame.K_a]:
                player_pos.x -= 2
                playerup_pos.x -= 2
                playerleft_pos.x -= 2
                playerright_pos.x -= 2
                sword_pos.x -= 2
                sword_attack_pos.x -= 2
                sb = True
                pencere.blit(playerleft, playerleft_pos)
                if keys[pygame.K_SPACE]:
                    pencere.blit(sword_attack, sword_attack_pos)
                    pencere.blit(playerleft, playerleft_pos)
                    bar = bar -  0.1
                    sb = False
            elif keys[pygame.K_d]:
                player_pos.x += 2
                playerleft_pos.x += 2
                playerup_pos.x += 2
                playerright_pos.x += 2
                sword_pos.x += 2
                sword_attack_pos.x += 2
                sb = True
                pencere.blit(playerright, playerright_pos)
                if keys[pygame.K_SPACE]:
                    pencere.blit(sword_attack, sword_attack_pos)
                    pencere.blit(playerright, playerright_pos)
                    bar = bar -  0.1
                    sb = False
            elif keys[pygame.K_SPACE]:
                pencere.blit(sword_attack, sword_attack_pos)
                pencere.blit(player, player_pos)
                bar = bar -  0.1
                sb = False
            else:
                pencere.blit(player, player_pos)
                sb = True
            if sb == True:
                pencere.blit(sword, sword_pos)
            if keys[pygame.K_SPACE]:
                pygame.draw.rect(pencere,(0,200,255),sword_attack_pos,1)
                pygame.draw.rect(pencere,(0,200,255),player_pos,1)
                if sword_attack_pos.colliderect(enemy_pos):
                    enemy_pos.x = random.randint(0,genislik-32)
                    enemy_pos.y = random.randint(0,yukseklik-90)
                    score += 1
            if player_pos.colliderect(healthplus_pos):
                healthplus_pos.x = random.randint(0,genislik-32)
                healthplus_pos.y = random.randint(0,yukseklik-90)
                hp = hp + 10
            if player_pos.colliderect(barplus_pos):
                barplus_pos.x = random.randint(0, genislik-32)
                barplus_pos.y = random.randint(0,yukseklik-90)
                bar = bar + 10
            if enemy_pos.colliderect(player_pos):
                hp = hp - 0.1
            if bar < 0:
                pygame.draw.rect(pencere,(0,200,255),ghost_pos, 1)
                pencere.blit(ghost,ghost_pos)
                if player_pos.x > ghost_pos.x:
                    ghost_pos.x = ghost_pos.x + 1
                if player_pos.x < ghost_pos.x:
                    ghost_pos.x = ghost_pos.x - 1
                if player_pos.y > ghost_pos.y:
                    ghost_pos.y = ghost_pos.y + 1
                if player_pos.y < ghost_pos.y:
                    ghost_pos.y = ghost_pos.y - 1
        if hp < 0:
            pygame.draw.circle(pencere,(0,255,255),(650,300),155,0)
            yazigo = font3.render("SCORE: " + str(score),True,(0,0,0))
            yazigo_pos = yazigo.get_rect()
            yazigo_pos.topleft = (560,200)

            yazigo0 = font3.render("Press R to RESTART",True,(0,0,0))
            yazigo0_pos = yazigo0.get_rect()
            yazigo0_pos.topleft = (560,250)

            yg = " "
            if score < 50:
                yg = "BAD"
            if score >= 50 and score < 70:
                yg = "MID"
            if score >= 70 and score < 100:
                yg = "GOOD"
            if score >= 100 and score < 150:
                yg = "INSANE"
            if score >=150:
                yg = "GOD"

            yazigo1 = font3.render(str(yg)+" Score",True,(0,0,0))
            yazigo1_pos = yazigo1.get_rect()
            yazigo1_pos.topleft = (560,300)
            
            pencere.blit(yazigo1, yazigo1_pos)
            pencere.blit(yazigo0, yazigo0_pos)
            pencere.blit(yazigo, yazigo_pos)
            if keys[pygame.K_r]:
                started = False
                creditstext = False
                hp = 100
                bar = 100
                score = 0
        if ghost_pos.colliderect(player_pos):
            hp = hp - 0.1
        if hp > 0:
            pencere.blit(enemy, enemy_pos)
        if player_pos.x > enemy_pos.x:
            enemy_pos.x = enemy_pos.x + 1
        if player_pos.x < enemy_pos.x:
            enemy_pos.x = enemy_pos.x - 1
        if player_pos.y > enemy_pos.y:
            enemy_pos.y = enemy_pos.y + 1
        if player_pos.y < enemy_pos.y:
            enemy_pos.y = enemy_pos.y - 1
    pygame.display.update()
    pygame.display.set_caption("ENEMY SMASHER")
    clock.tick(300)