import pytest
import main

def test_deck():
    deck = main.Deck()
    assert len(deck.all_deck) == 36

def test_suits():
    deck = main.Deck()
    assert len(deck._suits) == 4

def test_player():
    deck = main.Deck()
    deck.mix_deck()
    deck.hand_cards()
    assert len(deck.player_hand) == 6

def test_computer():
    deck = main.Deck()
    deck.mix_deck()
    deck.hand_cards()
    assert len(deck._computer_hand) == 6

def test_rest_deck():
    deck = main.Deck()
    deck.mix_deck()
    deck.hand_cards()
    assert len(deck._ls_mix_deck) == 24