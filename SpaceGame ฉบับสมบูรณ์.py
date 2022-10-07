import pgzrun
import os
from random import randint


def draw():

    if StatusGame == 0:
        screen.blit('home2', (0, 0))
        #message = "Are you ready, press Enter key to play."
        # screen.draw.text(message,topleft=(350,450),fontsize=40)

    elif StatusGame == 1:
        screen.clear()
        #screen.blit('menu2' ,(200,0))

        screen.blit('ff', (0, 0))
        screen.blit('ff', (1000, 0))
        if rand == 1:
            screen.blit('bbg1', (200, 0))
        elif rand == 2:
            screen.blit('bbg2', (200, 0))
        elif rand == 3:
            screen.blit('bbg3', (200, 0))
        elif rand == 4:
            screen.blit('bbg4', (200, 0))
        elif rand == 5:
            screen.blit('bbg5', (200, 0))
        elif rand == 6:
            screen.blit('bbg6', (200, 0))
        elif rand == 7:
            screen.blit('bbg7', (200, 0))
        elif rand == 8:
            screen.blit('bbg8', (200, 0))
        elif rand == 9:
            screen.blit('bbg9', (200, 0))
        elif rand == 10:
            screen.blit('bbg10', (200, 0))

        ship.draw()
        alien.draw()
        p1_1.draw()
        p2_1.draw()
        hp1.draw()
        hp2.draw()
        a.draw()
        d.draw()
        left.draw()
        right.draw()
        space.draw()
        en.draw()

        for bullet in bullets:
            bullet.draw()

        for bullet in bulleth:
            bullet.draw()

        for heart in hearts_ship:
            heart.draw()
        for heart in hearts_alien:
            heart.draw()

    elif StatusGame == 4:
        screen.clear()
        screen.blit('sl1', (0, 0))
        message = "Please space to select your ship"
        screen.draw.text(message, topleft=(290, 500),
                         fontsize=60, color='yellow')
        picship1.draw()
        picship2.draw()
        picship3.draw()
        fig.draw()

    elif StatusGame == 5:
        screen.clear()
        screen.blit('sl2', (0, 0))
        message = "Please space to select your ship"
        screen.draw.text(message, topleft=(290, 500),
                         fontsize=60, color='yellow')
        picship1.draw()
        picship2.draw()
        picship3.draw()
        fig2.draw()

    elif StatusGame == 7:
        screen.clear()
        screen.blit('w2', (0, 0))

    elif StatusGame == 8:
        screen.clear()
        screen.blit('w1', (0, 0))


def on_key_down(key):
    global StatusGame, Score, Time, fig, select, spt, spt2, check, select2, fig2, D_heart, D_heart2, hearts_ship, hearts_alien, heartPOS_alien, heartPOS_ship, alien, ship, rand

    if StatusGame == 7 or StatusGame == 8:
        rand = randint(1, 10)
        D_heart = 1
        D_heart2 = 1
        Max = 3
        for r in range(Max):
            hearts_ship[r].image = 'heart'
            hearts_alien[r].image = 'heart'
        '''for n in range(D_heart):
            hearts_ship[n].image='heart'
        '''

        for n in range(Max_heart):
            hearts_ship.append(Actor('heart'))
            hearts_ship[n].pos = heartPOS_ship[n]
        for n in range(Max_heart):
            hearts_alien.append(Actor('heart'))
            hearts_alien[n].pos = heartPOS_alien[n]

        ship = Actor('ship2')
        alien = Actor('ship2r')
        ship.pos = (WIDTH/2, HEIGHT-40)
        alien.pos = (WIDTH/2, 40)

    if StatusGame == 0:
        if key == keys.RETURN:
            # start_game()
            StatusGame = 4

    elif StatusGame == 2:
        if key == keys.SPACE:
            start_game()

    elif StatusGame == 4:
        if key == key.RIGHT:
            fig.x += 200
            select += 1
            if fig.x > 850:
                fig.x = 850
            if select > 3:
                select = 3

        if key == key.LEFT:
            fig.x -= 200
            select -= 1
            if select < 1:
                select = 1

            if fig.x < 450:
                fig.x = 450

        if key == key.SPACE:
            spt = select
            spt_1()
            StatusGame = 5

    elif StatusGame == 5:

        if key == key.RIGHT:

            fig2.x += 200
            select2 += 1
            if fig2.x > 850:
                fig2.x = 850
            if select2 > 3:
                select2 = 3

        if key == key.LEFT:
            fig2.x -= 200
            select2 -= 1
            if select2 < 1:
                select2 = 1
            if fig2.x < 450:
                fig2.x = 450

        if key == key.SPACE:
            spt2 = select2
            spt_2()
            StatusGame = 1

    elif StatusGame == 1:
        if key == keys.RETURN:
            bullets.append(Actor('bullet'))
            last1 = len(bullets)
            bullets[last1-1].pos = ship.pos
            sounds.laser.play()

        if key == keys.SPACE:
            bulleth.append(Actor('bullet2'))
            last2 = len(bulleth)
            bulleth[last2-1].pos = alien.pos
            sounds.laser.play()

    elif StatusGame == 7 or StatusGame == 8:
        if key == keys.RETURN:
            StatusGame = 4

            # exit()

