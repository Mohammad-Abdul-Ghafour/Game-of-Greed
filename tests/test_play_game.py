# from game_of_greed.game import Game
from tests.flow.flo import Flo

def test_quitter():
    Flo.test('tests/flow/quitter.sim.txt')

def test_one_and_done():
    Flo.test('tests/flow/one_and_done.sim.txt')