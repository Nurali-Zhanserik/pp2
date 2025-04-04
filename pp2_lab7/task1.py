# this is mickey clock and if you click "run" button you will see the clock 
import pygame 
import time
import math
pygame.init()


screen = pygame.display.set_mode((800, 600)) # creating the window
clock = pygame.time.Clock() # this is for controlling a fps rate


pygame.display.set_caption("Mickey clock") # just caption


leftarm = pygame.image.load("images/leftarm.png") #loads leftarm photo
rightarm = pygame.image.load("images/rightarm.png") # loads rightarm photo
mainclock = pygame.transform.scale(pygame.image.load("images/clock.png"), (800, 600)) # adjusting the size of clock

done = False

while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
 
    current_time = time.localtime() # getting time
    minute = current_time.tm_min # giving minutes
    second = current_time.tm_sec # giving seconds
    
     
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  
    
   
    screen.blit(mainclock, (0,0)) # drawing the clock in the window aftert loading 
    
   
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
   
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(60) 
    
pygame.quit()