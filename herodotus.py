#pyinstaller herodotus.py to convert to exe
import time
import luxor
import random
import os
import sys
time.sleep(10)
def customcontrols():
    global intro
    global currentBackground
    if(luxor.key == 97):
        luxor.spriteGraphical[1] = "<"
        luxor.spritex[1] = luxor.spritex[playerid]-1
        luxor.spritey[1] = luxor.spritey[playerid]
        luxor.key = 0
    elif(luxor.key == 100):
        luxor.spriteGraphical[1] = ">"
        luxor.spritex[1] = luxor.spritex[playerid]+1
        luxor.spritey[1] = luxor.spritey[playerid]
        luxor.key = 0
    elif(luxor.key == 119):
        luxor.spriteGraphical[1] = "^"
        luxor.spritex[1] = luxor.spritex[playerid]
        luxor.spritey[1] = luxor.spritey[playerid]-1
        luxor.key = 0
    elif(luxor.key == 115):
        luxor.spriteGraphical[1] = "V"
        luxor.spritex[1] = luxor.spritex[playerid]
        luxor.spritey[1] = luxor.spritey[playerid]+1
        luxor.key = 0
    elif(luxor.key == 114):
        python = sys.executable
        os.execl(python, python, *sys.argv)
def randomplace(spriteid):
    global playerid
    randomnumber = round(random.random()*3+1)
    if(randomnumber == 1):
        luxor.spritex[spriteid] = luxor.spritex[playerid]
        luxor.spritey[spriteid] = 0
        luxor.dy[spriteid] = 1
        luxor.dx[spriteid] = 0
    if(randomnumber == 2):
        luxor.spritex[spriteid] = 0
        luxor.spritey[spriteid] = luxor.spritey[playerid]
        luxor.dy[spriteid] = 0
        luxor.dx[spriteid] = 1
    if(randomnumber == 3):
        luxor.spritex[spriteid] = luxor.spritex[playerid]
        luxor.spritey[spriteid] = luxor.screenheight-1
        luxor.dy[spriteid] = -1
        luxor.dx[spriteid] = 0
    if(randomnumber == 4):
        luxor.spritex[spriteid] = luxor.screenlength-1
        luxor.spritey[spriteid] = luxor.spritey[playerid]
        luxor.dy[spriteid] = 0
        luxor.dx[spriteid] = -1
luxor.changeScreen(25,25)
area = 1
intro = 0
killcounter = 0
score = 0
health = 3
playerid = 7
timer = 0
loss = False
regen = False
slowTime = False
pauseTime = False
flux = False
difficulty = 0
currentBackground = luxor.backcolor.blue
innerspeech = ""
luxor.sprite(12,12,"O",luxor.colors.magenta,playerid, True)
luxor.sprite(12,13,"V",luxor.colors.white,1,True)
luxor.sprite(12,10,"0",luxor.colors.red,2,False)
while(area == 1):
    if(difficulty == 1):
        luxor.refreshRate = .2
    if(difficulty == 2):
        luxor.refreshRate = .12
    if(difficulty == 3):
        luxor.refreshRate = .09
    if(luxor.spriteonsprite(2,playerid)):
        health -= 1
        currentBackground = luxor.backcolor.red
    else:
        currentBackground = luxor.backcolor.blue
    if(health <= 0):
        luxor.dx[2] = 0
        luxor.dy[2] = 0
        currentBackground = luxor.backcolor.red
        innerspeech = "you lose - press 'r' to restart"
        loss = True
        health = 0
    luxor.refreshbackground(" ", luxor.colors.green, backgroundcolor = currentBackground)
    #luxor.createborder(luxor.colors.red)
    if(luxor.spriteonsprite(1,2) or luxor.spriteonsprite(2,playerid) or intro == 1):
        if(luxor.spriteonsprite(1,2)):
            killcounter += 1
            score += 1
        randomplace(2)
        intro = 2
    if((killcounter == 6 and difficulty == 1) or (killcounter == 9 and difficulty == 2) or (killcounter == 11 and difficulty == 3)):
        area = 2
        luxor.sprite(luxor.spritex[playerid],2,"8",luxor.colors.green,3,False)
        luxor.dy[3]=1
        luxor.dx[3]=0
    luxor.speech1 = "score: "+str(score)+" Health: "+str(health)
    luxor.speech2 = innerspeech
    if(intro == 0):
        luxor.speech1 = "1-easy, 2-medium, 3-hard"
        innerspeech = ""
    if((luxor.key == 49 or luxor.key == 50 or luxor.key == 51) and intro == 0):
        intro = 1
        if(round(random.random()*3) == 3):
            luxor.playsong("pressStart.mp3")
        else:
            luxor.playsong("megalovania.mp3")
        if(luxor.key == 49):
            difficulty = 1
        if(luxor.key == 50):
            difficulty = 2
        if(luxor.key == 51):
            difficulty = 3
        
    customcontrols()
    luxor.collisions()
    luxor.movement()
    luxor.graphics()
    if(luxor.key==27):
        break
    
