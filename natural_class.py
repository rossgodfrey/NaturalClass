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

    def claim_set(self, selected_cards, player):
        if is_set(selected_cards):# - if correct:
            print('Mmmm, delicious set!')
            # - remove those cards
            for card in selected_cards:
                self.deck.cards_in_play.remove(card)
            # - track player score   
            player.change_score(self.SET_LENGTH)
            # - deal cards
            self.deal_limit()
            if len(self.deck.cards_in_play) < self.SET_LENGTH:
                self.game_in_progress = False                
        else:    # - if incorrect:
            # - penalise player (track player score)
            print('smdh....')
            player.change_score(-self.SET_LENGTH)

    def deal_limit(self):
        self.deck.deal_number(max(self.NUM_STARTING_CARDS - len(self.deck.cards_in_play), 0))

    def declare_winners(self):
        players_by_score = sorted(self.players, key = lambda player: player.score, reverse = True)
        for player in players_by_score:
            print(f"{player.name}: {player.score}")
        # Create list of winners
        winner_names = [players_by_score[0].name]
        for player in players_by_score[1:]:
            if player.score == players_by_score[0].score:
                winner_names.append(player.name)
            else:
                break  
        print(f"Congratulations, {' and '.join(winner_names)}! You won!")

    def get_current_player(self):
        while True:
            try:
                input_name = input("Who are you? ")
                return next(player for player in self.players if player.name==input_name) # - returns the first thing that satisfies the condition
                break
            except StopIteration:
                print('Name not found; try again, dumbass. Players are:') 
                for player in self.players:
                    print(player)

    def get_selected_cards(self):
        selected_cards = []
        while len(selected_cards) < self.SET_LENGTH:
            try:
                index = int(input("Feed me a card. I'm so hungry! "))
                selected_cards.append(self.deck.cards_in_play[index])
            except ValueError:
                print("Enter the index of the card, bonehead.")
            except IndexError:
                print("Is there a card with that index? I didn't think so.")
        return selected_cards

    def play(self):
        self.deal_limit()     # - deal 9 cards
        while self.game_in_progress:    # - loop:
            #TODO: make cards look nicer!
            for i in range(len(self.deck.cards_in_play)):
                print(str(i) + '. ' + str(self.deck.cards_in_play[i]))
            #TODO: handle errors
            does_set_exist = input("Is there a set? I need food. (Answer 'y' for yes, 'n' for no.) ")    # - user says whether there's a set                
            if str.lower(does_set_exist) == "y":
                current_player = self.get_current_player()
                selected_cards = self.get_selected_cards()
                self.claim_set(selected_cards,current_player)
            else:    # - if no:
                if len(self.deck.undealt_cards) > 0:
                    self.deck.deal_number(self.SET_LENGTH)
                else:                    
                    self.game_in_progress = False
        self.declare_winners()

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
    def __str__(self):
        return self.name

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
            raise InvalidFeatureError

class InvalidFeatureError(Exception):
    pass

if __name__ == "__main__":
    STARTING_SCORE = 0
    while True:
        player_names = input("Who's there? (Enter player names separated by commas.) ").split(',')
        player_names = [name.strip() for name in player_names]
        if len(set(player_names)) != len(player_names):
            print('Names must be unique, numbskull.')
        else:
            break
    players = [Player(STARTING_SCORE, name) for name in player_names]
    Game(Deck(), players).play()

