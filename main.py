import pygame
from game_logic import *
from game_logic import Player
import game_logic as g
from pygame import *
from pygame.time import *
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
title_font = pygame.font.SysFont("segoeprint",int(h*0.1))
font = pygame.font.SysFont("segoeprint", int(h*0.03))
card_font = pygame.font.SysFont("segoeprint", int(h*0.0125))
clock = pygame.time.Clock()
windeath_font = pygame.font.SysFont("segoeprint", int(h*0.1))
clock.tick(60)

health_player = 20
health_enemy = 20

def update_hands(user,bot):
	Height = h*0.175
	Width = w*0.075
	for i ,card in enumerate(user.hand(), start =int(user.hand_size()//2*-1)):
		card_text_info = str(card)
		card_text_info = card_text_info.replace("(","")
		card_text_info = card_text_info.replace(")","")
		card_text_info = card_text_info.replace(",", " of",)
		card_text_info = card_text_info.replace("'", "")
		game_card = pygame.draw.rect(screen, (255,255,255), (w*0.5+i*(180),h*0.8 , Width, Height))
		card_info = card_font.render(str(card_text_info), 1, (0,0,0))
		text_rect = card_info.get_rect(center=game_card.center)
		screen.blit(card_info, text_rect)
	pygame.display.flip()

	for i , card in enumerate(bot.hand(),start = int(user.hand_size()//2*-1)):
		pygame.draw.rect(screen, (224,49,49), (w*0.5+i*(180),h*0.05 , Width, Height))
	pygame.display.flip()


def menu_draw():
	""" Draws the menu screen for the game. 
	The function is simply a cleaner way to call it when required as compared to dumping the text block inside the core loop.
	"""
	screen.fill((47, 158, 68)) # The green colour used in the program.
	width = w*0.6
	height = h*0.11
	play_button = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.55), width, height))
	options_button = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.70), width, height))
	quit_button = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.85), width, height))
	title = title_font.render("Joker's Judgement", 1, (255,255,255))
	play = font.render("Play", 1, (0,0,0))
	quit = font.render("Quit", 1, (0,0,0))
	options = font.render("Options", 1, (0,0,0))
	text_rect = title.get_rect(center=(w//2,h*0.15))
	play_text = play.get_rect(center=play_button.center)
	options_text = options.get_rect(center=options_button.center)
	quit_text = quit.get_rect(center=quit_button.center)
	screen.blit(title, text_rect)
	screen.blit(play, play_text)
	screen.blit(options, options_text)
	screen.blit(quit, quit_text)
	return play_button,options_button,quit_button

def main(player_deck,bot_deck):

	""" The main game function. 
	The function is used to cleanly call the loop, as I said above. I will likely call other functions or change other things to a class in later sprints.
	"""
	screen.fill((47, 158, 68))
	Height = h*0.175
	Width = w*0.075
	"Draw pile will be in sprint 3 or 4? which is heavily limited."
	#pygame.draw.rect(screen, (25,113,194), (20, 700, Width, Height))
	#pygame.draw.rect(screen, (224,49,49), (1820, 300, Width, Height))
	# TO be removed -
	"""
	card1 = pygame.draw.rect(screen, (255,255,255), (800+0*(180),930 , Width, Height))
	card2 =  pygame.draw.rect(screen, (255,255,255), (800+1*(180),930 , Width, Height))
	card3 =  pygame.draw.rect(screen, (255,255,255), (800+2*(180),930 , Width, Height))
	card1_bot = pygame.draw.rect(screen, (224,49,49), (800+0*(180),50 , Width, Height))
	card2_bot =  pygame.draw.rect(screen, (224,49,49), (800+1*(180),50 , Width, Height))
	card1_bot = pygame.draw.rect(screen, (224,49,49), (800+2*(180),50 , Width, Height))
	card2_bot =  pygame.draw.rect(screen, (224,49,49), (800+3*(180),50 , Width, Height))
	card2_bot =  pygame.draw.rect(screen, (224,49,49), (800-1*(180),50 , Width, Height))
	card3_bot =  pygame.draw.rect(screen, (224,49,49), (800-2*(180),50 , Width, Height))
	"""
	user = Player(player_deck)
	bot = Player(bot_deck)
	for i in range(3):
		user.add_card(user.draw())
		bot.add_card(bot.draw())
	update_hands(user,bot)
	players_health = title_font.render(str(health_player), 1, (25,113,194))
	text_rect_player = players_health.get_rect(center=(w*0.1,h*0.9))
	screen.blit(players_health, text_rect_player)
	enemy_health = title_font.render(str(health_enemy), 1, (224,49,49))
	text_rect_enemy = enemy_health.get_rect(center=(w*0.9,h*0.1))
	screen.blit(enemy_health, text_rect_enemy)
	pygame.display.flip()
	pos = pygame.mouse.get_pos()
	pressed = pygame.mouse.get_pressed()[0]
	turn = "Player"
	round_num = 1
	pygame.time.wait(5000)
	while bot.check_hp() and user.check_hp() > 0:
		if turn == "Player":
			if round_num == 1:
				user.add_card(user.draw())
				update_hands(user,bot)
				pygame.time.wait(5000)
				turn = "Bot"
			elif user.hand_size() <= 6:
				user.add_card(user.draw())
				while turn == "Player":
					for card in enumerate(user.hand()):
						card.card_clicked(pos,pressed,bot.hand(),user.hand())
				update_hands(user,bot)
				turn = "Bot"
				pygame.time.wait(5)
				pygame.display.flip()
			else:
				while turn == "Player":
					for card in enumerate(user.hand):
						card.card_clicked(pos,pressed,bot.check_hand(),user.hand())
				pygame.time.wait(5)
				pygame.display.flip()
		elif turn == "Bot":
			pygame.time.wait(5)
			if bot.hand_size() <= 6:
				bot.add_card(bot.draw())
				chosen_card = random.choice(bot.hand())
				play(chosen_card,user,bot)
			else:
				#play(chosen_card,round_num,user,bot))
				print("")
		else:
			print("Bug")

	if enemy_health < 0:
		screen.fill((255,255,255))
		win_text = windeath_font.render("You win!", True, (0,0,0))
		text_rect_idk = win_text.get_rect(center=(w//2,h//2))
		screen.blit(win_text, text_rect_idk)
		pygame.display.flip()
		pygame.time.wait(5)
		game_state = "menu"
	else:
		screen.fill((0,0,0))
		win_text = windeath_font.render("You Lose!", True, (255,0,0))
		text_rect_idk = win_text.get_rect(center=(w//2,h//2))
		screen.blit(win_text, text_rect_idk)
		pygame.display.flip()
		pygame.time.wait(5)
		game_state = "menu"

def options():
	# See above explanmations, to be fleshed out later on to provide the user with a better experience.
	screen.fill((47, 158, 68))
	filler = title_font.render("Options Coming Soon", 1, (255,255,255))
	text_rect_2 = filler.get_rect(center=(w//2,h*0.125))
	screen.blit(filler, text_rect_2)
	pygame.display.flip()

# Main game loop that calls the diffrent functions to navigate through.
game_state = "menu"
running = True
begin = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
			game_state = "menu"
	pygame.display.flip()
	if game_state == "menu": 
		play_button,options_button,quit_button=menu_draw()
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
		if begin == True:
			game_cards_ = start()
			Players_deck = game_cards_[:len(game_cards_)//2]
			Bots_deck = game_cards_[len(game_cards_)//2:]
			begin = False
		main(Players_deck,Bots_deck)
	elif game_state == "options":
		options()
	else:
		# Error handling but should never happen
		print("How did you escape the matrix?")
		running = False
pygame.quit()
