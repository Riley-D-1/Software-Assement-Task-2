import pygame
from game_logic import *
import random
import webbrowser
import sys
# Imports 

# Set up pygame
pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()
try:
	programIcon = pygame.image.load('images/Icon.png') # Load the Icon
	pygame.display.set_icon(programIcon) # Set Icon
	pygame.mixer.music.load('music/Get_After_It.ogg')
	pygame.mixer.music.set_volume(0.5)
	#main_music = pygame.mixer.music.load('music/Get_After_It.ogg')
	music = True
except FileNotFoundError:
	print("File not found")
	music = False

pygame.display.set_caption("Joker's Judgement") # Set window title
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

# Establish screen size, font sizing and pygame clock
w, h = pygame.display.get_surface().get_size()
title_font = pygame.font.SysFont("segoeprint",int(h*0.1))
font = pygame.font.SysFont("segoeprint", int(h*0.02))
card_font = pygame.font.SysFont("segoeprint", int(h*0.0125))
clock = pygame.time.Clock()
windeath_font = pygame.font.SysFont("segoeprint", int(h*0.1))
clock.tick(60)

def win():
	"""
	The win function simply displays a simple win screen
	"""
	screen.fill((255,255,255))
	win_text = windeath_font.render("You win!", True, (0,0,0))
	text_rect_idk = win_text.get_rect(center=(w//2,h//2))
	screen.blit(win_text, text_rect_idk)
	pygame.display.flip()

def lose():
	"""
	The lose function simply displays a simple lose screen
	"""
	screen.fill((0,0,0))
	win_text = windeath_font.render("You Lose!", True, (255,0,0))
	text_rect_idk = win_text.get_rect(center=(w//2,h//2))
	screen.blit(win_text, text_rect_idk)
	pygame.display.flip()

def update_hands_hp(user,bot):
	""" This function updates the users hands and hp
	The function requires the user class and the bot class in order to function
	The function does not return anything as it only updates the visual location and gamecards postions
	
	"""
	Height = h*0.175
	Width = w*0.075
	user.card_list_ = []
	screen.fill((47, 158, 68))
	Height = h*0.175
	Width = w*0.075
	# The users's hand being drawn 
	for i ,card in enumerate(user.hand(), start =int(user.hand_size()//2*-1)):
		card_text_info = str(card)
		# Modifing the string for the card
		card_text_info = card_text_info.replace("(","")
		card_text_info = card_text_info.replace(")","")
		card_text_info = card_text_info.replace(",", " of",)
		card_text_info = card_text_info.replace("'", "")
		game_card = pygame.draw.rect(screen, (255,255,255), (w*0.5+i*(180),h*0.8 , Width, Height))
		card_info = card_font.render(str(card_text_info), 1, (0,0,0))
		text_rect = card_info.get_rect(center=game_card.center)
		screen.blit(card_info, text_rect)
		# Store the position and card name for checking user input later.
		user.card_list(game_card,card)
	# The bot's hand being drawn 
	for i , card in enumerate(bot.hand(),start = int(bot.hand_size()//2*-1)):
		pygame.draw.rect(screen, (224,49,49), (w*0.5+i*(180),h*0.05 , Width, Height))
	bot_hp = str(bot.check_hp())
	user_hp = str(user.check_hp()) 
	# Players and bots health
	players_health = title_font.render(user_hp, 1, (25,113,194))
	text_rect_player = players_health.get_rect(center=(w*0.1,h*0.9))
	screen.blit(players_health, text_rect_player)
	enemy_health = title_font.render(bot_hp, 1, (224,49,49))
	text_rect_enemy = enemy_health.get_rect(center=(w*0.9,h*0.1))
	screen.blit(enemy_health, text_rect_enemy)
	# Name titles 
	players_name = title_font.render("(You)", 1, (25,113,194))
	text_rect_player_name = players_name.get_rect(center=(w*0.9,h*0.9))
	screen.blit(players_name, text_rect_player_name)
	enemy_name= title_font.render("Bot", 1, (224,49,49))
	text_rect_enemy_name  = enemy_name.get_rect(center=(w*0.1,h*0.1))
	screen.blit(enemy_name, text_rect_enemy_name)
	pygame.display.flip()

def user_input(user):
	"""
	The user input for the game is done below and returns the users choice
	The user paramater is passed to it
	"""
	# Establishes user's cards and their location
	cards = user.card_list_info()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# This is used so that the mouse button down is always checking and the pos collide only happens if a click occurs
				pygame.display.flip()
				pos = pygame.mouse.get_pos()
				for card in cards:
					# Splitting the vaules
					rect = card['rect']
					vaule = card['vaule']
					if rect.collidepoint(pos):
						# Collidepoint then returning the card to the function
						return vaule
	
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

def main(player_deck,bot_deck,help_info):

	""" The main game function. 
	The function is used to cleanly call the loop, as I said above. I will likely call other functions or change other things to a class in later sprints.
	I pass the player deck and bot deck to it and then the program returns a gamestate at the end
	"""
	screen.fill((47, 158, 68))
	

	user = Player(player_deck)
	bot = Player(bot_deck)
	for i in range(2):
		answer,drawn_card = bot.draw()
		bot.add_card(drawn_card)
		answer,drawn_card = user.draw()
		user.add_card(drawn_card)
		
	update_hands_hp(user,bot)
	pygame.display.flip()
	# The game loop that constantly checks if the hp is less than 0
	while bot.check_hp() > 0 and user.check_hp() > 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			# So users can quit the game
		if bot.hand_size() < 5:
			# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
			answer,drawn_card = bot.draw()
			if answer == "empty":
				Players_deck = drawn_card[:len(drawn_card)//2]
				Bots_deck = drawn_card[len(drawn_card)//2:]
				bot.new_deck(Bots_deck)
				user.new_deck(Players_deck)
				answer,drawn_card = bot.draw()
				bot.add_card(drawn_card)
			else:
				bot.add_card(drawn_card)
		if user.hand_size() < 5:
			answer,drawn_card = user.draw()
			# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
			if	answer == "empty":
				Players_deck = drawn_card[:len(drawn_card)//2]
				Bots_deck = drawn_card[len(drawn_card)//2:]
				bot.new_deck(Bots_deck)
				user.new_deck(Players_deck)
				answer,drawn_card = user.draw()
				user.add_card(drawn_card)
			else:
				user.add_card(drawn_card)
		# Updates their hands and hp 
		update_hands_hp(user,bot)
		# Wait for user_input
		user_card=user_input(user)
		play(user_card,random.choice(bot.hand()),user,bot,help_info)
		update_hands_hp(user,bot)
	# Checks who won the game and runs the correct function to display the screen.
	if user.check_hp() > 0:
		win()
		pygame.time.wait(3000)
		# returns that the thing is finished so  that the game returns to menu
		return "menu"
	else:
		lose()
		pygame.time.wait(3000)
		# returns that the thing is finished so  that the game returns to menu
		return "menu"

def options():
	width = w*0.6
	height = h*0.11
	# See above explanmations, to be fleshed out later on to provide the user with a better experience.
	screen.fill((47, 158, 68))
	filler = title_font.render("Options", 1, (255,255,255))
	Music_toggle = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.40), width, height))
	Help_info_toggle = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.55), width, height))
	Source = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.70), width, height))
	Main_menu = pygame.draw.rect(screen, (255, 255, 255), ((w-width)//2, (h*0.85), width, height))
	text_rect_2 = filler.get_rect(center=(w//2,h*0.125))
	music_toggle_ = font.render("Music Toggle", 1, (0,0,0))
	help = font.render("Toggle Help Info", 1, (0,0,0))
	source = font.render("Source", 1, (0,0,0))
	main_menu = font.render("Main Menu", 1, (0,0,0))
	music_toggle_text = music_toggle_.get_rect(center=Music_toggle.center)
	help_text = help.get_rect(center=Help_info_toggle.center)
	source_text = source.get_rect(center=Source.center)
	return_text = main_menu.get_rect(center=Main_menu.center)
	screen.blit(filler, text_rect_2)
	screen.blit(music_toggle_, music_toggle_text)
	screen.blit(help, help_text)
	screen.blit(source, source_text)
	screen.blit(main_menu, return_text)
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
		elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
			game_state = "menu"
			return game_state
		
		pressed = pygame.mouse.get_pressed()[0]		
		pos = pygame.mouse.get_pos()
		if Music_toggle.collidepoint(pos) and pressed:
			# Collidepoint then returning the card to the function
			return "music"
		elif Help_info_toggle.collidepoint(pos) and pressed:
			return "help_info"
		elif Source.collidepoint(pos) and pressed:
			webbrowser.open("https://github.com/Riley-D-1/Software-Assement-Task-2")
			return "web"
		elif Main_menu.collidepoint(pos) and pressed:
			return "menu"

def play(chosen_card,bot_card,player,bot,help_info):
	"""
	The play function returns the winner and loser of the compared cards and removes it form the hands
	It receives the classes of player and bot and also their chosen cards
	If its an ability it updates the user with the abilities effect before returning nothing to signify to continue.
	"""
	Height = h*0.175
	Width = w*0.075
	# The green colour used in the program.
	card_text_info = str(chosen_card)
	# Modifing the string for the card
	card_text_info = card_text_info.replace("(","")
	card_text_info = card_text_info.replace(")","")
	card_text_info = card_text_info.replace(",", " of",)
	card_text_info = card_text_info.replace("'", "")
	played_card = pygame.draw.rect(screen, (255,255,255),(w//2, h*0.55, Width, Height))
	card_info_rendered = card_font.render(str(card_text_info), 1, (0,0,0))
	text_rect = card_info_rendered.get_rect(center=played_card.center)
	screen.blit(card_info_rendered, text_rect)
	card_text_info = str(bot_card)
	# Modifing the string for the card
	card_text_info = card_text_info.replace("(","")
	card_text_info = card_text_info.replace(")","")
	card_text_info = card_text_info.replace(",", " of",)
	card_text_info = card_text_info.replace("'", "")
	played_card_bot = pygame.draw.rect(screen, (224,49,49),(w//2, h*0.25, Width, Height))
	card_info_rendered_bot = card_font.render(str(card_text_info), 1, (0,0,0))
	bot_text_rect = card_info_rendered_bot.get_rect(center=played_card_bot.center)
	screen.blit(card_info_rendered_bot, bot_text_rect)
	if chosen_card.type() == "Number" and bot_card.type() == "Number":
		if chosen_card.card_vaule() > bot_card.card_vaule():
			bot.remove_card(bot_card)
			message =  "Player wins the round. Bot's card discarded."
		elif chosen_card.card_vaule() < bot_card.card_vaule():
			player.remove_card(chosen_card)
			message =  "Bot wins the round. Player's card discarded."
		elif chosen_card.card_vaule() == bot_card.card_vaule():
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message =  "Tie for this round. Both cards discarded."
		else:
			print("Card comparision error")
	elif chosen_card.type() == "Number" and bot_card.type() == "Ability":
		if bot_card.card_ability() == "Jack":
			if bot.hand_size() < 5:
				# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
				answer,drawn_card = bot.draw()
				if answer == "empty":
					Players_deck = drawn_card[:len(drawn_card)//2]
					Bots_deck = drawn_card[len(drawn_card)//2:]
					bot.new_deck(Bots_deck)
					player.new_deck(Players_deck)
					answer,drawn_card = bot.draw()
					bot.add_card(drawn_card)
				else:
					bot.add_card(drawn_card)
				bot.damage_hp(chosen_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Player deals damage and Bot's ability used. Both cards discarded."
		elif bot_card.card_ability() == "King":
			player.damage_hp(5)
			bot.damage_hp(chosen_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Player deals damage and Bot's ability used. Both cards discarded."
		elif bot_card.card_ability() == "Queen":
			bot.heal()
			bot.damage_hp(chosen_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Player deals damage and Bot's ability used. Both cards discarded."
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
			message = "Joker played! Hand Wipe!"
	elif chosen_card.type() == "Ability" and bot_card.type() == "Number":
		if chosen_card.card_ability() == "Jack":
			for i in range(2):
				if player.hand_size() < 5:
							answer,drawn_card = player.draw()
							# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
							if	answer == "empty":
								Players_deck = drawn_card[:len(drawn_card)//2]
								Bots_deck = drawn_card[len(drawn_card)//2:]
								bot.new_deck(Bots_deck)
								player.new_deck(Players_deck)
								answer,drawn_card = player.draw()
								player.add_card(drawn_card)
							else:
								player.add_card(drawn_card)
			player.damage_hp(bot_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot deals damage and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "King":
			bot.damage_hp(5)
			player.damage_hp(bot_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot deals damage and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "Queen":
			player.heal()
			player.damage_hp(bot_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot deals damage and Player's ability used. Both cards discarded."
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
			message = "Joker played! Hand Wipe!"
	elif chosen_card.type() == "Ability" and bot_card.type() == "Ability":
		if chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "King":
			for i in range(2):
				if player.hand_size() < 5:
							answer,drawn_card = player.draw()
							# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
							if	answer == "empty":
								Players_deck = drawn_card[:len(drawn_card)//2]
								Bots_deck = drawn_card[len(drawn_card)//2:]
								bot.new_deck(Bots_deck)
								player.new_deck(Players_deck)
								answer,drawn_card = player.draw()
								player.add_card(drawn_card)
							else:
								player.add_card(drawn_card)
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "Queen":
			for i in range(2):
				if player.hand_size() < 5:
							answer,drawn_card = player.draw()
							# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
							if	answer == "empty":
								Players_deck = drawn_card[:len(drawn_card)//2]
								Bots_deck = drawn_card[len(drawn_card)//2:]
								bot.new_deck(Bots_deck)
								player.new_deck(Players_deck)
								answer,drawn_card = player.draw()
								player.add_card(drawn_card)
							else:
								player.add_card(drawn_card)
			bot.heal()
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "Jack":
			for i in range(2):
				if player.hand_size() < 5:
							answer,drawn_card = player.draw()
							# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
							if	answer == "empty":
								Players_deck = drawn_card[:len(drawn_card)//2]
								Bots_deck = drawn_card[len(drawn_card)//2:]
								bot.new_deck(Bots_deck)
								player.new_deck(Players_deck)
								answer,drawn_card = player.draw()
								player.add_card(drawn_card)
							else:
								player.add_card(drawn_card)
			for i in range(2):
				if bot.hand_size() < 5:
					# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
					answer,drawn_card = bot.draw()
					if answer == "empty":
						Players_deck = drawn_card[:len(drawn_card)//2]
						Bots_deck = drawn_card[len(drawn_card)//2:]
						bot.new_deck(Bots_deck)
						player.new_deck(Players_deck)
						answer,drawn_card = bot.draw()
						bot.add_card(drawn_card)
					else:
						bot.add_card(drawn_card)

			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "Queen" and bot_card.card_ability() == "King": 
			player.heal()
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "Queen" and bot_card.card_ability() == "Queen": 
			player.heal()
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded"
		elif chosen_card.card_ability() == "Queen" and bot_card.card_ability() == "Jack": 
			player.heal()
			for i in range(2):
				if bot.hand_size() < 5:
					# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
					answer,drawn_card = bot.draw()
					if answer == "empty":
						Players_deck = drawn_card[:len(drawn_card)//2]
						Bots_deck = drawn_card[len(drawn_card)//2:]
						bot.new_deck(Bots_deck)
						player.new_deck(Players_deck)
						answer,drawn_card = bot.draw()
						bot.add_card(drawn_card)
					else:
						bot.add_card(drawn_card)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "King" and bot_card.card_ability() == "King":
			player.damage_hp(5)
			bot.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "King" and bot_card.card_ability() == "Queen": 
			bot.damage_hp(5)
			bot.heal()
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		elif chosen_card.card_ability() == "King" and bot_card.card_ability() == "Jack": 
			for i in range(2):
				if bot.hand_size() < 5:
					# This is drawn if they have less than 5 cards and checks if their deck if empty and if so refreshes their deck with cards.
					answer,drawn_card = bot.draw()
					if answer == "empty":
						Players_deck = drawn_card[:len(drawn_card)//2]
						Bots_deck = drawn_card[len(drawn_card)//2:]
						bot.new_deck(Bots_deck)
						player.new_deck(Players_deck)
						answer,drawn_card = bot.draw()
						bot.add_card(drawn_card)
					else:
						bot.add_card(drawn_card)

			bot.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			message = "Bot's and Player's ability used. Both cards discarded."
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
			message = "Joker played! Hand Wipe!"
	else:
		print("Bug, no type logic registered correctly")
	if help_info == True:
		message_render = font.render(message, True, (255,255,255))
		text_rect_thing = message_render.get_rect(center=(w//2,h//2))
		screen.blit(message_render,text_rect_thing)
		pygame.display.flip()
		pygame.time.wait(4000)
	else:
		pygame.display.flip()
		pygame.time.wait(2000)


# Main game loop that calls the diffrent functions to navigate through.
game_state = "menu"
running = True
begin = True
help_info = False
while running:
	if music == True and not pygame.mixer.music.get_busy():
		try:
			pygame.mixer.music.play(-1)
		except:
			music = False
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
		if main(Players_deck,Bots_deck,help_info) == "menu":
			game_state = "menu"		
			begin = True
	elif game_state == "options":
		options_result = options()
		if options_result == "menu":
			pygame.time.wait(200)
			game_state = "menu"	
		elif options_result == "web":
			pygame.time.wait(500)
			game_state = "menu"
		elif options_result == "help_info":
			pygame.time.wait(200)
			if help_info == True:
				help_info = False
				game_state = "menu"
			elif help_info == False:
				help_info = True
				game_state = "menu"
		elif options_result == "music":
			if music == True:
				pygame.mixer.music.pause()
				music = False
				game_state = "menu"
			else: 
				pygame.mixer.music.unpause()
				music = True
				game_state = "menu"
	else:
		# Error handling but should never happen
		print("How did you escape the matrix?")
		running = False
pygame.quit()
