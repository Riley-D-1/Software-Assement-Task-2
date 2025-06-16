# Software Engineering Task 2
### By Riley Dowse
# Sprint 1


## Task Definition


TBC


## Requirements definition
### Functional requirements
- Users must be able to view a bot in a fun and interactive GUI and play Joker's Judgement.
- The system must have random drawing and deck splitting
- The system must be able to track players' health and card inventories.
- The system must follow the rules of Joker's judgement
- The system must clearly show who is the winner and loser.




### Non Functional requirements
- The system must respond quickly to the players actions
- It must load within 3 seconds
- The game must maintain smooth and responsive
- The controls must be simple yet functional and easy to pick up
- Have settings to adapt and modify the user's experience
- The system must be reliable and not crash
- The game should handle errors gracefully and provide clear error messages.
- The game must have clear documentation and install steps.
- The game's rules must be clear and understandable.


## Determining Specifications
### Functional Specifications
What does the system actually NEED to do?


User Requirements
- Users must be able to view a bot in a fun and interactive GUI and play Joker's Judgement.
- The user needs to be able to input their actions and receive an output by the system informing them of their actions.


Inputs & Outputs
- The system needs to have clear and responsive inputs that correctly match the user's intent.
- The system needs to have simple but clear outputs that clearly display the game state to the user
- The input system has to be logical and easy to understand and pickup


Core Features
- At its core it needs to provide a fun card game experience that follows the rules of Joker's judgement
- It needs to be an exciting card game played against a challenging but fun bot.
- The system needs to be enticing to a wide variety of players.




User Interaction
- The users will interact with the game in a logical but simple GUI. A detailed readme will explain how to use the program, furthermore the rules of the game will be clearly laid out in a separate readme.
- The user
Error Handling
- The game will print errors in the terminal and provide game information for debugging purposes.
- I will also list errors with the program in the readme and provide clear and achievable solutions to them
What possible errors could you face that need to be handled by the system?
### Non Functional Specifications


Performance
- The system needs to respond quickly to the users input and be fluid and smooth at all times
- The system must remain at a consistent 60fps
- The system must load all aspects in less than 3 seconds
How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?


Useability / Accessibility
- My readme and installation guide will make it easy for anyone to install my game and cater to a wide variety of technological knowledge levels.
- If I have time I will code more accessibility settings.
How might you make your application more accessible? What could you do with the User Interface to improve usability?


Reliability
- I will code clear error messages and address all
- The user's data does not disclose any personal information and will be kept from the AI bot to keep the game fair and equal.


## Use case diagram
Actor: User


Preconditions: A suitable operating system that can run .exe files or alternatively an IDE that can run python files.


Main Flow:
- Begin - User selects the option to play.


- Setup – The system equally splits a deck of cards that have


- Draw Card – User clicks the draw pile


- Play Card- User selects a number card or an ability card to play


- Attack - User attacks with a number card leading the system to defend


Postconditions: Turn changes to the system , the user draws a card and play's a card.




## Design
Storyboard
![Alt text](images/Storyboard.png)  
Data Frame Diagram Level 0


![Alt text](images/dfd-0.png)  
Data Frame Diagram Level 1
![Alt text](images/dfd-1.png)
### Gantt Chart
![Alt text](images/Gantt-chart.png)
## Build and Test
```python
import pygame
# Intergration to be added 
#import game_logic as g
#from game_logic import *
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
	player_draw_pile = pygame.draw.rect(screen, (25,113,194), (20, 700, Width, Height))
	bot_draw_pile = pygame.draw.rect(screen, (224,49,49), (1820, 300, Width, Height))
	card1 = pygame.draw.rect(screen, (255,255,255), (800+0*(110),930 , Width, Height))
	card2 =  pygame.draw.rect(screen, (255,255,255), (800+1*(110),930 , Width, Height))
	card3 =  pygame.draw.rect(screen, (255,255,255), (800+2*(110),930 , Width, Height))
	card1_bot = pygame.draw.rect(screen, (224,49,49), (800+0*(110),50 , Width, Height))
	card2_bot =  pygame.draw.rect(screen, (224,49,49), (800+1*(110),50 , Width, Height))
	card3_bot =  pygame.draw.rect(screen, (224,49,49), (800+2*(110),50 , Width, Height))
	played_card_bot =  pygame.draw.rect(screen, (224,49,49), (800+1*(110),300 , Width, Height))
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
	if player_draw_pile.collidepoint(pos) and pressed:
		screen.fill((47, 158, 68))
		filler = title_font.render("Draw Logic goes here", 1, (255,255,255))
		text_rect_2 = filler.get_rect(center=(w//2,150))
		screen.blit(filler, text_rect_2)
		pygame.display.flip()
		t.sleep(2)
	elif card1.collidepoint(pos) and pressed:
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

```


