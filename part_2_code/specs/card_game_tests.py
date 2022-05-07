import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):



    def test_can_find_ace(self):
        new_card = Card('hearts', 1)
        self.assertEqual(True, CardGame.check_for_ace(self, new_card))

    def test_can_find_highest_card(self):
        card1 = Card('diamonds', 2)
        card2 = Card('clubs', 1)
        self.assertEqual(card1, CardGame.highest_card(self, card1, card2))

    def test_can_get_cards_total(self):
        card1 = Card('diamonds', 2)
        card2 = Card('clubs', 1)
        cards = [card1, card2]
        self.assertEqual("You have a total of " + str(card1.value+card2.value), CardGame.cards_total(self, cards))

