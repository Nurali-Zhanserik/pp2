# this is for the circle which just gets commanded to move in any direction
# as the output you should see the screen with the red circle and it moves
import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 400))
done = False
color = (255, 0, 0)
x = 100
y = 100
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get(): # collects all the user input and loops through it
                if event.type == pygame.QUIT: # if one action is about quitting the window, the done becomes true whick stops the while loop
                        done = True
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (x,y), 25 )
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 25:  
                y -= 20  
        if pressed[pygame.K_DOWN] and y < 375:  
                y += 20  
        if pressed[pygame.K_LEFT] and x > 25:  
                x -= 20  
        if pressed[pygame.K_RIGHT] and x < 475:  
                x += 20        

        
        pygame.display.flip()
        clock.tick(40)