## Review
End of Sprint Review Questions
1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.


My pygame project in sprint 1 does not effectively meet the majority of the functional requirements and meets only a few of non functional requirements in the planning stage of my project. I don't effectively meet the requirements I set out as my program is only a non functional Graphical User Interface that is a template for further development in sprint 2. The user is unable to play the game or versus a bot. You are unable to follow rules or see your card hand. Positively by pressing W and L you can get the win and lose screens and the GUI is intuitive and easy to navigate around in.


2. Analyse the performance of your program against the key use-cases you identified.


It does not follow most of the key use cases however my program behaves as I expected it to in this first sprint of the project, it handles input and output well and hits most of the functional specifications focused around output and input. The program reacts smoothly and fast to inputs and outputs clear GUI screens that match my storyboard at a consistent frame rate. I will be able to hit more of the key use case's requirements as I continue the project in the next sprints.


3. Assess the quality of your code in terms of readability, structure, and maintainability.


My quality of code is average, the system uses functions for better readability and the code is explained with comments that makes the code quite readable. The structure of the program could be improved by using Object Oriented Programming (OOP) and applying classes to simplify my code. The maintainability is quite simple at the moment as I did extensive testing and the main problem is that we are unable to use any of the game logic so you can only navigate around a shell as such.

4. Explain the improvements that should be made in the next stage of development.

The next stage of development must hit most if not all of the functional criteria and ideally hit most of the non-functional criteria as well. I need to begin to incorporate OOP fundamentals into my program and remove some of the bad practice  to ensure my code's readability, quality and structure. By implementing OOP I can ensure that my game logic remains fast and speedy as I continue development, furthermore by removing my I can follow best coding practices to ensure that my code is easier to maintain and build upon. For example I need to remove the Global variables used to identify the button positions for collision handling to be able to navigate around the GUI.




# KEYNOTE! THE PROGRAM DOES NOT CURRENTLY WORK IN RESOLUTIONS THAT ARE NOT 1080P (1920 PIXELS WIDE BY 1080 PIXELS TALL)






# Sprint 2


## Design

### Structure Chart
![Alt text](images/Main_flowchart.png)  

### Algorithms
#### Main Routine
###### Flowchart
![Alt text](images/Main_flowchart.png)  

##### Psudeocode
```
BEGIN Joker's Judement
    WHILE Program is running
        IF Game State = Menu
			Menu()
			IF MOS_Pos = Quit Button and Clicked 
				Running = False
			ELIF MOS_Pos = Play Button and Clicked 
			 	Game State = Playing
			ELIF MOS_Pos = Options Button and Clicked 
				Game State = Options
			ENDIF
        ELIF Game State = Options
            Options()
		ELIF Game State = Playing
			Game()
		ELSE
			Error Handling
        ENDIF
    ENDWHILE
END Joker's Judement 
```
#### Game loop Subroutinue

###### Flowchart
![Alt text](images\Game_loop_flowchart.png) 

##### Psudeocode
```
Begin Gameloop
Create Bot and User classes
Output green screen
Draw 3 cards
WHILE User Health and Bot Health > 0
	Draw 1 Card
	Update Health and Hands()
	User Input()
	Play()
	Update Health and Hands()
IF User Health > 0
	Win()
ELSE
	Lose()
ENDIF
```

#### Options Subroutine

###### Flowchart
![Alt text](images/Options_flowchart.png)  

##### Psudeocode
```
Begin Options
WHILE Program is running
		OUTPUT OPTION SCREEN
		IF MOS_Pos = Help Button and Clicked 
			Help
		ELIF MOS_Pos = Play Button and Clicked 
			Source
		ELIF MOS_Pos = Toggle Music Button and Clicked 
			Toggle Music
		ELIF MOS_Pos = Main Menu Button and Clicked 
			Running = False
		ENDIF
    ENDWHILE
END Options
```

