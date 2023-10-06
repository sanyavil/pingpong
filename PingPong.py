#Создай собственный Шутер!


from pygame import *
from random import randint
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

clock = time.Clock()
font2 = font.Font(None, 36)


#фоновая музыка

#нам нужны такие картинки:



score = 0 #сбито кораблей
goal = 20 #столько кораблей нужно сбить для победы
lost = 0 #пропущено кораблей
max_lost = 10 #проиграли, если пропустили столько кораблей
life = 3  #очки жизни


#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
      #вызываем конструктор класса (Sprite):
      super().__init__()
      #каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (wight, height))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed



   #метод "выстрел" (используем место игрока, чтобы создать там пулю)

#класс спрайта-врага 




width = 600
height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((width,height))
background = transform.scale(image.load('фон.jpg'), (width, height))
racket1 = Player('ракетка.jpg',30,200,4,50,150)
racket2 = Player('ракетка.jpg',520,200,4,50,150)
ball = GameSprite('Мячик.jpg',200,200,4,50,50)


font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!',True,(180,0,0))
time = font.render('Время:',True,(255,255,255))
count = font.render('Счёт:',True,(255,255,255))
count1 = font.render('Счёт:',True,(255,255,255))
win1 = font.render('PLAYER 1 WIN!',True,(0,180,0))
win2 = font.render('PLAYER 2 WIN!',True,(0,180,0))

speed_x = 3
speed_y = 3

game = True 
finish = False


score = 0
score1 = 0

FPS = 60
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish == False:
        window.blit(background,(0,0))
        window.blit(count,(100,50))
        window.blit(count1,(430,50))
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        
        ball.reset()

        count = font.render('Счёт: ' + str(score),1,(255,255,255))
        count1 = font.render('Счёт: ' + str(score1),1,(255,255,255))
        if sprite.collide_rect(racket1,ball):

            
            score+=1
        if sprite.collide_rect(racket2,ball):
            
            score1+=1
        if score == 10:
            finish = True
            window.blit(win1,(200,200))
        if score1 == 10:
            score1+=1
            window.blit(win2,(200,200))
            finish = True

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > 450 or ball.rect.y <0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > 550:
            finish = True
            window.blit(lose2,(200,200))




        display.update()

            
            

    
    
    clock.tick(FPS)

