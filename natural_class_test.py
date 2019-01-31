import unittest
from natural_class import is_set, Card, Game, Deck, Player

class TestClaimSet(unittest.TestCase):

    def test_claimSet_isRealSet_differentCardsInPlay(self):
        game = Game(Deck(), [Player(0, "Tomo-Ross")])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('empty', 'red', 'diamond', '3'),
                                   Card('striped', 'purple', 'swirl', '1'),
                                   Card('filled', 'red', 'swirl', '3')]
        old_cards_in_play = game.deck.cards_in_play[:]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'swirl', '1'),
                                   # Card('filled', 'purple', 'oval', '2'),
                                   # Card('empty', 'purple', 'diamond', '3'),
                                   # Card('striped', 'red', 'swirl', '1'),
                                   # Card('filled', 'purple', 'oval', '2'),
                                   # Card('empty', 'purple', 'diamond', '3'),
                                   # Card('striped', 'red', 'swirl', '1'),
                                   # Card('filled', 'purple', 'oval', '2'),
                                   # Card('empty', 'purple', 'diamond', '3'),
                                   # Card('striped', 'red', 'swirl', '1')
                                   ]
        #Why does undealt_cards have so many cards? Because it created an error when there were only 3.
        #So let's see if this works.
        game.claim_set(old_cards_in_play[:3])
        self.assertNotEqual(set(old_cards_in_play), set(game.deck.cards_in_play))

    def test_claimSet_isNotRealSet_sameCardsInPlay(self):
        game = Game(Deck(), [Player(0, "Tomo-Ross")])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('striped', 'red', 'oval', '3'),
                                   Card('filled', 'purple', 'oval', '1'),
                                   Card('filled', 'red', 'swirl', '3')]
        old_cards_in_play = game.deck.cards_in_play[:]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'swirl', '1'),
                                   # Card('filled', 'purple', 'oval', '2'),
                                   # Card('empty', 'purple', 'diamond', '3'),
                                   # Card('striped', 'red', 'swirl', '1'),
                                   # Card('filled', 'purple', 'oval', '2'),
                                   # Card('empty', 'purple', 'diamond', '3'),
                                   # Card('striped', 'red', 'swirl', '1'),
                                   # Card('filled', 'purple', 'oval', '2'),
                                   # Card('empty', 'purple', 'diamond', '3'),
                                   # Card('striped', 'red', 'swirl', '1')
                                   ]
        #Why does undealt_cards have so many cards? Because it created an error when there were only 3.
        #So let's see if this works.
        game.claim_set(old_cards_in_play[0:3])
        self.assertEqual(set(old_cards_in_play), set(game.deck.cards_in_play))

class TestIsSet(unittest.TestCase):

    def test_allCards_differentValuesForAllFeatures_isSet(self):
        cards = []
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('empty', 'red', 'diamond', '3'))
        cards.append(Card('striped', 'purple', 'swirl', '1'))
        self.assertTrue(is_set(cards))

    def test_allCards_sameValuesForAllFeatures_isSet(self):
        cards = []
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('filled', 'green', 'oval', '2'))
        self.assertTrue(is_set(cards))

    def test_allCards_differentValuesForTwoFeaturesAndSameValuesForOtherTwo_isSet(self):
        cards = []
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('filled', 'red', 'oval', '3'))
        cards.append(Card('filled', 'purple', 'oval', '1'))
        self.assertTrue(is_set(cards))

    def test_allCards_firstFeatureNotMeetSetCondition_isNotSet(self):
        cards = []
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('striped', 'red', 'oval', '3'))
        cards.append(Card('filled', 'purple', 'oval', '1'))
        self.assertFalse(is_set(cards))

    def test_allCards_lastFeatureNotMeetSetCondition_isNotSet(self):
        cards = []
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('filled', 'red', 'oval', '3'))
        cards.append(Card('filled', 'purple', 'diamond', '1'))
        self.assertFalse(is_set(cards))

    def test_allCards_noFeatureMeetSetCondition_isNotSet(self):
        cards = []
        cards.append(Card('empty', 'green', 'oval', '1'))
        cards.append(Card('filled', 'red', 'oval', '3'))
        cards.append(Card('filled', 'green', 'swirly', '1'))
        self.assertFalse(is_set(cards))

if __name__ == '__main__':
             unittest.main()