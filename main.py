import pygame as pg
import numpy as np
from time import sleep

pg.init()

# colors
white = (255,255,255)
blue = (0,100,100)
brown = (150,75,0)

display_width = 400
display_height = 800
gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption("Car Game")

# car imgae
car_image = pg.image.load("0.jpg")
car_image = pg.transform.scale(car_image, (180,180))

def car(x,y):
    gameDisplay.blit(car_image, (x,y))

def obstacle(x,y,w,h,color):
    pg.draw.rect(gameDisplay,color,[x,y,w,h])

crash = False
x = 0
y = display_height - 180
ob_x = 0
ob_y = 0
ob_w = 180
ob_h = 180

car_position = 0 # 0:left 1:right
while not crash:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                print("LEFT")
                x = 0
                car_position = 0
            elif event.key == pg.K_RIGHT:
                print("RIGHT")
                x = 220
                car_position = 1

    gameDisplay.fill(white)
    # draw center line
    pg.draw.line(gameDisplay, (0,0,0), (200,0),(200,800),40)
    # obstacle
    x_pos = [0,220]
    obstacle(ob_x, ob_y, ob_w, ob_h, (255,30,20))
    obstacle_speed = 90
    ob_y += obstacle_speed
    #crash judgement
    if ob_y > 800 - 300:
        if x_pos.index(ob_x) == car_position:
            print("Game Over")
            crash = True
    if ob_y > 800 - 180:
        # restart
        ob_y = 0
        # ob_xを選び直す
        ob_x = x_pos[np.random.randint(2)]
    car(x,y)

    pg.display.update()
