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
	def card_clicked(self,card,pos,clicked,bot_deck,user):
		if card.collidepoint(pos) and clicked:
			play(self.card_info(),bot_deck,user)
	
	def __str__(self):
		return f"({self.rank}, '{self.suit}')"
	def __repr__(self): return str(self)

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
	def check_hp(self):
		return self.hp
	def damage_hp(self,damage):
		self.hp -= int(damage)
	def heal(self):
		self.hp += 5
	def add_card(self,card):
		self.hand_.append(card)
	def check_hand(self):
		for card in self.hand_:
			print(card)
	def hand(self):
		temp_list = []
		for card in self.hand_:
			temp_list.append(card)
		return temp_list
	def deck(self):
		temp_list = []
		for card in self.deck_:
			temp_list.append(card.card_info())
		return temp_list
	def hand_size(self):
		return len(self.hand_)
	def draw(self): 
		card = random.choice(self.deck_)
		self.deck_.remove(card)
		return card
	def discard(self):
		for card in self.hand_:
			self.hand_.remove(card)
		
def shuffle(game_cards):
	random.shuffle(game_cards)
	return game_cards

# Game start logic
def start():
	deck = Deck()
	game_cards = deck.create_deck()
	cards = shuffle(game_cards) 
	return cards

def play(chosen_card,defender,player):
	chosen_card.type()
	if chosen_card.type() == "Number":
			#Ask defender for defence card
			# defence_card
			#defemder
			attacker_vaule = chosen_card.vaule()
			# defender_card.vaule
			#if attacker_vaule == defender_card.vaule():
			#elif attacker card < defender_card:
			#else:
	else:
		if chosen_card.card_ability() == "Jack":
			player.add_card(player.draw())
		elif chosen_card.card_ability() == "King":
			defender.damage_hp(5)
		elif chosen_card.card_ability() == "Queen":
			player.heal()
			round_num += 1
			turn = "Bot"
		else:
			player.wipe()

			


			