while(area == 2):
    if(difficulty == 1):
        luxor.refreshRate = .15
    if(difficulty == 2):
        luxor.refreshRate = .11
    if(difficulty == 3):
        luxor.refreshRate = .04
    if(luxor.spriteonsprite(2,playerid)):
        health -= 1
        currentBackground = luxor.backcolor.red
    else:
        currentBackground = luxor.backcolor.blue
    if(health <= 0):
        luxor.dx[2] = 0
        luxor.dy[2] = 0
        luxor.dx[3] = 0
        luxor.dy[3] = 0
        currentBackground = luxor.backcolor.red
        innerspeech = "you lose - press 'r' to restart"
        loss = True
        health = 0
    luxor.refreshbackground(" ", luxor.colors.blue, backgroundcolor = currentBackground)
    luxor.createborder(luxor.colors.cyan)
    if(luxor.spriteonsprite(1,2) or luxor.spriteonsprite(2, playerid)):
        if(luxor.spriteonsprite(1,2)):
            score += 1
            killcounter += 1
        randomplace(2)
    if(luxor.spriteonsprite(1,3) or luxor.spriteonsprite(3,playerid)):
        if(luxor.spriteonsprite(1,3)):
            score += 2
        randomplace(3)
    luxor.speech1 = "score: "+str(score)+" health: "+str(health)
    luxor.speech2 = innerspeech
    if((killcounter == 14 and difficulty == 1) or (killcounter == 19 and difficulty == 2) or (killcounter == 29 and difficulty == 3)):
        area = 3
        luxor.sprite(luxor.spritex[playerid],3,"0",luxor.colors.red,4,False)
        luxor.dy[4]=1
        luxor.dx[4]=0
    customcontrols()
    luxor.collisions()
    luxor.movement()
    luxor.graphics()
    if(luxor.key==27):
        break
while(area == 3):
    if(difficulty == 1):
        luxor.refreshRate = .17
    if(difficulty == 2):
        luxor.refreshRate = .1
    if(difficulty == 3):
        luxor.refreshRate = .04
    if(luxor.spriteonsprite(2,playerid) or luxor.spriteonsprite(4,playerid)):
        health -= 1
        currentBackground = luxor.backcolor.red
    else:
        currentBackground = luxor.backcolor.black
    if(health <= 0):
        luxor.dx[2] = 0
        luxor.dy[2] = 0
        luxor.dx[3] = 0
        luxor.dy[3] = 0
        luxor.dx[4] = 0
        luxor.dy[4] = 0
        currentBackground = luxor.backcolor.red
        innerspeech = "you lose - press 'r' to restart"
        loss = True
        health = 0
    luxor.refreshbackground(" ", luxor.colors.green, backgroundcolor = currentBackground)
    #luxor.createborder(luxor.colors.white)
    if(luxor.spriteonsprite(1,2) or luxor.spriteonsprite(2,playerid)):
        if(luxor.spriteonsprite(1,2)):
            score += 1
            killcounter += 1
        randomplace(2)
    if(luxor.spriteonsprite(1,3) or luxor.spriteonsprite(3,playerid)):
        if(luxor.spriteonsprite(1,3)):
            score += 2
        randomplace(3)
    if(luxor.spriteonsprite(1,4) or luxor.spriteonsprite(4,playerid)):
        if(luxor.spriteonsprite(1,4)):
            score += 1
            killcounter += 1
        randomplace(4)
    luxor.speech1 = "score: "+str(score)+" health: "+str(health)
    luxor.speech2 = innerspeech
    if((killcounter == 27 and difficulty == 1) or (killcounter == 40 and difficulty == 2) or (killcounter == 56 and difficulty == 3)):
        area = 4
        luxor.sprite(luxor.spritex[playerid],5,"0",luxor.colors.red,5,False)
        luxor.dy[5]=1
        luxor.dx[5]=0
        luxor.sprite(luxor.spritex[playerid],4,"H",luxor.colors.cyan,8,False)
        luxor.dy[8]=1
        luxor.dx[8]=0
    customcontrols()
    luxor.collisions()
    luxor.movement()
    luxor.graphics()
    if(luxor.key==27):
        break
