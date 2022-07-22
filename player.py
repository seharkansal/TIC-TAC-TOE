import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    #we  want all players to get their next move
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #gets a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + 's turn. Input move (0-9): ')
            '''
            we will check that this is a correct value by tryin to cast
            it to an integer, and if its not, then we say its invalid
            if that spot is not available on the board, we also say its invalid
            '''
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are successfull, then yay!

            except ValueError:
                print("invalid square, try again")

        return val

