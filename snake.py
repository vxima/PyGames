import pygame , random
from pygame.locals import *

WIDTH = 600
HEIGHT = 600
FPS = 10

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cobrinha")

snake = [(200,200) , (210 , 200) , (220 , 200)] #posicao inicial
snake_skin = pygame.Surface((10 , 10)) 
snake_skin.fill((255 , 255 , 255)) # branco

def rand_position():
    x = random.randint(10 , 580)
    y = random.randint(10 , 580)
    return (x//10 *10 , y//10 * 10)

apple_pos = rand_position()
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #vermelho

clock = pygame.time.Clock()
UP = 0 
RIGHT = 1 
DOWN = 2 
LEFT = 3 

direction = LEFT 
score = 0
borders = [(0,0)]
for i in range(60):
    borders.append((0 , borders[i][1] + 10)) #borda esquerda

for i in range(60 , 120):
    borders.append((borders[i][0] + 10, 590)) #borda baixo

for i in range(120 , 180):
    borders.append((590, borders[i][1] - 10)) # borda direita
    
for i in range(180 , 240):
    borders.append((borders[i][0] - 10, 0 )) #borda cima

borders_shape = pygame.Surface((10 , 10)) 
borders_shape.fill((0 , 0 , 255))


while True:
    
    clock.tick(FPS + 5*score) #posso botar a dificuldade aqui , ou ir aumentando a cada maçã comida
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    #colisao com as bordas
    for x in range(len(borders)):
        if snake[0] == borders[x]:
            print("Sua pontuação foi :" , score)
            pygame.quit()

    #colisao com a propria cobrinha
    for x in range(2 , len(snake)):
        if snake[0] == snake[x]:
            print("Sua pontuação foi : " + score)
            pygame.quit()
    #atualizar pontuaçao e tamanho da cobra
    if snake[0] == apple_pos:
        score += 1
        apple_pos = rand_position()
        snake.append((0,0)) #aumenta o tamanho da cobrinha

    #controle nas setas 
    if event.type == KEYDOWN:
        if event.key == K_UP and direction != DOWN:
            direction = UP
        if event.key == K_RIGHT and direction != LEFT:
            direction = RIGHT
        if event.key == K_DOWN and direction != UP:
            direction = DOWN
        if event.key == K_LEFT and direction != RIGHT:
            direction = LEFT 

    #direçao
    if direction == UP:
        snake[0] = (snake[0][0] , snake[0][1] - 10) # ( x , y - 10)

    if direction == DOWN:
        snake[0] = (snake[0][0] , snake[0][1] + 10) # ( x , y + 10)

    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10 , snake[0][1]) # ( x  + 10, y )
    
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1] ) # ( x - 10, y )
    
    #continuaçao da cobra
    for i in range(len(snake) - 1 , 0 , -1):
        snake[i] = (snake[i-1][0] , snake[i-1][1]) #atualiza posiçao da cobra



    screen.fill((0,0,0)) #tela toda preta
    screen.blit(apple , apple_pos) #printa a maça
    
    for bl in borders: 
        screen.blit(borders_shape , bl)#printa a borda
    for pos in snake:
        screen.blit(snake_skin , pos) #printa a posiçao da cobra e todas as outras 

    pygame.display.update() 