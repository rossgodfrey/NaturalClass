import unittest
from natural_class import is_set, Card, Game, Deck, Player

class TestClaimSet(unittest.TestCase):

    def test_claimSet_isRealSet_differentCardsInPlay(self):
        orig_score = 0
        player = Player(orig_score, "Tomo-Ross")
        game = Game(Deck(), [player])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('empty', 'red', 'diamond', '3'),
                                   Card('striped', 'purple', 'squiggle', '1'),
                                   Card('filled', 'red', 'squiggle', '3')]
        old_cards_in_play = game.deck.cards_in_play[:]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'squiggle', '1')]
        game.claim_set(old_cards_in_play[:game.SET_LENGTH], player)
        self.assertNotEqual(set(old_cards_in_play), set(game.deck.cards_in_play))

    def test_claimSet_isNotRealSet_sameCardsInPlay(self):
        orig_score = 0
        player = Player(orig_score, "Tomo-Ross")
        game = Game(Deck(), [player])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('striped', 'red', 'oval', '3'),
                                   Card('filled', 'purple', 'oval', '1'),
                                   Card('filled', 'red', 'squiggle', '3')]
        old_cards_in_play = game.deck.cards_in_play[:]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'squiggle', '1')]
        game.claim_set(old_cards_in_play[:game.SET_LENGTH], player)
        self.assertEqual(set(old_cards_in_play), set(game.deck.cards_in_play))

    def test_claimSet_isRealSet_scoreGoesUpByLengthOfSet(self):
        orig_score = 0
        player = Player(orig_score, "Tomo-Ross")
        game = Game(Deck(), [player])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('empty', 'red', 'diamond', '3'),
                                   Card('striped', 'purple', 'squiggle', '1'),
                                   Card('filled', 'red', 'squiggle', '3')]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'squiggle', '1')]
        game.claim_set(game.deck.cards_in_play[:game.SET_LENGTH], player)
        self.assertEqual(orig_score + game.SET_LENGTH, game.players[0].score)

    def test_claimSet_isNotRealSetWithOrigScoreAboveSetLength_scoreGoesDownByLengthOfSet(self):
        orig_score = 10
        player = Player(orig_score, "Tomo-Ross")
        game = Game(Deck(), [player])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('striped', 'red', 'oval', '3'),
                                   Card('filled', 'purple', 'oval', '1'),
                                   Card('filled', 'red', 'squiggle', '3')]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'squiggle', '1')]
        game.claim_set(game.deck.cards_in_play[:game.SET_LENGTH], player)
        self.assertEqual(orig_score - game.SET_LENGTH, game.players[0].score)

    def test_claimSet_isNotRealSetWithOrigScoreZero_scoreStaysAtZero(self):
        orig_score = 0
        player = Player(orig_score, "Tomo-Ross")
        game = Game(Deck(), [player])
        game.deck.cards_in_play = [Card('filled', 'green', 'oval', '2'),
                                   Card('striped', 'red', 'oval', '3'),
                                   Card('filled', 'purple', 'oval', '1'),
                                   Card('filled', 'red', 'squiggle', '3')]
        game.deck.undealt_cards = [Card('filled', 'purple', 'oval', '2'),
                                   Card('empty', 'purple', 'diamond', '3'),
                                   Card('striped', 'red', 'squiggle', '1')]
        game.claim_set(game.deck.cards_in_play[:game.SET_LENGTH], player)
        self.assertEqual(orig_score, game.players[0].score)



class TestIsSet(unittest.TestCase):

    def test_allCards_differentValuesForAllFeatures_isSet(self):
        cards = []
        cards.append(Card('filled', 'green', 'oval', '2'))
        cards.append(Card('empty', 'red', 'diamond', '3'))
        cards.append(Card('striped', 'purple', 'squiggle', '1'))
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
        cards.append(Card('filled', 'green', 'squiggle', '1'))
        self.assertFalse(is_set(cards))

if __name__ == '__main__':
             unittest.main()