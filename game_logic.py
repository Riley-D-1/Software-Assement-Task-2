import time as t
import random

suits = [ "Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen","King")

class Card:
	def __init__(self,rank,suit):  
		self.rank = rank
		self.suit = suit
	def card_info(self):
		return self.rank,self.suit

class Number_Card(Card):
	def __init__(self, rank, suit):
		super().__init__(rank, suit)
		if self.rank == "Ace":
			self.vaule = 11
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
		self.create_deck()
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
	def __init__(self,num):
		self.hp = 20
		self.hand = []
		self.deck_ = start()[num]
	def check_hp(self):
		return self.hp
	def damage_hp(self,damage):
		self.hp -= int(damage)
	def heal(self):
		self.hp += 5
	def add_card(self,card):
		self.hand.append(card)
	def check_hand(self):
		for card in self.hand:
			print(card)
	def deck(self):
		temp_list = []
		for card in self.deck_:
			temp_list.append(card.card_info())
		return temp_list
	def hand_size(self):
		return len(self.hand)
	def remove_card(self):
		discard = random.choice(self.deck_)
		self.deck_.remove(discard)
def shuffle(deck):
	random.shuffle(deck)

def draw(deck): 
	card = random.choice(deck)
	deck.remove(card)
	return card

def info(deck):
	for card in deck:
		print(card.card_info())
		print(card.type())
		
# Game start logic
def start():
	new_deck = Deck()
	game_cards= new_deck.create_deck()
	shuffle(game_cards)
	Players_deck = game_cards[:len(game_cards)//2]
	Bots_deck = game_cards[len(game_cards)//2:]
	return Players_deck, Bots_deck 

def play(chosen_card,turn_num,defender,player):
	chosen_card.type()
	if chosen_card.type() == "Number":
		if turn_num == 1:
			print("First round, you can't attack")
		else:
			#Ask defender for defence card
			# defence_card
			#defemder
			attacker_vaule = chosen_card.vaule()
			# defender_card.vaule
			#if attacker_vaule == defender_card.vaule()
	else:
		if chosen_card.card_ability() == "Jack":
			player.add_card(draw(player.deck()))	
		if chosen_card.card_ability() == "King":
			draw(defender(defender.remove()))
		if chosen_card.card_ability() == "Queen":
			player.heal()
			round_num += 1
			turn = "Bot"


			


