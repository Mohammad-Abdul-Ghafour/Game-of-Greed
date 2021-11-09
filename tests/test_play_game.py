# from game_of_greed.game import Game
from tests.flow.flo import Flo

def test_quitter():
    Flo.test('tests/flow/quitter.sim.txt')

def test_one_and_done():
    Flo.test('tests/flow/one_and_done.sim.txt')

def test_bank_first_for_two_rounds():
    Flo.test('tests/flow/bank_first_for_two_rounds.sim.txt')


def test_bank_one_roll_and_quit():
    Flo.test('tests/flow/bank_one_roll_then_quit.sim.txt')


def test_hot_dice():
    Flo.test('tests/flow/hot_dice.txt')

def test_zilch():
    Flo.test('tests/flow/zilch.sim.txt')

def test_zilch():
    Flo.test('tests/flow/cheat_and_fix.sim.txt')