#######################################


def spt_1():
    global spt, ship
    if spt == 1:
        ship.image = 'ship'
    elif spt == 2:
        ship.image = 'ship2'
    elif spt == 3:
        ship.image = 'ship3'


def spt_2():
    global spt2, alien
    if spt2 == 1:
        alien.image = 'shipr'
    elif spt2 == 2:
        alien.image = 'ship2r'
    elif spt2 == 3:
        alien.image = 'ship3r'


def update():
    global blood, blue, sumer, StatusGame, Max_heart, speed, time

    if keyboard.LEFT:
        ship.x -= speed
    if ship.left < 200:
        ship.left = 200
    elif keyboard.RIGHT:
        ship.x += speed
    if ship.right > 1000:
        ship.right = 1000

    if keyboard.A:
        alien.x -= speed
    if alien.left < 200:
        alien.left = 200
    elif keyboard.D:
        alien.x += speed
    if alien.right > 1000:
        alien.right = 1000

    for bullet in bullets:
        bullet.y -= 20
        if bullet.top < 0:
            bullets.remove(bullet)

    for bullet in bulleth:
        bullet.y += 20
        if bullet.top > HEIGHT:
            bulleth.remove(bullet)

    # เช็คกระสุน
    for bullet in bulleth:
        if bullet.colliderect(ship):
            bulleth.remove(bullet)

            heart_1()

    for bullet in bullets:
        if bullet.colliderect(alien):
            bullets.remove(bullet)
            heart_2()


def start_game():
    global StatusGame, D_heart, D_heart2
    if StatusGame == 4:
        D_heart = 1
        D_heart2 = 1
    else:
        StatusGame = 1


def ship_boom():
    global ship
    # ship=Actor('boom2')
    ship.image = 'boom2'
    print('boom')

    clock.schedule(alien_win, 0.5)


def aline_boom():
    global alien
    # alien=Actor('boom2')
    alien.image = 'boom2'
    clock.schedule(ship_win, 0.5)


def alien_win():
    global StatusGame, ship
    StatusGame = 7


def ship_win():
    global StatusGame, alien
    StatusGame = 8


def heart_1():
    global blood, blue, sumer, StatusGame, Max_heart, heartPOS_ship, D_heart, hearts_ship, StatusGame
    if D_heart == 3:
        print(D_heart)
        ship_boom()
        StatusGame = 99

    if D_heart < 3:
        print(D_heart)
        for n in range(D_heart):
            hearts_ship[n].image = 'heart2'
    D_heart += 1


def heart_2():
    global blood, blue, sumer, StatusGame, Max_heart, heartPOS_ship, D_heart2, hearts_alien, StatusGame
    if D_heart2 == 3:
        aline_boom()
        StatusGame = 99

    if D_heart2 < 3:
        for a in range(D_heart2):
            hearts_alien[a].image = 'heart3'
    D_heart2 += 1


w1 = Actor('w1')
w2 = Actor('w2')
rand = randint(1, 10)
spt = 0  # ship_statut
spt2 = 0
check = 0
picship1 = Actor('ship')
picship2 = Actor('ship2')
picship3 = Actor('ship3')
picship1.x = 450
picship2.x = 650
picship3.x = 850
picship1.y = 350
picship2.y = 350
picship3.y = 350
fig = Actor('fig')
fig.x = 450
fig.y = 450
fig2 = Actor('fig')
fig2.x = 450
fig2.y = 450
WIDTH = 1200
HEIGHT = 600
MaxTime = 2
StatusGame = 0
Score = 0
Time = 0
select = 1
select2 = 1
ship = Actor('ship2')
alien = Actor('ship2r')
a = Actor('a')
d = Actor('d')
left = Actor('left')
right = Actor('right')
space = Actor('space')
en = Actor('en')
a.pos = 1050, 450
d.pos = 1150, 450
left.pos = 50, 50
right.pos = 150, 50
space.pos = 1100, 520
en.pos = 100, 125
hearts_ship = []
hearts_alien = []
heartPOS_ship = [(100, 300), (100, 350), (100, 400)]
heartPOS_alien = [(1100, 300), (1100, 350), (1100, 400)]
Max_heart = 3
D_heart = 1
D_heart2 = 1
alien.pos = (WIDTH/2, 40)
ship.pos = (WIDTH/2, HEIGHT-40)
bullets = []
bulleth = []
p1_1 = Actor('p1')
p2_1 = Actor('p2')
hp1 = Actor('hp1')
hp2 = Actor('hp2')

sounds.s1.play()


p1_1.pos = 100, 520
p2_1.pos = 1100, 120
hp1.pos = 100, 220
hp2.pos = 1100, 220
speed = 10
for n in range(Max_heart):
    hearts_ship.append(Actor('heart'))
    hearts_ship[n].pos = heartPOS_ship[n]
for n in range(Max_heart):
    hearts_alien.append(Actor('heart'))
    hearts_alien[n].pos = heartPOS_alien[n]

pgzrun.go()
