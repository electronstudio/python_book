from rlzero import *
import random
import math

WIDTH = 600
HEIGHT = 800

player = Sprite("alien.png", (300, 780))
player.vx = 0   # horizontal velocity
player.vy = 1   # vertical velocity

lines = []          # list of tuples of horizontal lines of walls
wall_gradient = -3  # steepness of wall
left_wall_x = 200   # x-coordinate of wall
distance = 0        # how far player has travelled
time = 15           # time left until game ends
playing = False     # True when in game, False when on title screen
best_distance = 0   # remember the highest distance scored

def draw():
    if playing: # we are in game
        for i in range(0, len(lines)): # draw the walls
            x, x2, color = lines[i]
            draw_line(0, i, int(x), i, color)
            draw_line(int(x + x2), i, WIDTH, i, color)
        player.draw()
    else:   # we are on title screen
        draw_text("PRESS SPACE TO START", 150, 300, 30, GREEN)
        draw_text("BEST DISTANCE: "+str(int(best_distance / 10)),
                  170, 400,  30, GREEN)
    draw_text("SPEED: " + str(int(player.vy)),
              0, 0, 30, GREEN)
    draw_text("DISTANCE: " + str(int(distance / 10)),
              200, 0, 30, GREEN)
    draw_text("TIME: " + str(int(time)),
              480, 0, 30, GREEN)


def update(delta):
    global playing, distance, time
    if playing:
        wall_collisions()
        scroll_walls()
        generate_lines()
        player_input()
        timer(delta)
    elif keyboard.space:
        playing = True
        distance = 0
        time = 10


def player_input():
    pass

def generate_lines():
    pass

generate_lines()

def scroll_walls():
    pass

def wall_collisions():
    pass

def timer(delta):
    pass

def on_mouse_move(pos):
    pass
