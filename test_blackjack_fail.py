import pytest
from blackjack import blackjack
def test_blackjack():
    assert blackjack(5, 6, 7) == 18
    assert blackjack(5, 6, 8) == 16
    assert blackjack(5, 6, 9) == 19
    assert blackjack(3, 4, 5) == 'BUST'