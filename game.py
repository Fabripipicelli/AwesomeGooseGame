

from typing import Optional, Tuple
import random


class Game:
    
    def __init__(self, player1: str, player2: str) -> None:
        self.player1 = player1
        self.player2 = player2
        # Save player1 data in self.player1
        self.spaceP1 = 0
        self.spaceP2 = 0
        self.current_player = self.player1
        self.previous_roll = None

    
    def get_player1_name(self) -> str:
        "Returns the name of Player 1 as a string."
        return self.player1
    
    def get_player2_name(self) -> str:
        "Returns the name of Player 2 as a string."
        return self.player2
    
    def get_player1_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 1 is currently on"""
        if self.spaceP1 == 0:
            return None
        else:
            return self.spaceP1

    
    def get_player2_space(self) -> Optional[int]:
        """Returns either None (for Start) or the space number player 2 is currently on"""
        if self.spaceP2 == 0:
            return None
        else:
            return self.spaceP2
        
    def get_current_player(self) -> str:
        """Returns the name of the current player."""
        return self.current_player
    
    def roll_dice(self) -> None:
        """Updates the game in-place by rolling dice."""
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if self.current_player == self.player1:
            new_pos = self.spaceP1 + dice1 + dice2
            if new_pos > 63:
                pass
            else:
                if new_pos == self.spaceP2:
                    self.spaceP2 = self.spaceP1
                self.spaceP1 = new_pos
            self.current_player = self.player2
        else:
            new_pos = self.spaceP2 + dice1 + dice2
            if new_pos > 63:
                pass
            else:
                if new_pos == self.spaceP1:
                    self.spaceP1 = self.spaceP2
                self.spaceP2 = new_pos
            self.current_player = self.player1

        self.previous_roll = (dice1, dice2)

        
    def get_last_dice_roll(self) -> Optional[Tuple[int, int]]:
        """Returns either None or a pair of die rolls, like (2, 6)"""

        return self.previous_roll
        
    def is_over(self) -> bool:
        """Returns True if game is over."""
        gameover = False
        if (self.spaceP1 == 63) | (self.spaceP2 == 63):
            gameover = True
        return gameover
    
    def get_winner(self) -> Optional[str]:
        """Returns None (if the game is not over) or the name of the winner"""
        winner = None
        if self.is_over():
            winner = self.current_player
        return winner
    
    
    