## Build and Test
#### Main
```py
import pygame
from game_logic import *
# Imports 

# Set up pygame
pygame.init()
programIcon = pygame.image.load('images/Icon.png') # Load the Icon
pygame.display.set_icon(programIcon) # Set Icon
pygame.display.set_caption("Joker's Judgement") # Set window title
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

# Establish screen size, font sizing and pygame clock
w, h = pygame.display.get_surface().get_size()
title_font = pygame.font.SysFont("segoeprint",int(h*0.1))
font = pygame.font.SysFont("segoeprint", int(h*0.03))
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
	for i , card in enumerate(bot.hand(),start = int(user.hand_size()//2*-1)):
		pygame.draw.rect(screen, (224,49,49), (w*0.5+i*(180),h*0.05 , Width, Height))
	bot_hp = str(bot.check_hp())
	user_hp = str(user.check_hp()) 
	players_health = title_font.render(user_hp, 1, (25,113,194))
	text_rect_player = players_health.get_rect(center=(w*0.1,h*0.9))
	screen.blit(players_health, text_rect_player)
	enemy_health = title_font.render(bot_hp, 1, (224,49,49))
	text_rect_enemy = enemy_health.get_rect(center=(w*0.9,h*0.1))
	screen.blit(enemy_health, text_rect_enemy)
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
				quit()
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

def main(player_deck,bot_deck):

	""" The main game function. 
	The function is used to cleanly call the loop, as I said above. I will likely call other functions or change other things to a class in later sprints.
	I pass the player deck and bot deck to it and then the program returns a gamestate at the end
	"""
	screen.fill((47, 158, 68))
	#Height = h*0.175
	#Width = w*0.075
	"Draw pile will be in sprint 3 or 4? which is heavily limited."
	#pygame.draw.rect(screen, (25,113,194), (20, 700, Width, Height))
	#pygame.draw.rect(screen, (224,49,49), (1820, 300, Width, Height))
	# TO be removed -
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
				quit()
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
		play(user_card,random.choice(bot.hand()),user,bot)
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
		if main(Players_deck,Bots_deck) == "menu":
			game_state = "menu"		
	elif game_state == "options":
		options()
	else:
		# Error handling but should never happen
		print("How did you escape the matrix?")
		running = False
pygame.quit()

```

