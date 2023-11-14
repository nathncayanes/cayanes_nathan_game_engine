# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# player settings
PLAYER_JUMP = 23
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2

# define colors, I got the color codes for most of these from Coolors.co
# link: https://coolors.co/
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (118, 137, 72)
BLUE = (0, 0, 255)
GRAY = (46, 97, 113)
ICEWHITE = (224, 251, 252)
ORANGE = (220, 150, 90)
YELLOW = (255, 215, 0)

# this sets up the properties (coordinates and size) of the platforms that are called in main.py
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (10, 25, 100, 20, "normal"),
                 (50, -30, 100, 20, "moving"),
                 (250, -100, 100, 20, "moving"),
                 (138, -234, 100, 20, "moving"),
                 (24, -370, 200, 20, "normal"),
                 (WIDTH / 2 - 50, -500, 100, 20, "normal"),
                 (25, -750, 75, 20, "normal"),
                 (100, -850, 100, 20, "moving"),
                 (WIDTH / 2 - 50, -1000, 100, 20, "finish")
                 ]

# same as above but for Ice Platforms
ICEPLATFORM_LIST = [(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, "normal"),
                    (175, 100, 50, 20, "normal"),
                    (157, -172, 50, 20, "normal"),
                    (75, -600, 100, 20, "normal"),
                    (250, -600, 100, 20, "normal"),
                    (25, -900, 50, 20, "normal")
                    ]

# same as above but for the Finishline
FINISHLINE_LIST = [(WIDTH / 2 - 50, -1000, 100, 20, "normal")]