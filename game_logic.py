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
		#if self.deck_ len greater than  one then
		card = random.choice(self.deck_)
		self.deck_.remove(card)
		return card
		# Else refill decks,
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
		
def shuffle(game_cards):
	random.shuffle(game_cards)
	return game_cards

# Game start logic
def start():
	deck = Deck()
	game_cards = deck.create_deck()
	cards = shuffle(game_cards) 
	return cards

def play(chosen_card,bot_card,player,bot):
	chosen_card.type()
	bot_card.type()
	print(chosen_card.type())
	print(bot_card.type())
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
			return discard_cards,winning_card
		
		else:
			print("Card comparision error")
	elif chosen_card.type() == "Number" and bot_card.type() == "Ability":
		if bot_card.card_ability() == "Jack":
			bot.add_card(bot.draw())
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
			player.add_card(player.draw())
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
			player.add_card(player.draw())
			player.add_card(player.draw())
			player.damage_hp(5)
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "Queen":
			player.add_card(player.draw())
			player.add_card(player.draw())
			bot.heal()
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		elif chosen_card.card_ability() == "Jack" and bot_card.card_ability() == "Jack":
			player.add_card(player.draw())
			player.add_card(player.draw())
			bot.add_card(bot.draw())
			bot.add_card(bot.draw())
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
			bot.add_card(bot.draw())
			bot.add_card(bot.draw())
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
			bot.add_card(bot.draw())
			bot.add_card(bot.draw())
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
		else:
			player.remove_card(chosen_card)
			bot.remove_card(bot_card)
			player.wipe()
			bot.wipe()
	else:
		print("Bug, no type logic registered correctly")

			


			


