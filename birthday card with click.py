import pygame
import time
playing = True
pygame.init()
time1 = 3
screen = pygame.display.set_mode((600,600))
card1 = pygame.image.load("cake.jpg") 
card2 = pygame.image.load("back.jpg") 
card3 = pygame.image.load("present.jpg") 
font = pygame.font.SysFont("Times New Roman",72)
while playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                time1 = 3
                screen.blit(card1,(0,0)) 
                text1 = font.render("happy birthday",True,"black")
                screen.blit(text1,(100,50))
                pygame.display.update()
                
                time.sleep(time1)
                
                screen.blit(card2,(0,0)) 
                text2 = font.render("happy birthday",True,"black")
                screen.blit(text2,(100,50))
                pygame.display.update()
                
                time.sleep(time1)
                
                screen.blit(card3,(0,0)) 
                text3 = font.render("happy birthday",True,"black")
                screen.blit(text3,(100,50))
                pygame.display.update()
                
                time.sleep(time1)
        if event.type == pygame.MOUSEBUTTONUP:
                        time1 = 3
  
    screen.fill("white")
    pygame.display.update()

