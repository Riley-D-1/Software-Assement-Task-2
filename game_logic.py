import pprint
from pprint import pprint
import random
suits = [ "Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen","King")
card_deck = []
Running = True

def create_deck():
	for suit in suits:
		for rank in ranks:
			card_deck.append([rank, suit])
	card_deck.append(["Joker","Red"])
	card_deck.append(["Joker","Black"])
	return card_deck

#pprint(create_deck())
#pprint(card_deck)

def shuffle(deck):
	random.shuffle(deck)

def draw(deck): 
	card = random.choice(deck)
	deck.remove(card)
	return card


# Game start logic
def start():
	game_cards=create_deck()
	shuffle(game_cards)
	Players_deck = game_cards[:len(game_cards)//2]
	Bots_deck = game_cards[len(game_cards)//2:]
	#print("Bots Deck \n")
	#pprint(Bots_deck)
	#print("Length of deck "+ str(len(Bots_deck)))
	#print("Players Deck \n")
	#pprint(Players_deck)
	#print("Length of players deck "+ str(len(Players_deck)))
	return Players_deck, Bots_deck 


def attack(chosen_card,defence_card,turn_num):
	chosen_card.type()
	if turn_num == 1:
		print("First round, you can't attack")
	else:
		print("Filler")
	


decks = start()
Players_deck = decks[0]
Bots_deck  = decks[1]
players_life = 20
bots_life = 20
players=["Player","Bot"]
hand=[]
bots_hand= []
for i in range(3):
	hand.append(draw(Players_deck))
	bots_hand.append(draw(Bots_deck))
print(bots_hand)
print(hand)
turn = random.choice(players)
round_num = 1
while players_life or bots_life > 0:
	if turn == "Player":
			
	#elif turn == "Bot":
		
		print("Bot does stuff")




