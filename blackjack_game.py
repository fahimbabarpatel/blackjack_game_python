from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):

        self.player_names = player_names
        self.player_list = []
        self.d = Dealer()



    def play_rounds(self, num_rounds=1):
        """

        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2)) # MOST OF TIME THIS LINE IS GOING TO  FAIL BECASUE OF NON DETERMINISTIC BEHAVIOUR
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """

        str_result = ""
        self.d.shuffle_deck()
        for player in self.player_names:
            self.player_list.append(Player(player, self.d))

        for round in range(num_rounds):
            # two cards first
            for itrator in range(2):
                for p_l in self.player_list:
                    p_l.play_round(itrator)
                self.d.play_round()
            # extra opportunity
            for p_l in self.player_list:
                p_l.play_round()
            self.d.play_round()

            self.decide_winner()
            if round == 0:
                str_result  += f'Round {round+1}\n'
            else:
                str_result  += f'\nRound {round+1}\n'
                
            str_result  += str(self.d) + '\n'
            for i, p_l in enumerate(self.player_list):
                if i == len(self.player_list) - 1:
                    str_result  += str(p_l)
                else:
                    str_result  += str(p_l) + '\n'
            self.reset_hand()
            self.d.shuffle_deck()
        
        return str_result

    
    
    def reset_hand(self):
        for p_l in self.player_list:
            p_l.discard_hand()
        self.d.discard_hand()    

    
    
    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()   # MOST OF TIME THIS LINE IS GOING TO  FAIL BECASUE OF NON DETERMINISTIC BEHAVIOUR
        >>> game.reset_game()
        >>> print(str(game.player_list[0]))
        Lawrence: [] 0/0/0
        >>> print(str(game.player_list[1]))
        Melissa: [] 0/0/0
        """
        for p_l in self.player_list:
            p_l.reset_stats()
        self.d.reset_stats() 

    
    def decide_winner(self):
        is_dealer_black_jack = False
        is_dealer_busted = False
        


        #1 checking black jack
        if self.d.black_jack:
            is_dealer_black_jack = True
        for p_l in self.player_list:
            if p_l.black_jack and is_dealer_black_jack:
                p_l.record_tie()
                p_l.is_processing_done = True
                
            elif p_l.black_jack and is_dealer_black_jack == False:
                p_l.record_win()
                p_l.is_processing_done = True
                
            elif p_l.black_jack == False and is_dealer_black_jack:
                p_l.record_loss()
                p_l.is_processing_done = True
                    
        
        if is_dealer_black_jack:
            return is_dealer_black_jack

        #2 checking busted
        if self.d.busted and self.d.black_jack == False:
            is_dealer_busted = True
        for p_l in self.player_list:
            if p_l.busted and is_dealer_busted and p_l.black_jack == False and p_l.is_processing_done == False:
                p_l.record_loss()
                p_l.is_processing_done = True
                
            elif p_l.busted == False and is_dealer_busted and p_l.is_processing_done == False:
                p_l.record_win()
                p_l.is_processing_done = True
                   
        
        if is_dealer_busted:
            return is_dealer_busted

        #3 checking card_sum
        if self.d.is_standing:
            dealer_hand_total =  self.d.card_sum
            for p_l in self.player_list:
                if p_l.busted and p_l.is_processing_done == False:
                    p_l.record_loss()
                    p_l.is_processing_done = True
                if p_l.is_standing  and p_l.card_sum < dealer_hand_total and p_l.is_processing_done == False:
                    p_l.record_loss()
                    p_l.is_processing_done = True
                if p_l.is_standing and p_l.card_sum == dealer_hand_total and p_l.is_processing_done == False:
                        p_l.record_tie()
                        p_l.is_processing_done = True
                if p_l.is_standing and p_l.card_sum > dealer_hand_total and p_l.is_processing_done == False:
                    p_l.record_win()
                    p_l.is_processing_done = True
                    
                        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)