while(area == 4):
    if(difficulty == 1):
        luxor.refreshRate = .2
    if(difficulty == 2):
        luxor.refreshRate = .1
    if(difficulty == 3):
        luxor.refreshRate = .05
    if(luxor.spriteonsprite(2,playerid) or luxor.spriteonsprite(4,playerid) or luxor.spriteonsprite(5,playerid)):
        health -= 1
        currentBackground = luxor.backcolor.red
    else:
        currentBackground = luxor.backcolor.black
    if(health <= 0):
        luxor.dx[2] = 0
        luxor.dy[2] = 0
        luxor.dx[3] = 0
        luxor.dy[3] = 0
        luxor.dx[4] = 0
        luxor.dy[4] = 0
        luxor.dx[5] = 0
        luxor.dy[5] = 0
        luxor.dx[8] = 0
        luxor.dy[8] = 0
        currentBackground = luxor.backcolor.red
        innerspeech = "you lose - press 'r' to restart"
        loss = True
        health = 0
    luxor.refreshbackground(" ", luxor.colors.green, backgroundcolor = currentBackground)
    luxor.createborder(luxor.colors.white)
    if(luxor.spriteonsprite(1,2) or luxor.spriteonsprite(2,playerid)):
        if(luxor.spriteonsprite(1,2)):
            score += 1
            killcounter += 1
        randomplace(2)
    if(luxor.spriteonsprite(1,3) or luxor.spriteonsprite(3,playerid)):
        if(luxor.spriteonsprite(1,3)):
            score += 2
        randomplace(3)
    if(luxor.spriteonsprite(1,4) or luxor.spriteonsprite(4,playerid)):
        if(luxor.spriteonsprite(1,4)):
            score += 1
            killcounter += 1
        randomplace(4)
    if(luxor.spriteonsprite(1,5) or luxor.spriteonsprite(5,playerid)):
        if(luxor.spriteonsprite(1,5)):
            score += 1
            killcounter += 1
        randomplace(5)
    if(luxor.spriteonsprite(1,8) or luxor.spriteonsprite(8,playerid)):
        if(luxor.spriteonsprite(1,8)):
            health += 1
        luxor.spritex[8] = luxor.spritex[playerid]
        luxor.spritey[8] = luxor.spritey[playerid]
        luxor.dx[8] = 0
        luxor.dy[8] = 0
        regen = False
    if(round(random.random()*8) == 1 and regen == False):
        randomplace(8)
        regen = True
    if((killcounter == 53 and difficulty == 1) or (killcounter == 70 and difficulty == 2) or (killcounter == 100 and difficulty == 3)):
        area = 5
        luxor.sprite(luxor.spritex[playerid],2,"0",luxor.colors.red,6,False)
        luxor.dy[6]=1
        luxor.dx[6]=0
    luxor.speech1 = "score: "+str(score)+" health: "+str(health)
    luxor.speech2 = innerspeech
    customcontrols()
    luxor.collisions()
    luxor.movement()
    luxor.graphics()
    if(luxor.key==27):
        break
