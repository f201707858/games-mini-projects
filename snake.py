import pygame
import random
import time

WIDTH = 800
HEIGHT = 600
FPS = 2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKEBITE")
clock = pygame.time.Clock()

#Creating fonts
myfont=pygame.font.SysFont('Times New Roman', 80)
myfont_win=pygame.font.SysFont('Times New Roman', 50)

#snake initial segment
segment_width = 15
segment_height = 15
segment_margin = 3

#snake speed
x_change = segment_width + segment_margin
y_change = 0

#length

count=5
score=0
points=5




class Segment(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([segment_width, segment_height])
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


        





class FOOD(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        #positioning
        X=[]
        Y=[]
        X.extend(range(100,700,15))
        Y.extend(range(100,490,15))
        x1=random.randint(0,39)#40
        y1=random.randint(0 ,25)#26
        self.rect.x=X[x1]
        self.rect.y=Y[y1]
        self.speedx=0
        self.speedy=0




allspriteslist = pygame.sprite.Group()
sprites=pygame.sprite.Group()


snake_segments = []
for i in range(5):
    x = 160 - (segment_width + segment_margin) * i
    y = 103
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)
 

        


food=FOOD()
sprites.add(food)





# Game loop
running = True
while running:

    clock.tick(FPS)
    

#game over on touching screen
    
        
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change == 0:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT and x_change == 0:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP and y_change == 0:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN and y_change == 0:
                x_change = 0
                y_change = (segment_height + segment_margin)
    allspriteslist.remove(snake_segments.pop())
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)


    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    

        

    

 
 

    # Update
    allspriteslist.update()
    sprites.update()
    hit = pygame.sprite.collide_circle(segment,food)
    if hit == True:
        score+=points
        food.kill()
        food = FOOD()
        sprites.add(food)
        x = snake_segments[0].rect.x + x_change
        y = snake_segments[0].rect.y + y_change
        segment = Segment(x, y)
 
    # Insert new segment into the list
        snake_segments.insert(0, segment)
        allspriteslist.add(segment)
 
        
    # Insert new segment into the list
        snake_segments.insert(0, segment)
        allspriteslist.add(segment)
 

    # Draw / render
    screen.fill(BLACK)
    #draw game
    pygame.draw.aalines(screen,GREEN,True, [[100,100], [700,100],[700,500],[100,500]],1)
    

    
    allspriteslist.draw(screen)
    sprites.draw(screen)
    textsurface = myfont_win.render(str(score), False, WHITE)
    screen.blit(textsurface,(350,20))

    # *after* drawing everything, flip the display
    if snake_segments[0].rect.x < 100 or snake_segments[0].rect.x > 685  or snake_segments[0].rect.y< 85 or snake_segments[0].rect.y>= 485 :
        screen.fill(BLACK)
        textsurface = myfont.render('GAME OVER', False, WHITE)
        screen.blit(textsurface,(200,250))
        running = False
    else :
        for i in range(1,count):
            if snake_segments[0].rect.center == snake_segments[i].rect.center and hit != True :
                screen.fill(BLACK)
                textsurface = myfont.render('GAME OVER', False, WHITE)
                screen.blit(textsurface,(200,250))
                
                print i
                print snake_segments[0].rect.center
                print snake_segments[i].rect.center
                running = False
   
                
    pygame.display.flip()

pygame.quit()







