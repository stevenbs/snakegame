import pygame
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green= (0,155,0)
yellow = (200,200,0)
hight = 800
width = 800
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((hight,width))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("images.png")
pygame.display.set_icon(icon)
img = pygame.image.load("snake.png")
img1 = pygame.image.load("images.png")
b_size =25
FPS =10
sFont = pygame.font.SysFont("comicsansms",25)
mFont = pygame.font.SysFont("comicsansms",50)
lFont = pygame.font.SysFont("comicsansms",80)
def pause():
    paused =True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:## pause() function.
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message("Paused",black,-100,size="large")
        message("Press C to continue or Q to quit",black,40)
        pygame.display.update()
        clock.tick(5)         
def score(score):
    text = mFont.render("score: "+ str(score),True,black)
    gameDisplay.blit(text,[0,0])
def randApple():
    randappleX= round (random.randrange(0,width-b_size)/float(b_size))*float(b_size)
    randappleY = round (random.randrange(0,hight-b_size)/float(b_size))*float(b_size)
    return randappleX,randappleY
def game_in():
    intro =True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key ==pygame.K_c:
                    intro = False
                    
        gameDisplay.fill(white)
        message("Welcome to Snake Game",green,-100,"large")
        message("Press C to Play or Press Q to Quit",black,50,"medium")
        pygame.display.update()
        clock.tick(15)

def snake(b_size,snakeList):
    for XnY in snakeList:
        gameDisplay.blit(img,(XnY[0],XnY[1]))
def text_objects(text,color,size):
    if size == "small":
        textS = sFont.render(text,True,color)
    elif size == "medium":
        textS = mFont.render(text,True,color)
    elif size == "large":
        textS = lFont.render(text,True,color)
    return textS,textS.get_rect()
def message(msg,color,y_displace=0, size = "small"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = (width/2),(hight/2)+y_displace
    gameDisplay.blit(textSurf,textRect)
def gameloop():
    gameExit = False
    gameOver = False
    lead_x=hight/2
    lead_y=width/2
    lead_x_change =0
    lead_y_change=0
    snakeList =[]
    snakelength =1

    randappleX,randappleY = randApple()
    while  not gameExit:
        if gameOver == True:
            message("Game Over",red,-50,size ="large")
            message("Press C to play again or Q to quit",black, 50,size ="medium")
            pygame.display.update()
        while gameOver == True:
           
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameOver = False
                    gameExit = True
            if event.type==pygame.KEYDOWN:
                    if event.key ==pygame.K_q:
                        gameExit = True
                        gameOver =False
                    if event.key ==pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type ==pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    lead_x_change=-b_size ##game loop to control the key event.
                    lead_y_change=0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change=b_size 
                    lead_y_change=0
                elif event.key == pygame.K_UP:
                    lead_y_change=-b_size 
                    lead_x_change=0
                elif event.key == pygame.K_DOWN:
                    lead_y_change=b_size 
                    lead_x_change=0
                elif event.key == pygame.K_p:
                    pause()
                
        if lead_x>= width or lead_x<0 or lead_y>=hight or lead_y<0:
            gameOver =True 
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gameDisplay.fill(white)
        gameDisplay.blit(img1,(randappleX,randappleY))
        snakeHead =[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakelength:## the method to add snake parts into the array and lengthen the snake.
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True          
        snake(b_size,snakeList)
        score(snakelength-1)
        pygame.display.update()
        if lead_x == randappleX and lead_y==randappleY:
             randappleX,randappleY = randApple()
             snakelength+=1
        for item in snakeList:
            if item == [randappleX,randappleY]:
                randappleX,randappleY = randApple()             
        clock.tick(FPS)    
    pygame.quit()
    quit()
game_in()
gameloop()
