import pygame , random
from pygame.locals import *

WIDTH = 600
HEIGHT = 600
FPS = 30

#classe da barra com as posiçoes e direçao
class dir_barra:
    
    def posicao(self , altura):
        self.altura = altura
        self.barra_pos_init = [(300 , altura) , (310 , altura) , (320 , altura) , (330 , altura) , (340 , altura) , (350 , altura) , (360 , altura) , (370 , altura) , (380 , altura) , (390 , altura) , (400 , altura)]
        
    LEFT = 0 
    RIGHT = 1 
    STOP = 2
    direction_barra = STOP






#inicializaçao do pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


#funçoes para bola
def rand_position():
    x = random.randint(0 , 580)
    y = random.randint(0 , 580)
    return [x//10 *10 , y//10 * 10]

def rand_velocity():
    x = random.randint(-10 , 10)
    y = random.randint(-10 , 10)
    return [x , y]




clock = pygame.time.Clock()


score_1 = 0
score_2 = 0
#fazer a barra(100x10)

bar1 = dir_barra()
bar1.posicao(580)
bar2 = dir_barra()
bar2.posicao(10)

barra = pygame.Surface((10,10))
barra.fill((255, 255, 255)) 
    
#fazer a bola (20x20)

ball_pos = [300 , 300]
ball = pygame.Surface((20,20))
ball.fill((255,0,0)) #vermelho
ball_vel = rand_velocity()

while True:
    #definir a condiçao de vitoria de cada lado
    if score_1 == 3:
        print("Player 1 wins")
        pygame.quit()
    if score_2 == 3:
        print("Player 2 wins")
        pygame.quit()   

    clock.tick(FPS) #posso botar a dificuldade aqui , ou ir aumentando a cada maçã comida
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    

    #fazer a barra se mexer 

        
    if event.type == KEYDOWN:
        
        #primeiro o teclado do player 1
        if event.key == K_RIGHT :
            bar1.direction_barra = bar1.RIGHT
            
       
        if event.key == K_LEFT :
            bar1.direction_barra = bar1.LEFT 

        #segundo o teclado do player 2
        if event.key == K_d :
            bar2.direction_barra = bar2.RIGHT
            
       
        if event.key == K_a :
            bar2.direction_barra = bar2.LEFT 
        
    #atualizar barra do player 1

    if bar1.direction_barra == bar1.RIGHT and bar1.barra_pos_init[9][0] <600:
        for i in range(len(bar1.barra_pos_init)):
            bar1.barra_pos_init[9-i] = (bar1.barra_pos_init[9-i][0] + 10 , bar1.barra_pos_init[9-i][1]) 
            
    if bar1.direction_barra == bar1.LEFT and bar1.barra_pos_init[0][0] >0:
        for i in range(len(bar1.barra_pos_init)):
            bar1.barra_pos_init[9-i] = (bar1.barra_pos_init[9-i][0] - 10 , bar1.barra_pos_init[9-i][1]) 

    #atualizar barra do player 2
    if bar2.direction_barra == bar2.RIGHT and bar2.barra_pos_init[9][0] <600:
        for i in range(len(bar2.barra_pos_init)):
            bar2.barra_pos_init[9-i] = (bar2.barra_pos_init[9-i][0] + 10 , bar2.barra_pos_init[9-i][1]) 
            
    if bar2.direction_barra == bar2.LEFT and bar2.barra_pos_init[0][0] >0:
        for i in range(len(bar2.barra_pos_init)):
            bar2.barra_pos_init[9-i] = (bar2.barra_pos_init[9-i][0] - 10 , bar2.barra_pos_init[9-i][1]) 
    
    
    #fazer a bola se mexer
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #fazer a colisao da bola com as bordas
    if ball_pos[0] >= 580 or ball_pos[0] <= 0: 
            ball_vel[0] = -ball_vel[0] #muda o eixo x
    if ball_pos[1] <= 0:
        score_1 += 1 
        ball_pos = [300 , 300]
        ball_vel = rand_velocity()
        
    if ball_pos[1] >=580:
        score_2 += 1
        ball_pos = [300 , 300]
        ball_vel = rand_velocity()
       
    
    #fazer a colisao da bola com a barra

    if (ball_pos[0] >=bar1.barra_pos_init[0][0] and ball_pos[0] <= bar1.barra_pos_init[9][0]) and (ball_pos[1] >=570 and ball_pos[1] <=580):
        ball_vel[1] = -ball_vel[1] #muda o eixo y ao colidir com a barra 1

    if (ball_pos[0] >=bar2.barra_pos_init[0][0] and ball_pos[0] <= bar2.barra_pos_init[9][0]) and (ball_pos[1] >=10 and ball_pos[1] <=20):
        ball_vel[1] = -ball_vel[1] #muda o eixo y ao colidir com a barra 2
    
    

    screen.fill((0,0,0)) #tela toda preta
    screen.blit(ball , ball_pos) #printa a bola

    
    #printa as barras 
    for i in bar1.barra_pos_init:
        screen.blit(barra , i)
    
    for i in bar2.barra_pos_init:
        screen.blit(barra , i)
   

    pygame.display.update() 