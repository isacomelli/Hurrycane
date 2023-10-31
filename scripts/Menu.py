import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()
 
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
screen_width=500
screen_height=660
screen=pygame.display.set_mode((screen_width, screen_height))
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
    return newText
 
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
 
# Game Fonts
font = "Retro.ttf"

 
 
# Game Framerate
clock = pygame.time.Clock()
FPS=30


def main_menu():
 
    menu=True
    selected= 0
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    if selected == 0:
                        selected = 0
                    else:
                        selected -= 1
                elif event.key==pygame.K_DOWN:
                    if selected == 4:
                        selected = 4
                    else:
                        selected += 1
                if event.key==pygame.K_RETURN:
                        #TITLE, START, CHARACTER, OPTION, ABOUT,
                    if selected== 0:
                        print("Start")
                    if selected== 1:
                        print("character")
                    if selected== 2:
                        print("option")
                    if selected== 3:
                        print("about")
                    if selected== 4:
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(gray)
        title=text_format("HurryCane", font, 90, yellow)
        if selected==0:
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected==1:
            text_character=text_format("CHARACTER", font, 75, white)
        else:
            text_character = text_format("CHARACTER", font, 75, black)
        if selected==2:
            text_options=text_format("OPTIONS", font, 75, white)
        else:
            text_options = text_format("OPTIONS", font, 75, black)
        if selected==3:
            text_about=text_format("ABOUT", font, 75, white)
        else:
            text_about = text_format("ABOUT", font, 75, black)
        if selected==4:
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        character_rect=text_character.get_rect()
        options_rect=text_options.get_rect()
        about_rect=text_about.get_rect()
        quit_rect=text_quit.get_rect()

        #TITLE, START, CHARACTER, OPTION, ABOUT,
        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_character, (screen_width/2 - (character_rect[2]/2), 360))
        screen.blit(text_options, (screen_width/2 - (options_rect[2]/2), 420))
        screen.blit(text_about, (screen_width/2 - (about_rect[2]/2), 480))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 540))

        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")
        
#Initialize the Game
main_menu()

