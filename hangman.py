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
font3 = pygame.font.SysFont("Times New Roman", 24)

def display():
    i=25
    j=0
    for x in string.ascii_lowercase:
        l.append(x)
        
        text2 = font3.render(x,True,(255,255,255))
        arr.append(pygame.Rect(pygame.draw.rect(win,(255,255,255),(30+i,485,25,25),2)))
        win.blit(text2,(40+i,485))
        j=j+1
        i=i+30
    
    pygame.display.update()
    
font = pygame.font.SysFont("Times New Roman", 26)
text = font.render(guess, True, (255, 255, 255))
win.blit(text,(230,380))

while True:
    font1 = pygame.font.SysFont("Times New Roman", 36)
    name = font1.render("HANGMAN", True, (255, 255, 255))
    win.blit(name,(350,50)) 
    if cnt1==0:
        start_text = font.render("Start guessing", True, (255, 255, 255))
        win.blit(start_text,(200,100))
    display()
    if cnt==1:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.display.update()
                            
    if cnt==2:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.display.update()
    if cnt==3:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.display.update()
    if cnt==4:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),5)
        pygame.display.update()
    if cnt==5:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),5)
        pygame.display.update()
    if cnt==6:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(275,265),5)
    if cnt==7:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(275,265),5)
        pygame.draw.line(win,(248,248,255),(250,265),(225,300),5)
    if cnt==8:
        pygame.draw.line(win,(248,248,255),(100,150),(100,350),5)
        pygame.draw.line(win,(248,248,255),(100,150),(300,150),5)
        pygame.draw.line(win,(248,248,255),(70,350),(130,350),5)
        pygame.draw.line(win,(248,248,255),(250,150),(250,185),5)
        pygame.draw.circle(win,(248,248,255),(250,210),25,5)
        pygame.draw.line(win,(248,248,255),(250,235),(250,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(225,265),5)
        pygame.draw.line(win,(248,248,255),(250,247),(275,265),5)
        pygame.draw.line(win,(248,248,255),(250,265),(225,300),5)
        pygame.draw.line(win,(248,248,255),(250,265),(275,300),5)
        text3 = font.render(" WRONG ! Game Over!!!", True, (255, 0, 0))
        win.blit(text3,(420,380))
        pygame.display.update()
        break
    if guess==s:
        text4 = font.render("  CORRECT ", True, (0, 255, 0))
        win.blit(text4,(420,380))
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
                    screen = pygame.display.get_surface()
                    screen.fill(pygame.Color("black")) 
                    text1 = font.render(guess, True, (255, 255, 255))
                    win.blit(text1,(230,380))
                    pygame.display.update()
    
pygame.time.delay(10000)                
pygame.quit()
