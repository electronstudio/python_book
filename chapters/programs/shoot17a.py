from rlzero import *
import random

WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

background = Sprite("background.png")
player = Sprite("player.png", (200, 730))
enemies = []
bullets = []
bombs = []
