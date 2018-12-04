from random import shuffle

def is_set(cards):  
  features = ["shading", "color", "number", "shape"]
  for feature in features:
      unique_values = set()
      for card in cards:
        unique_values.add(card[feature])
      #TODO: return error if len(u_v) == 0 or if len(u_v) > len(cards)
      if 1 < len(unique_values) < len(cards):
        return False              
  return True

class Game:
	def __init__(self, deck, players):
		self.deck = deck
		self.players = players

class Deck:
	def __init__(self):
		self.undealt_cards = []
		shadings = ["solid", "striped", "empty"]
		colors	= ["red", "green", "purple"]
		shapes	= ["oval", "diamond", "squiggle"]
		numbers	= ["one", "two", "three"]
		for shading in shadings:
			for color in colors:
				for shape in shapes:
					for number in numbers:
						self.undealt_cards.append(Card(shading, color, shape, number))
		shuffle(self.undealt_cards)
		self.cards_in_play = []

	def deal(self, number_of_cards):
		for _ in range(number_of_cards):
			self.cards_in_play.append(self.undealt_cards.pop())

class Player:
	def __init__(self, score, name):
		self.score = score
		self.name	= name

class Card:
	def __init__(self, shading, color, shape, number):
		self.shading = shading
		self.color = color
		self.shape = shape
		self.number = number
	def __repr__(self):
		return f"({self.shading}, {self.color}, {self.shape}, {self.number})"

if __name__ == "__main__":
	d = Deck()
	d.deal(12)
	print(len(d.undealt_cards))
	print(len(d.cards_in_play))

