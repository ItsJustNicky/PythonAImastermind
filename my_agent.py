__author__ = "<Nicky Patterson>"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "<nicky.patterson1633@gmail.com>"


from itertools import product


import numpy as np

from mastermind import evaluate_guess


class MastermindAgent():
    """
              A class that encapsulates the code dictating the
              behaviour of the agent playing the game of Mastermind.

              ...

              Attributes
              ----------
              code_length: int
                  the length of the code to guess
              colours : list of char
                  a list of colours represented as characters
              num_guesses : int
                  the max. number of guesses per game

              Methods
              -------
              AgentFunction(percepts)
                  Returns the next guess of the colours on the board
              """

    def __init__(self, code_length, colours, num_guesses):
        """
        :param code_length: the length of the code to guess
        :param colours: list of letter representing colours used to play
        :param num_guesses: the max. number of guesses per game
        """
        self.code_length = code_length
        self.colours = colours
        self.num_guesses = num_guesses
        self.possible_guesses = None

    def generate_possible_guesses(self):
        """
        A method used to generate a list of all possible guesses at the begining
        :return Returns a list of every possible guess the agent is able to make for use of evaluation:
        """
        return list(product(self.colours, repeat=self.code_length))

    def first_Guess(self):
        """
        A method that creates the first guess of a game
        :return The first guess of the game comprimised of the colours available:
        """
        colours_len = len(self.colours)
        if colours_len >= 2:
            if self.code_length == 1:
                first_guess = [self.colours[0]]
            if self.code_length == 2:
                first_guess = [self.colours[0], self.colours[1]]
            if self.code_length == 3:
                first_guess = [self.colours[0], self.colours[0], self.colours[1]]
            if self.code_length == 4:
                first_guess = [self.colours[0], self.colours[0], self.colours[1], self.colours[1]]

            elif self.code_length > 4:
                if self.code_length <= colours_len:
                    first_guess = self.colours[:self.code_length]
                else:
                    first_guess = [self.colours[i % colours_len] for i in range(self.code_length)]


        return first_guess

    def new_game(self):
        """
        A method used to call the generate possible move method at the beginning of a new game, needed because otherwise
        the possible guesses from the last game are retained

        """
        self.possible_guesses = self.generate_possible_guesses()

    def AgentFunction(self, percepts):
        """
        The Agents desicison making, it employs the first guess method on turn one, and from there uses evaluate_guess
        method from the mastermind class to evaluate all guesses currently available, similar to the tick-tack-toe agent
        it then adds the guesses found to be positive using this method to a list of consistent guesses, going with the
        first guess in the list
        :param percepts: all the stuff the agent sees playing the game
        :return actions: The next guess the agent makes
        """
        guess_counter, last_guess, in_place, in_colour = percepts

        if guess_counter == 0:
            actions = self.first_Guess()
            self.new_game()

        else:
            effectiveGuesses = []
            for possible_guess in self.possible_guesses:
                rightPlace, rightColour = evaluate_guess(possible_guess, last_guess)
                if rightPlace == in_place and rightColour == in_colour:
                    effectiveGuesses.append(possible_guess)


            self.possible_guesses = effectiveGuesses

            actions = list(self.possible_guesses[0])

        return actions
