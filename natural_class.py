from random import shuffle

def is_set(cards):    
    features = ["shading", "color", "number", "shape"]
    for feature in features:
        unique_values = set()
        for card in cards:
            unique_values.add(card.get_value(feature))
        #TODO: return error if len(u_v) == 0 or if len(u_v) > len(cards)
        if 1 < len(unique_values) < len(cards):
            return False                            
    return True

class Game:    
    def __init__(self, deck, players):
        #TODO: allow 'deck' to be omitted, in which case default deck is created
        self.deck = deck
        self.players = players
        self.NUM_STARTING_CARDS = 12
        self.SET_LENGTH = 3
        self.game_in_progress = True

    def claim_set(self, selected_cards):
        if is_set(selected_cards):# - if correct:
            # - remove those cards
            for card in selected_cards:
                self.deck.cards_in_play.remove(card)
            # - track player score            
            # TODO: What if there's more than one player?
            self.players[0].change_score(self.SET_LENGTH)
            # - deal cards
            self.deal_limit(self.deck)
            if len(self.deck.cards_in_play) < self.SET_LENGTH:
                self.game_in_progress = False
            # TODO?  - if < 3 cards in play area, end game                 
        else:    # - if incorrect:
            # - penalise player (track player score)
            self.players[0].change_score(-self.SET_LENGTH)

    def deal_limit(self, deck):
        self.deck.deal_number(max(self.NUM_STARTING_CARDS - len(self.deck.cards_in_play), 0))

    def play(self):
        self.deal_limit(self.deck)     # - deal 9 cards
        while self.game_in_progress:    # - loop:
            #TODO: make cards look nicer!
            for i in range(len(self.deck.cards_in_play)):
                print(str(i + 1) + '. ' + str(self.deck.cards_in_play[i]))
            #TODO: handle errors
            does_set_exist = input("Is there a set? I need food. (Answer 'y' for yes, 'n' for no.) ")    # - user says whether there's a set                
            if str.lower(does_set_exist) == "y":
                selected_indices = []
                for _ in range(self.SET_LENGTH):
                    selected_indices.append(int(input("Feed me a card. I'm so hungry! ")) - 1)    # - if yes: evaluate chosen cards    
                selected_cards = []    
                for integer in selected_indices:
                    selected_cards.append(self.deck.cards_in_play[integer])
                self.claim_set(selected_cards)
            #finish this
            else:    # - if no:
                if len(self.deck.undealt_cards) > 0:
                    self.deck.deal_number(self.SET_LENGTH)
                else:                    
                    self.game_in_progress = False
        max_score = max([p.score for p in self.players])
        winners = [p for p in self.players if p.score == max_score]

        # winners = [player for player in self.players if player.score == max(self.players, key = lambda player: player.score).score]

        # highest = max(self.players, key = lambda player: player.score)
        # winners = [player for player in self.players if player.score == highest.score]

        # winners = list(filter(lambda player: player.score == max([x.score for x in self.players]), self.players))

        # best_score = max([player.score for player in self.players])
        # winners = list(filter(lambda player: player.score == best_score, self.players))

        # highest = max(self.players, key = lambda p: p.score)
        # winners = list(filter(lambda p: p.score == highest.score, self.players))

        # scores = {player: player.score for player in self.players}
        # winners = list(filter(lambda player: scores[player] == max(scores), scores))

        # scores = {player: player.score for player in self.players}
        # winners = [player for player in scores if scores[player] == max(scores.values())]

        # winners = []
        # for p in self.players:
        #     if not winners or p.score > winners[0].score:
        #         winners = [p]
        #     elif p.score == winners[0].score:
        #         winners.append(p)

class Deck:
    def __init__(self):
        self.undealt_cards = []
        shadings = ["solid", "striped", "empty"]
        colors    = ["red", "green", "purple"]
        shapes    = ["oval", "diamond", "squiggle"]
        numbers    = ["one", "two", "three"]
        for shading in shadings:
            for color in colors:
                for shape in shapes:
                    for number in numbers:
                        self.undealt_cards.append(Card(shading, color, shape, number))
        shuffle(self.undealt_cards)
        self.cards_in_play = []

    def deal_number(self, number_of_cards):
        for _ in range(min(number_of_cards, len(self.undealt_cards))):
            self.cards_in_play.append(self.undealt_cards.pop())

class Player:
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def change_score(self, num_points):
        self.score = max(0, self.score + num_points)

class Card:
    def __init__(self, shading, color, shape, number):
        self.shading = shading
        self.color = color
        self.shape = shape
        self.number = number        
    def __repr__(self):
        return f"({self.shading}, {self.color}, {self.shape}, {self.number})"
    def get_value(self, feature):
        if feature == "shading":
            return self.shading
        elif feature == "color":
            return self.color
        elif feature == "shape":
            return self.shape
        elif feature == "number":
            return self.number
        else:
            print('Go fuck yourself. Give a real feature, asshole.') #TODO: Raise error


if __name__ == "__main__":
    Game(Deck(), [Player(0, 'Tomo-Ross')]).play()

