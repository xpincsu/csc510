import pytest
from blackjack import blackjack
def test_blackjack():
    assert blackjack(5, 6, 7) == 18
    assert blackjack(5, 6, 8) == 19
    assert blackjack(5, 6, 9) == 20
    assert blackjack(7, 8, 9) == 'BUST'