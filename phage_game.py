import math
import os
import random
import time
import pygame

#參數設置
game_title = "The War of Phage" #遊戲名稱
screen_x = 600 #視窗橫向大小
screen_y = 600 #視窗直向大小
FPS = 60 #更新頻率
number_of_phages = 100 #aka 血量 且影響感染細菌速度
dlife = 20 #每次碰到酶扣血量
time_remaining = int(60) #剩餘時間 一秒減1
bacteria_remaining = 5 #剩餘敵人數
addlife = 20 #每次擊殺加血量
dtime = 1/FPS
###

#函式
#def draw_cover():
font_name = pygame.font.match_font('arial')
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surface.blit(text_surface, text_rect)

def draw_health(surface, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH+100, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surface, (0, 255, 0), fill_rect)
    pygame.draw.rect(surface, (255, 255, 255), outline_rect, 2)

def draw_cover():
    waiting = True
    while waiting:
        clock.tick(FPS) #每秒FPS次
        screen.blit(cover, (0,0))
        draw_text(screen, "Press 'Enter' To Start", 30, screen_x/2+5, screen_y/1.7)
        pygame.display.update() #更新視窗
        #取得輸入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            waiting = False
            return False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
        
def draw_winend():
    #draw_text(screen, "win", 20, screen_x/2, screen_y/2)
    #pygame.display.update() #更新視窗
    waiting = True
    screen.blit(win1, (0,0))
    endframe = 0
    while waiting:
        clock.tick(5) #每秒FPS次
        pygame.display.update() #更新視窗
        #取得輸入
        keyss = pygame.key.get_pressed()
        if keyss[pygame.K_RETURN]:
            waiting = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        endframe += 1
        if endframe >= 2:
            endframe = 0
        screen.blit(win_end[endframe], (0,0))
        draw_text(screen, "Press 'Enter' To Exit", 30, screen_x/2+5, screen_y-50)

def draw_lose1end():
    #pygame.display.update() #更新視窗
    waiting = True
    screen.blit(lose1_end[0], (0,0))
    endframe = 0
    while waiting:
        clock.tick(8) #每秒FPS次
        pygame.display.update() #更新視窗
        #取得輸入
        keyss = pygame.key.get_pressed()
        if keyss[pygame.K_RETURN]:
            waiting = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        endframe += 1
        if endframe >= len(lose1_end):
            endframe = len(lose1_end)-1
        screen.blit(lose1_end[endframe], (0,0))
        draw_text(screen, "Patient Died", 50, screen_x/2, screen_y/10)
        draw_text(screen, "Press 'Enter' To Exit", 30, screen_x/2+5, screen_y-50)
        
def draw_lose2end():
    #pygame.display.update() #更新視窗
    waiting = True
    screen.blit(lose2, (0,0))
    endframe = 0
    while waiting:
        clock.tick(5) #每秒FPS次
        pygame.display.update() #更新視窗
        #取得輸入
        keyss = pygame.key.get_pressed()
        if keyss[pygame.K_RETURN]:
            waiting = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        endframe += 1
        if endframe >= 2:
            endframe = 0
        screen.blit(lose2_end[endframe], (0,0))
        draw_text(screen, "LOSE", 50, screen_x/2, screen_y/10)
        draw_text(screen, "Press 'Enter' To Exit", 30, screen_x/2+5, screen_y-50)


#初始化
pygame.init() #啟動套件
screen = pygame.display.set_mode((screen_x, screen_y)) #建立視窗
pygame.display.set_caption(game_title) #設定視窗標題
canvas = pygame.Surface(screen.get_size()) #建立與視窗同大的畫布
canvas = canvas.convert() #為畫布建立副本
canvas.fill((0,0,0)) #設定畫布顏色
screen.blit(canvas, (0,0)) #在視窗上顯示畫布
pygame.display.update() #更新視窗內容

background = pygame.image.load(os.path.join("img", "Background_.png")).convert()
cover = pygame.image.load(os.path.join("img", "Cover.png")).convert()
protease_inhibit = pygame.image.load(os.path.join("img", "Protease_Inhibitors_.png")).convert()
icon =  pygame.image.load(os.path.join("img", "icon.png")).convert()
icon.set_colorkey([0,0,0])
pygame.display.set_icon(icon)
pygame.display.set_caption("The War of Phage")
bac1 = pygame.image.load(os.path.join("img", "Bacteria1_.png")).convert()
bac2 = pygame.image.load(os.path.join("img", "Bacteria2.png")).convert()
bac3 = pygame.image.load(os.path.join("img", "Bacteria3.png")).convert()
win1 = pygame.image.load(os.path.join("img", "IMG_0421.png")).convert()
lose2 = pygame.image.load(os.path.join("img", "IMG_0412.png")).convert()
lose22 = pygame.image.load(os.path.join("img", "IMG_0411.png")).convert()
win2 = pygame.image.load(os.path.join("img", "IMG_0422.png")).convert()
win_end = []
win_end.append(win1)
win_end.append(win2)
lose2_end = []
lose2_end.append(lose2)
lose2_end.append(lose22)
uv = pygame.image.load(os.path.join("img", "UV_Light.png")).convert()
bac_ani = {}
bac_ani["b1"] = []
bac_ani["b2"] = []
bac_ani["b3"] = []
for i in range(33, 47):
    bac_img = pygame.image.load(os.path.join("img", f"IMG_03{i}.PNG")).convert()
    bac_img.set_colorkey([0,0,0])
    bac_ani["b3"].append(pygame.transform.scale(bac_img, (110, 110)))
