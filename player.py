import random


class Player:

    def __init__(self, name, dealer):

        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.hand = []
        self.name = name
        self.dealer = dealer
        self.busted = False
        self.black_jack = False
        self.is_processing_done = False
        self.is_standing = False


    def decide_hit(self):
        # DO NOT MODIFY
        return random.choice([True, True, False])

    def deal_to(self, card_value):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.hand
        [11]
        >>> player.deal_to(10)
        >>> player.hand
        [11, 10]
        """
        self.hand.append(card_value)

    @property
    def card_sum(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(2)
        >>> player.card_sum
        2
        >>> player.deal_to(10)
        >>> player.card_sum
        12
        """
        sum = 0
        for card in self.hand:
            sum += card


        return sum

    def play_round(self, itrator=2):
        """
        >>> from dealer import Dealer
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, dealer)

        We see that after the first call the play_round, we have only hit once as dictated by decide_hit
        >>> player.play_round()
        >>> player.hand
        [10]

        After calling play_round again, decide_hit has decided to stand
        >>> player.play_round()
        >>> player.hand
        [10]

        After a third call to play_round, we've decided to hit, but busted!
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]

        After a final call to play_round, our hand shouldn't change since we've already busted
        >>> player.play_round()
        >>> player.hand
        [10, 8, 10]
        """

  
        if itrator <= 1:
            if itrator == 0:
                if self.decide_hit():
                    self.dealer.signal_hit(self)
                    return
                return
            if itrator == 1:
                if self.decide_hit():
                    self.dealer.signal_hit(self)
                    if self.card_sum == 21:
                        self.busted = True
                        self.black_jack = True
                        return
                    elif self.card_sum > 21:
                        self.busted = True
                        return
                return

        while (self.decide_hit() and self.busted == False):
            self.dealer.signal_hit(self)
            if self.card_sum == 21:
                self.busted = True
                self.black_jack = True
            elif self.card_sum > 21:
                self.busted = True
        if self.busted == False:
            self.is_standing = True

                        

    def discard_hand(self):
        """
        >>> player = Player(None, None)
        >>> player.deal_to(11)
        >>> player.deal_to(5)
        >>> player.discard_hand()
        >>> player.hand
        []
        """
        self.hand = []
        self.busted = False
        self.black_jack = False
        self.is_processing_done = False
        self.is_standing = False


    

    def record_win(self):
        """
        >>> player = Player(None, None)
        >>> player.record_win()
        >>> player.wins
        1
        """
        self.wins += 1

    def record_loss(self):
        """
        >>> player = Player(None, None)
        >>> player.record_loss()
        >>> player.losses
        1
        """

        self.losses += 1

    def record_tie(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.ties
        1
        """

        self.ties += 1

    def reset_stats(self):
        """
        >>> player = Player(None, None)
        >>> player.record_tie()
        >>> player.record_loss()
        >>> player.record_win()
        >>> player.reset_stats()
        >>> player.ties
        0
        >>> player.wins
        0
        >>> player.losses
        0
        """
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.hand = []
        self.busted = False
        self.black_jack = False
        self.is_processing_done = False
        self.is_standing = False


    def get_name(self):
        return self.__class__.__name__

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.name}: {self.hand} {self.wins}/{self.ties}/{self.losses}'


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)