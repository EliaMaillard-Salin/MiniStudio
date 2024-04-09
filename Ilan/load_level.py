import pygame
import csv
from ..Plateform import *

def load_level1(file_path):
    level_data = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            level_data.append(row)
    return level_data

# Use the level_data to create your pygame level


def load_level(level_path):
    with open(level_path, 'r') as file:
        return csv.load(file)

def create_platforms(level_data):
    platforms = []
    for y, row in enumerate(level_data):
        for x, tile_type in enumerate(row):
            if tile_type != -1:  # -1 signifie pas de plateforme
                platforms.append(Plateform(x * 40, y * 40, 40, 40, WHITE))
    return platforms

# Charge le niveau
WHITE = (255, 255, 255)
level_data = load_level('Levels/level1.csv')
platforms = create_platforms(level_data)

# Use the level_data to create your pygame level