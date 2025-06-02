import pygame
import game_logic as g
from game_logic import *
from pygame import *
import time as t
# Imports 

# Set up pygame
pygame.init()
programIcon = pygame.image.load('images/Icon.png') # Load the Icon
pygame.display.set_icon(programIcon) # Set Icon
pygame.display.set_caption("Joker's Judgement") # Set window title
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((450,450))

# Establish screen size, font sizing and pygame clock
w, h = pygame.display.get_surface().get_size()
title_font = pygame.font.SysFont("segoeprint", 80)
font = pygame.font.SysFont("segoeprint", 30)
clock = pygame.time.Clock()
windeath_font = pygame.font.SysFont("segoeprint", 150)
clock.tick(60)

health_player = 20
health_enemy = 20

def menu_draw():
	""" Draws the menu screen for the game. 
	The function is simply a cleaner way to call it when required as compared to dumping the text block inside the core loop.
	"""
	screen.fill((47, 158, 68)) # The green colour used in the program.
	width = 750
	height = 100
	global play_button # I know globals are bad practice and lazy 
	global quit_button #but its simply the first prototype.
	global options_button
	play_button = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, 600, width, height))
	options_button = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, 750, width, height))
	quit_button = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, 900, width, height))
	title = title_font.render("Joker's Judgement", 1, (255,255,255))
	play = font.render("Play", 1, (0,0,0))
	quit = font.render("Quit", 1, (0,0,0))
	options = font.render("Options", 1, (0,0,0))
	text_rect = title.get_rect(center=(w//2,150))
	play_text = play.get_rect(center=play_button.center)
	options_text = options.get_rect(center=options_button.center)
	quit_text = quit.get_rect(center=quit_button.center)
	screen.blit(title, text_rect)
	screen.blit(play, play_text)
	screen.blit(options, options_text)
	screen.blit(quit, quit_text)

def main():

	""" The main game function. 
	The function is used to cleanly call the loop, as I said above. I will likely call other functions or change other things to a class in later sprints.
	"""
	screen.fill((47, 158, 68))
	Height = 125
	Width = 100
	pygame.draw.rect(screen, (25,113,194), (20, 700, Width, Height))
	pygame.draw.rect(screen, (224,49,49), (1820, 300, Width, Height))
	card1 = pygame.draw.rect(screen, (255,255,255), (800+0*(110),930 , Width, Height))
	card2 =  pygame.draw.rect(screen, (255,255,255), (800+1*(110),930 , Width, Height))
	card3 =  pygame.draw.rect(screen, (255,255,255), (800+2*(110),930 , Width, Height))
	card1_bot = pygame.draw.rect(screen, (224,49,49), (800+0*(110),50 , Width, Height))
	card2_bot =  pygame.draw.rect(screen, (224,49,49), (800+1*(110),50 , Width, Height))
	card3_bot =  pygame.draw.rect(screen, (224,49,49), (800+2*(110),50 , Width, Height))
	# Importantly the bots knowledge doesn't exist yet and won't until the game is devolped further in later sprints.
	played_card =  pygame.draw.rect(screen, (255,255,255), (800+1*(110),700 , Width, Height))
	players_health = title_font.render(str(health_player), 1, (25,113,194))
	text_rect_player = players_health.get_rect(center=(100,980))
	screen.blit(players_health, text_rect_player)
	enemy_health = title_font.render(str(health_enemy), 1, (224,49,49))
	text_rect_enemy = enemy_health.get_rect(center=(1820,100))
	screen.blit(enemy_health, text_rect_enemy)
	pygame.display.flip()
	pos = pygame.mouse.get_pos()
	pressed = pygame.mouse.get_pressed()[0]
	# Leftover debugging, leaving as will need in further dev sprints
	#print(pos)
	# Collisoin dectetion 
	if card1.collidepoint(pos) and pressed:
		screen.fill((47, 158, 68))
		filler = title_font.render("Card Play Logic goes here", 1, (255,255,255))
		text_rect_2 = filler.get_rect(center=(w//2,150))
		screen.blit(filler, text_rect_2)
		pygame.display.flip()
		t.sleep(2)
	elif card2.collidepoint(pos) and pressed:
		screen.fill((47, 158, 68))
		filler = title_font.render("Card Play Logic goes here", 1, (255,255,255))
		text_rect_2 = filler.get_rect(center=(w//2,150))
		screen.blit(filler, text_rect_2)
		pygame.display.flip()
		t.sleep(2)
	elif card3.collidepoint(pos) and pressed:
		screen.fill((47, 158, 68))
		filler = title_font.render("Card Play Logic goes here", 1, (255,255,255))
		text_rect_2 = filler.get_rect(center=(w//2,150))
		screen.blit(filler, text_rect_2)
		pygame.display.flip()
		t.sleep(2)
	elif played_card.collidepoint(pos) and pressed:
		screen.fill((47, 158, 68))
		filler = title_font.render("Attack Logic goes here", 1, (255,255,255))
		text_rect_2 = filler.get_rect(center=(w//2,150))
		screen.blit(filler, text_rect_2)
		pygame.display.flip()
		t.sleep(2)
	elif pygame.key.get_pressed()[pygame.K_w]:
		screen.fill((255,255,255))
		win_text = windeath_font.render("You win!", True, (0,0,0))
		text_rect_idk = win_text.get_rect(center=(w//2,h//2))
		screen.blit(win_text, text_rect_idk)
		pygame.display.flip()
		t.sleep(2)
	elif pygame.key.get_pressed()[pygame.K_l]:
		screen.fill((0,0,0))
		win_text = windeath_font.render("You Lose!", True, (255,0,0))
		text_rect_idk = win_text.get_rect(center=(w//2,h//2))
		screen.blit(win_text, text_rect_idk)
		pygame.display.flip()
		t.sleep(2)

def options():
	# See above explanmations, to be fleshed out later on to provide the user with a better experience.
	screen.fill((47, 158, 68))
	filler = title_font.render("Options Coming Soon", 1, (255,255,255))
	text_rect_2 = filler.get_rect(center=(w//2,150))
	screen.blit(filler, text_rect_2)
	pygame.display.flip()

# Main game loop that calls the diffrent functions to navigate through.
game_state = "menu"
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
			game_state = "menu"
	pygame.display.flip()
	if game_state == "menu": 
		menu_draw()
		pygame.display.flip()
		pos = pygame.mouse.get_pos()
		pressed = pygame.mouse.get_pressed()[0]
		if play_button.collidepoint(pos) and pressed:
			game_state = "playing"
		elif options_button.collidepoint(pos) and pressed:
			game_state = "options"
		elif quit_button.collidepoint(pos) and pressed:
			running = False
		pygame.display.flip()
	elif game_state == "playing":
		main()
	elif game_state == "options":
		options()
	else:
		# Error handling but should never happen
		print("How did you escape the matrix?")
		running = False
pygame.quit()