for i in range(23, 58):
    bac_img = pygame.image.load(os.path.join("img", f"IMG_04{i}.PNG")).convert()
    bac_img.set_colorkey([0,0,0])
    bac_ani["b1"].append(pygame.transform.scale(bac_img, (110, 130)))
for i in range(59, 71):
    bac_img = pygame.image.load(os.path.join("img", f"IMG_04{i}.PNG")).convert()
    bac_img.set_colorkey([0,0,0])
    bac_ani["b2"].append(pygame.transform.scale(bac_img, (110, 90)))
lose1_end = []
for i in range(395, 411):
    end_img = pygame.image.load(os.path.join("img", f"IMG_0{i}.PNG")).convert()
    lose1_end.append(end_img)
phage_img = []
for i in range(79, 87):
    img = pygame.image.load(os.path.join("img", f"IMG_04{i}.PNG")).convert()
    img.set_colorkey([255,255,255])
    phage_img.append(pygame.transform.scale(img, (40, 60)))

#角色模板
class bacteria (pygame.sprite.Sprite):
    bac_type = 0
    updatetime=0
    move_rate = 25
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bac_type = random.randrange(1, 4)
        if self.bac_type == 1:
            self.image = pygame.transform.scale(bac3, [95,95])
            self.image.set_colorkey([0,0,0])
        elif self.bac_type == 2:
            self.image = pygame.transform.scale(bac2, [85,85])
            self.image.set_colorkey([0,0,0])
        else:
            self.image = pygame.transform.scale(bac1, [110,110])
            self.image.set_colorkey([0,0,0])
        #self.image = pygame.Surface([30, 30])
        #self.image.fill([0,0,255])
        self.rect = self.image.get_rect() #取得角色區域
        #self.radius = self.rect.width*1
        self.radius = self.rect.width * 0.95 / 2
        #pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
        self.rect.x = random.randrange(0, screen_x-self.rect.width)
        self.rect.y = random.randrange(0, screen_y-self.rect.height)
        self.move_rate = random.randrange(20, 30)

    def update(self): 
        self.updatetime += 1
        if (self.updatetime//self.move_rate)%2 == 0:
            self.rect.y += 1
            self.y = self.rect.y
        else:
            self.rect.y -= 1
            self.y = self.rect.y

class uvlight (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(uv, [20,60])
        self.image.set_colorkey([0,0,0])
        #self.image = pygame.Surface([10, 10])
        #self.image.fill([255,0,0])
        self.rect = self.image.get_rect() #取得角色區域
        #self.radius = self.rect.width / 2
        #pygame.draw.rect(self.image, (255,0,0), self.rect, width=2)
        self.rect.x = random.randrange(0, screen_x-self.rect.width)
        self.rect.y = random.randrange(-15, -10)
        self.speedy = random.randrange(5, 8)
        #self.speedx = random.randrange(-2, 2)
    
    def update(self):
        self.rect.y += self.speedy
        #self.rect.x += self.speedx
        if self.rect.top > screen_y:
            #self.rect.x = random.randrange(0, screen_x-self.rect.width)
            self.rect.y = random.randrange(-15, -10)
            self.speedy = random.randrange(5, 8)

class phage (pygame.sprite.Sprite):
    dx = 2
    dy = 2
    x = 0
    y = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = screen_x/2
        self.y = screen_y/1.2
        #self.image = pygame.image.load("1234.PNG")
        #self.image = pygame.Surface([10, 10])
        #self.image.fill([255,255,255])
        self.image = phage_img[0]
        self.rect = self.image.get_rect() #取得角色區域
        self.radius = self.rect.width * 0.85 / 2
        #pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
        self.rect.center = (screen_x/2, screen_y/1.2)
        self.health = number_of_phages
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < screen_x:
            self.rect.x += self.dx
            self.x = self.rect.x
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.dx
            self.x = self.rect.x
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.dy
            self.y = self.rect.y
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_y:
            self.rect.y += self.dy
            self.y = self.rect.y   
        
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(phage_img):
                self.frame = 0
            else:
                self.image = phage_img[self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

class protease (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(protease_inhibit, [50,50])
        self.image.set_colorkey([0,0,0])
        #self.image = pygame.Surface([10, 10])
        #self.image.fill([255,0,0])
        self.rect = self.image.get_rect() #取得角色區域
        self.radius = self.rect.width / 2
        #pygame.draw.circle(self.image, (0,0,0), self.rect.center, self.radius)
        self.rect.x = random.randrange(0, screen_x-self.rect.width)
        self.rect.y = random.randrange(-50, -10)
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-2, 2)
    
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > screen_y:
            self.rect.x = random.randrange(0, screen_x-self.rect.width)
            self.rect.y = random.randrange(-50, -10)
            self.speedy = random.randrange(2, 5)
            self.speedx = random.randrange(-2, 2)

class bac_anim (pygame.sprite.Sprite):
    def __init__(self, center, bac_num):
        pygame.sprite.Sprite.__init__(self)
        self.bac_num = bac_num
        self.image = bac_ani[self.bac_num][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(bac_ani[self.bac_num]):
                if self.bac_num != 'b2' and self.bac_num != 'b3':
                   global bacteria_remaining
                   bacteria_remaining -= 1
                self.kill()
            else:
                self.image = bac_ani[self.bac_num][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center


###

clock = pygame.time.Clock() #時間元件
phages = pygame.sprite.Group() #腳色群組
proteases = pygame.sprite.Group()
bacterias = pygame.sprite.Group()
uvls = pygame.sprite.Group()
killanims = pygame.sprite.Group()


phage_main = phage()
phages.add(phage_main)
for i in range(2):
    protease1 = protease()
    proteases.add(protease1)
for i in range(6):
    bacteria1 = bacteria()
    bacterias.add(bacteria1)
for i in range(5):
    uvl1 =uvlight()
    uvls.add(uvl1)
###

#遊戲開始
running = True
showcover = True
showwinend = False
showlose1end = False
showlose2end = False
add_life = True
while running:
    clock.tick(FPS) #每秒FPS次
    if showcover:
        closed = draw_cover()
        if closed:
            break
        showcover = False
    elif showwinend:
        draw_winend()
        running = False
    elif showlose1end:
        draw_lose1end()
        running = False
    elif showlose2end:
        draw_lose2end()
        running = False
    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #更新遊戲
    phages.update()
    proteases.update()
    bacterias.update()
    uvls.update()
    killanims.update()
    hitbyuv = pygame.sprite.groupcollide(phages, uvls, False, True, pygame.sprite.collide_circle)
    for i in hitbyuv:
        phage_main.health -= dlife
        uvl1 = uvlight()
        uvls.add(uvl1)

    hitbyproin = pygame.sprite.groupcollide(phages, proteases, False, True, pygame.sprite.collide_circle)
    for i in hitbyproin:
        add_life = False
        protease1 = protease()
        proteases.add(protease1)
    
    dtime_kill = (1/(phage_main.health+100))*200
    dtime_kill_fail = (1/(number_of_phages))*50
    keys_pressed = pygame.key.get_pressed()
    touchbacteria = pygame.sprite.groupcollide(bacterias, phages, False, False, pygame.sprite.collide_circle)
    if touchbacteria and keys_pressed[pygame.K_SPACE]:
        for i in touchbacteria:
            if i.bac_type != 1 and i.bac_type != 2:
                killanim1 = bac_anim(i.rect.center, "b1")
                killanims.add(killanim1)
                time_remaining -= dtime_kill
                #bacteria_remaining -= 1
                if add_life:
                    phage_main.health += addlife
            elif i.bac_type == 1:
                killanim3 = bac_anim(i.rect.center, "b3")
                killanims.add(killanim3)
                time_remaining -= dtime_kill_fail
            elif i.bac_type == 2:
                killanim2 = bac_anim(i.rect.center, "b2")
                killanims.add(killanim2)
                time_remaining -= dtime_kill_fail
            i.kill()
            bacteria1 = bacteria()
            bacterias.add(bacteria1)
    """for i in touchbacteria:
        phage_main.health += dlife
        bacteria1 = bacteria()
        bacterias.add(bacteria1)"""
    if bacteria_remaining <= 0 and time_remaining > 0:
        showwinend = True
    elif bacteria_remaining > 0 and time_remaining <= 0:
        showlose1end = True
    elif phage_main.health <= 0:
        showlose2end = True

    time_remaining = time_remaining - dtime
    
    #畫面顯示
    #screen.blit(canvas, (0,0)) #清除視窗
    screen.blit(background, (0,0))
    phages.draw(screen)
    proteases.draw(screen)
    bacterias.draw(screen)
    killanims.draw(screen)
    uvls.draw(screen)
    draw_text(screen, str(phage_main.health), 15, 12, 8)
    draw_text(screen, str(int(time_remaining)), 20, screen_x/2+10, 8)
    draw_text(screen, str(bacteria_remaining), 20, screen_x-10, 8)
    draw_health(screen, phage_main.health, 25, 10)
    #draw_health(screen, time_remaining, screen_x/2, 10)
    pygame.display.update() #更新視窗

pygame.quit()
###