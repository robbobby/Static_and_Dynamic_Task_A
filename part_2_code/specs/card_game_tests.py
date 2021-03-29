import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        
        # Cards
        self.card1 = Card("Hearts", 7)
        self.card2 = Card("Spades", 2)
        self.card3 = Card("Diamons", 1)

        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        check_if_ace = CardGame.check_for_ace(self, self.card3)
        self.assertEqual(True, check_if_ace)

    def test_highest_card(self):
        highest_card = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(7, highest_card.value)

    def test_cards_total(self):
        cards_total = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 10", cards_total)