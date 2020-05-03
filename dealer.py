from player import Player
from card_deck import CardDeck


class Dealer(Player):

    def __init__(self):
        super().__init__('Dealer', self)
        self.deck = CardDeck()
        self.busted = False
        self.black_jack = False
        self.is_processing_done = False
        self.is_standing = False


    def shuffle_deck(self):
        """
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> str(dealer.deck)[0:20]
        '10 8 10 6 8 9 3 10 2'
        """
        self.deck.shuffle()

    def signal_hit(self, player):
        """
        A method called by players when they want to hit
        Player objects should pass their `self` references to this method
        Should deal one card to the player that signalled a hit

        These doctests will not run properly if the `deal_to` method 
        in the `Player` class is not properly implemented

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, None)
        >>> dealer.signal_hit(player)
        >>> player.hand
        [10]
        """

        if player != None:
            player.deal_to(self.deck.draw())
        else:
            self.deal_to(self.deck.draw())

        


    def play_round(self):
        """
        A dealer should hit if his hand totals to 16 or less

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> dealer.play_round()
        >>> dealer.play_round()
        >>> dealer.hand
        [10, 8]
        """
        if len(self.hand) < 2:
            if len(self.hand) == 0:
                self.signal_hit(None)
                return
            if len(self.hand) == 1:
                self.signal_hit(None)
                if self.card_sum > 16 and self.card_sum < 21:
                    self.is_standing = True
                    return
                if self.card_sum == 21:
                    self.busted = True
                    self.black_jack = True
                    return
                if self.card_sum > 21:
                    self.busted = True
                    return
        if self.card_sum <= 16:
            while self.card_sum <= 16:
                self.signal_hit(None)
                if self.card_sum > 16 and self.card_sum < 21:
                    self.is_standing = True
                    break
                if self.card_sum == 21:
                    self.busted = True
                    self.black_jack = True
                    break
                if self.card_sum > 21:
                    self.busted = True
                    break
                    
    def get_name(self):
        return self.__class__.__name__
    
    def __str__(self):
        """Return string representation for str()."""
        return f'Dealer: {self.hand} 0/0/0'

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)