while(area == 5):
    if(difficulty == 1):
        luxor.refreshRate = .18
    if(difficulty == 2):
        luxor.refreshRate = .09
    if(difficulty == 3):
        luxor.refreshRate = .06
    if(flux):
        flux = False
    else:
        flux = True
    if(luxor.spriteonsprite(2,playerid) or luxor.spriteonsprite(4,playerid) or luxor.spriteonsprite(5,playerid) or luxor.spriteonsprite(6,playerid)):
        health -= 1
        currentBackground = luxor.backcolor.red
    else:
        currentBackground = luxor.backcolor.black
    if(health <= 0):
        luxor.dx[2] = 0
        luxor.dy[2] = 0
        luxor.dx[3] = 0
        luxor.dy[3] = 0
        luxor.dx[4] = 0
        luxor.dy[4] = 0
        luxor.dx[5] = 0
        luxor.dy[5] = 0
        luxor.dx[6] = 0
        luxor.dy[6] = 0
        luxor.dx[8] = 0
        luxor.dy[8] = 0
        currentBackground = luxor.backcolor.red
        innerspeech = "you lose - press 'r' to restart"
        loss = True
        health = 0
    if(round(random.random()*10) == 1 and slowTime == False):
        slowTime = True
        timer = 15
    if(slowTime):
        luxor.spritecolor[1] = luxor.colors.purple
        luxor.spritecolor[7] = luxor.colors.purple
        currentBackground = luxor.backcolor.pink
    else:
        luxor.spritecolor[1] = luxor.colors.white
        luxor.spritecolor[7] = luxor.colors.magenta
        currentBackground = luxor.backcolor.black
    if(health == 0):
        currentBackground = luxor.backcolor.red
    if(timer == 0):
        slowTime = False
        pauseTime = False
    if((killcounter == 80 and difficulty == 1) or (killcounter == 100 and difficulty == 2) or (killcounter == 150 and difficulty == 3)):
        area = 6
        currentBackground = luxor.backcolor.green
    if(slowTime and luxor.key == 32):
        pauseTime = True
    luxor.refreshbackground(" ", luxor.colors.green, backgroundcolor = currentBackground)
    luxor.createborder(luxor.colors.magenta)
    if(luxor.spriteonsprite(1,2) or luxor.spriteonsprite(2,playerid)):
        if(luxor.spriteonsprite(1,2)):
            score += 1
            killcounter += 1
        randomplace(2)
    if(luxor.spriteonsprite(1,3) or luxor.spriteonsprite(3,playerid)):
        if(luxor.spriteonsprite(1,3)):
            score += 2
        randomplace(3)
    if(luxor.spriteonsprite(1,4) or luxor.spriteonsprite(4,playerid)):
        if(luxor.spriteonsprite(1,4)):
            score += 1
            killcounter += 1
        randomplace(4)
    if(luxor.spriteonsprite(1,5) or luxor.spriteonsprite(5,playerid)):
        if(luxor.spriteonsprite(1,5)):
            score += 1
            killcounter += 1
        randomplace(5)
    if(luxor.spriteonsprite(1,6) or luxor.spriteonsprite(6,playerid)):
        if(luxor.spriteonsprite(1,6)):
            score += 1
            killcounter += 1
        randomplace(6)
    if(luxor.spriteonsprite(1,8) or luxor.spriteonsprite(8,playerid)):
        if(luxor.spriteonsprite(1,8)):
            health += 1
        luxor.spritex[8] = luxor.spritex[playerid]
        luxor.spritey[8] = luxor.spritey[playerid]
        luxor.dx[8] = 0
        luxor.dy[8] = 0
        regen = False
    if(round(random.random()*6) == 1 and regen == False):
        randomplace(8)
        regen = True
    luxor.speech1 = "score: "+str(score)+" health: "+str(health)
    luxor.speech2 = innerspeech
    customcontrols()
    luxor.collisions()
    if(slowTime and pauseTime and flux):
        timer -= 1
    else:
        luxor.movement()
    luxor.graphics()
    if(luxor.key==27):
        break
print("you win")
while(True):
    customcontrols()
    if(luxor.key==27):
        break