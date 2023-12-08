import pygame
from random import *
from operator import attrgetter
# Game size
GAME_WIDTH, GAME_HEIGHT = 1280, 550
GAME_X, GAME_Y = 0, 170

# Window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# Leaderboard
LEADERBOARD_WIDTH, LEADERBOARD_HEIGHT = 320, 150
LEADERBOARD_X, LEADERBOARD_Y = 800, 10

# Events
EVENTS_WIDTH, EVENTS_HEIGHT = 600, 150
EVENTS_X, EVENTS_Y = 350, 10

# Maps
MAPS = 4
GRAY = '#1C1C1C'

# Cars
CARS = 5

# Coins
COINS = 4

# NAME
NAMES = ['Hawkeye', 'Loki', 'Daredevil', 'Storm', 'Ultron', 'Groot', 'Magneto', 'Wanda', 'Wasp',
         'Shang-Chi', 'Yondu', 'Thanos', 'Hulk', 'X-Men', 'Nebula', 'Thor', 'Dr. Strange']

TEST_NAMES = ['Hawkeye', 'Black Widow', 'Daredevil', 'Storm', 'Black Panther']

# Color
COLOR = pygame.Color('lightskyblue3')