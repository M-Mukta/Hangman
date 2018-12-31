# -*- coding: utf-8 -*-
import string
import pygame
import random

pygame.init()
win=pygame.display.set_mode((900,600))
pygame.display.set_caption("Hangman")
run=True
s1=["p y t h o n","m u k t a","s t r i n g","h a n g m a n"]
s=random.choice(s1)
guess=""
r=0
print(len(s))
while r<len(s):
    if s[r] != " ":
        guess=guess+"_"
    else:
        guess+=" "
    r=r+1
    
cnt=0
arr=[]
l=[]
cnt1=0
def display():
    pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
    pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
    pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
    pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
    i=25
    j=0
    for x in string.ascii_lowercase:
        l.append(x)
        text2 = font.render(x,True,(255,255,255))
        arr.append(pygame.Rect(pygame.draw.rect(win,(255,255,255),(30+i,430,25,25),2)))
        win.blit(text2,(40+i,430))
        j=j+1
        i=i+30
    
    pygame.display.update()
    
    

font = pygame.font.SysFont("Times New Roman", 24)
text = font.render(guess, True, (255, 255, 255))
win.blit(text,(230,380))

while True:
    
    display()
    if cnt1==0:
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(275,265),5)
        pygame.draw.line(win,(248,248,255),(250,265),(225,300),5)
        pygame.draw.line(win,(248,248,255),(250,265),(275,300),5)
        pygame.display.update()
    if cnt==1:
        pygame.draw.circle(win,(248,248,255),(250,210),25,2)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),2)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),2)
        pygame.draw.line(win,(248,248,255),(250,247),(275,265),2)
        pygame.draw.line(win,(248,248,255),(250,265),(225,300),2)
        pygame.display.update()
                            
    if cnt==2:
        pygame.draw.circle(win,(248,248,255),(250,210),25,2)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),2)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),2)
        pygame.draw.line(win,(248,248,255),(250,247),(275,265),2)
        pygame.display.update()
    if cnt==3:
        pygame.draw.circle(win,(248,248,255),(250,210),25,2)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),2)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),2)
        pygame.display.update()
    if cnt==4:
        pygame.draw.circle(win,(248,248,255),(250,210),25,2)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),2)
        pygame.display.update()
    if cnt==5:
        pygame.draw.circle(win,(248,248,255),(250,210),25,2)
        pygame.display.update()
    if cnt==6:
        text3 = font.render("Game Over!", True, (255, 255, 255))
        win.blit(text3,(380,380))
        pygame.display.update()
        break
    if guess==s:
        text4 = font.render("WORD FOUND", True, (255, 255, 255))
        win.blit(text4,(380,380))
        pygame.display.update()
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            c=0
            for itr in range(26):
                if arr[itr].collidepoint(x, y):
                    if l[itr] in s:
                        while c<len(s):
                            
                            if s[c]==l[itr]:
                                guess=guess[:c]+l[itr]+guess[c+1:]
                            c=c+1
                    else:
                        cnt=cnt+1    
                        cnt1=cnt1+1
                    print(guess,cnt)
                    screen = pygame.display.get_surface()
                    screen.fill(pygame.Color("black")) 
                    text1 = font.render(guess, True, (255, 255, 255))
                    win.blit(text1,(230,380))
                    pygame.display.update()
    
pygame.time.delay(1000)                
pygame.quit()
