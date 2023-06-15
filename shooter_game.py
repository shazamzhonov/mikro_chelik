
#Создай собственный Шутер! 
 
from pygame import * 
from random import randint 
mixer.init() 
mixer.music.load('Megalovania.mp3') 
mixer.music.play() 
window_w = 700 
window_h = 500 
FPS = 60 
game = True  
sound = mixer.Sound('fire.ogg') 
#создай окно игры 
window = display.set_mode((window_w,window_h)) 
background = transform.scale(image.load('galaxy.jpg'),(window_w,window_h)) 
player = transform.scale(image.load('rocket.png'),(40,40)) 
m = transform.scale(image.load('ufo.png'),(40,40)) 
#задай фон сцены 
class GameSprite(sprite.Sprite): 
    def __init__(self,player_image,player_speed,player_x,player_y,width,height): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image),(width,height)) 
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self): 
        window.blit(self.image,(self.rect.x,self.rect.y)) 
    def fire(self): 
        bullet = Bullet('bullet.png',10,self.rect.centerx,self.rect.top,6,12) 
        bullets.add(bullet) 
        sound.play() 
class Player(GameSprite): 
    def update(self): 
        global run 
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_LEFT] and self.rect.x>0: 
            self.rect.x -= self.speed 
        if keys_pressed[K_RIGHT]and self.rect.x<window_w-60: 
            self.rect.x += self.speed 
        if keys_pressed[K_UP] and self.rect.y>0 and keys_pressed[K_c]: 
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y<window_h-60 and keys_pressed[K_c]: 
            self.rect.y += self.speed 
class Enemy(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        global missed,missed_text 
        if self.rect.y >= window_h: 
            self.rect.y = -40 
            self.rect.x = randint(10,650) 
            missed = missed + 1 
            missed_text = font1.render(f'Propusheno: {missed}',True,(255,255,255)) 
class EN(GameSprite): 
    def update(self): 
        self.rect.y += self.speed 
        global missed,missed_text 
        if self.rect.y >= window_h: 
            self.rect.y = -40 
            self.rect.x = randint(10,650) 
 
class Bullet(GameSprite): 
    def update(self): 
        self.rect.y -= self.speed 
        if self.rect.y < -10: 
            self.kill() 
bullets = sprite.Group() 
asteroids = sprite.Group() 
for i in range(3): 
    a = EN('asteroid.png',1,randint(0,650),0,65,65) 
    asteroids.add(a) 
click = time.Clock() 
player = Player('rocket.png',10,100,400,70,100) 
finish = False 
monsters = sprite.Group() 
for i in range(5): 
    m = Enemy('ufo.png',randint(1,3),randint(0,650),0,65,65) 
    monsters.add(m) 
missed = 0 
shot = 0 
font.init() 
font1 = font.SysFont('jokerman',20) 
font2 = font.SysFont('jokerman',100) 
missed_text = font1.render(f'Propusheno:{missed}',True,(255,255,255)) 
shot_text = font1.render(f'Shet:{shot}',True,(255,255,255))     
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
        if e.type == KEYDOWN and e.key == K_SPACE: 
            player.fire() 
    if not finish: 
        bullets_enemys = sprite.groupcollide(bullets,monsters,True,True) 
        player_enemys = sprite.spritecollide(player,monsters,False) 
        for i in bullets_enemys: 
            m = Enemy('ufo.png',randint(2,4),randint(0,650),0,65,65) 
            shot += 1 
            monsters.add(m) 
            shot_text = font1.render(f'Shet:{shot}',True,(255,255,255)) 
        for i in player_enemys: 
            finish = True 
        if missed > 30: 
            finish = True 
        window.blit(background,(0,0)) 
        window.blit(missed_text,(0,20)) 
        window.blit(shot_text,(0,5)) 
        player.reset() 
        player.update() 
        asteroids.update() 
        asteroids.draw(window) 
        bullets.update() 
        bullets.draw(window) 
        monsters.draw(window) 
        monsters.update() 
    elif finish == True: 
        finish_text = font2.render(f'lox',True,(255,255,255)) 
        window.blit(missed_text,(300,250)) 
        window.blit(shot_text,(310,280)) 
        window.blit(finish_text,(160,140)) 
    display.update() 
    click.tick(FPS)