#### Game Logic
```py
import random
# Import the required imports
suits = [ "Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen","King")

class Card:
	def __init__(self,rank,suit):  
		self.rank = rank
		self.suit = suit
	def card_info(self):
		return self.rank,self.suit
	def card_clicked(self,pos,clicked,rect):
		if rect.collidepoint(pos) and clicked:
			print(rect)
			return "clicked"
			
	def __str__(self):
		return f"({self.rank}, '{self.suit}')"
	def __repr__(self): return str(self)

class Number_Card(Card):
	def __init__(self, rank, suit):
		super().__init__(rank, suit)
		if self.rank == "Ace":
			self.vaule = 10
		else:
			self.vaule = self.rank
	def card_vaule(self):
		return self.vaule
	def type(self):
		return "Number"
	
class Ability_Card(Card):
	def __init__(self, rank, suit):
		super().__init__(rank, suit)
		self.ability = self.rank
	def card_ability(self):
		return self.ability
	def type(self):
		return "Ability"

class Deck:
	def __init__(self):
		self.card_deck = []
	def create_deck(self):
		for suit in suits:
			for rank in ranks:	
				#if rank == "Jack" or "Joker" or "Queen" or "King":
				if rank in ["Jack", "Joker", "Queen", "King"]:				
					self.card_deck.append(Ability_Card(rank, suit))
				else:
					self.card_deck.append(Number_Card(rank, suit))
		self.card_deck.append(Ability_Card("Joker","Red"))
		self.card_deck.append(Ability_Card("Joker","Black"))
		return self.card_deck
	
class Player:
	def __init__(self,deck):
		self.hp = 20
		self.hand_ = []
		self.deck_ = deck
		self.card_list_ = []
		self.card_list_name = []
	def check_hp(self):
		return self.hp
	def damage_hp(self,damage):
		self.hp -= int(damage)
	def heal(self):
		self.hp += 5
	def add_card(self,card):
		self.hand_.append(card)
	def hand(self):
		return self.hand_
	def deck(self):
		temp_list = []
		for card in self.deck_:
			temp_list.append(card.card_info())
		return temp_list
	def hand_size(self):
		return len(self.hand_)
	def draw(self):
		#Check if the deck is empty 
		if len(self.deck_) == 0:
			start()
			game_cards_ = start()
			return "empty",game_cards_
		card = random.choice(self.deck_)
		self.deck_.remove(card)
		return "full",card
		# Else refill decks
	def wipe(self):
		self.hand_.clear()
		
	def remove_card(self,card):
		if card in self.hand_:
			self.hand_.remove(card)
		else:
			('card not found')
	def card_list(self,card,card_info):
		self.card_list_.append({"vaule":card_info,"rect":card})
	def card_list_info(self):
		unique_list = []
		for item in self.card_list_:
			if item not in unique_list:
				unique_list.append(item)
		self.card_list_ = unique_list
		return unique_list
	def new_deck(self,deck):
		self.deck_ = deck
		
def shuffle(game_cards):
	random.shuffle(game_cards)
	return game_cards

# Game start logic
def start():
	""" 
	The start of the game
	I create the deck class and then return the shuffled deck to be split into the users draw pile and bots draw pile
	"""
	deck = Deck()
	game_cards = deck.create_deck()
	cards = shuffle(game_cards) 
	return cards

def play(chosen_card,bot_card,player,bot):
	"""
	The play function returns the winner and loser of the compared cards and removes it form the hands
	It receives the classes of player and bot and also their chosen cards
	If its an ability it updates the user with the abilities effect before returning nothing to signify to continue.
	"""
	chosen_card.type()
	bot_card.type()
	if chosen_card.type() == "Number" and bot_card.type() == "Number":
		if chosen_card.card_vaule() > bot_card.card_vaule():
			discard_cards = bot_card 
			winning_card = chosen_card
			bot.remove_card(bot_card)
			return discard_cards,winning_card
		elif chosen_card.card_vaule() < bot_card.card_vaule():
			discard_cards = chosen_card 
			winning_card = bot_card
			player.remove_card(chosen_card)
			return discard_cards,winning_card
		elif chosen_card.card_vaule() == bot_card.card_vaule():
			discard_cards = bot_card,chosen_card 
			winning_card = None
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			return discard_cards,winning_card
		else:
			print("Card comparision error")
	elif chosen_card.type() == "Number" and bot_card.type() == "Ability":
		if bot_card.card_ability() == "Jack":
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			bot.damage_hp(chosen_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif bot_card.card_ability() == "King":
			player.damage_hp(5)
			bot.damage_hp(chosen_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif bot_card.card_ability() == "Queen":
			bot.heal()
			bot.damage_hp(chosen_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
	elif chosen_card.type() == "Ability" and bot_card.type() == "Number":
		if chosen_card.card_ability() == "Jack":
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			player.damage_hp(bot_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "King":
			bot.damage_hp(5)
			player.damage_hp(bot_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Queen":
			player.heal()
			player.damage_hp(bot_card.card_vaule())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
	elif chosen_card.type() == "Ability" and bot_card.type() == "Ability":
		if chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "King":
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "Queen":
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			bot.heal()
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "Jack":
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			answer,drawn_card = player.draw()
			player.add_card(drawn_card)
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Queen" and bot_card.card_ability() == "King": 
			player.heal()
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Queen" and bot_card.card_ability() == "Queen": 
			player.heal()
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Queen" and bot_card.card_ability() == "Jack": 
			player.heal()
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "King" and bot_card.card_ability() == "King":
			player.damage_hp(5)
			bot.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "King" and bot_card.card_ability() == "Queen": 
			bot.damage_hp(5)
			bot.heal()
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "King" and bot_card.card_ability() == "Jack": 
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			answer,drawn_card = bot.draw()
			bot.add_card(drawn_card)
			bot.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
	else:
		print("Bug, no type logic registered correctly")

```

## End of Sprint Review Questions
1. Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning. 

Refer to specific criteria or expectations outlined in your requirements document.

My  project effectively meets most of the functional and non functional criteria.



2. Analyse the performance of your program against the key use-cases you identified.

Discuss whether the program behaves as expected and handles input/output as planned.

My program behaves as expected and handles the input and output of my program well. 

3. Assess the quality of your code in terms of readability, structure, and maintainability.

Consider naming conventions, use of functions, comments, and overall organisation.

My code is more readable however after updating pygame i am now recieving an error related to maintainbility that would have to be fixed to enusre the long term functionality of my program. My naming conventions are slightly s
```
UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
```
4. Explain the improvements that should be made in the next stage of development.
Include both feature enhancements and refinements to code quality or structure.
In sprint 4, I need to continue refining my code quality and structure and develop a clearer user interface so that the game is easier to understand and use. I also want to add music into my game to give my game a more fun and cartoony feel.




Sprint 3

## Design

##































## Credit


The Icon inspiration comes from https://drawsgood.itch.io/8bit-deck-card-assets.
I made my own much smaller version that was heavily influenced by the asset.
