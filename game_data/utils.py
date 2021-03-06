# Authors: Bryan Hunter and Kent Lewis

# Custom imports (PIP packages):
from art import tprint

# Normal built-in packages:
import os
from os.path import sep
import random
from sys import platform


# Colors for the text!
class TextColors:
    
    # Text colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    PROMPT = '\033[96m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET_ALL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37m'
    CYAN = '\033[36m'
    BLUE = '\033[34m'
    BLACK = '\033[30m'
    
    # Background colors:
    GREYBG = '\033[100m'
    REDBG = '\033[101m'
    GREENBG = '\033[102m'
    YELLOWBG = '\033[103m'
    BLUEBG = '\033[104m'
    PINKBG = '\033[105m'
    CYANBG = '\033[106m'
    
    # Misc:
    BRIGHT = '\033[1m'
    NORMAL_BRIGHTNESS = '\033[22m'

class Utils():      

    # Initialize the Utils() class:
    def __init__(self):
        self.print_platform()
        self.tcolors = TextColors()
    
    # Print the user's current OS:
    def print_platform(self):
        print("Current platform: {}\n".format(platform.capitalize()))
        return platform.lower()
    
    # Clear the console, if needed:
    def clear_console(self):
        command = 'cls' if os.name in ('nt', 'dos') else 'clear'
        os.system(command)

    #Print the guess line and guessed letters
    def print_guess_string(self, guess_string):
        print(" ".join(guess_string))
    
    # Prints a fancy word in the console:
    def print_fancy(self, msg, font):
        if font != None:
            tprint(msg, font)
        else:
            tprint(msg)
    
    # Gets the player's guess input:
    def get_player_input(self, guess_input):  
        _input = str(input(guess_input)).lower()
        if _input.isalpha():
            if len(_input) > 1:
                raise ValueError("Too many letters!")
            else:
                return str(_input)
        print("\n\n{}Please input a valid letter and try again.{}\n".format(self.tcolors.YELLOW, self.tcolors.RESET_ALL))

    # Give the user feedback for how they are doing:
    def get_feedback(self, scenario, user_guess="guess"):
        if scenario in ["miss", "wrong", "incorrect", 0]:
            if user_guess in ["guess", None]: 
                feedback = ["Sorry, try again!", "Try another letter. :)"]
                return random.choice(feedback)
            else:
                guess_feedback = [f"Sorry, {user_guess} is not a correct letter.", f"'{user_guess}'? Really?"]
                return random.choice(guess_feedback)
        if scenario in ["correct", "right", 1]:
            if user_guess in ["guess", None]: 
                feedback = ["You guessed a letter!", "That was a great guess!"]
                return random.choice(feedback)
            else:
                guess_feedback = [f"'{user_guess}' is a correct letter!", f"'{user_guess}' is correct! Congrats on not getting a darwin award!"]
                return random.choice(guess_feedback)
        if scenario in ["win", "victory", 2]:
            feedback = ["You Win!", "That's some good guessin' there partner.", "You guessed all the letters!", "I like letters.", "Ready for another round, freddy?"]
            return random.choice(feedback)
        if scenario in ["quit", "exit", 3]:
            feedback = ["See you later." ,"/kill game", "Going so soon? Awww...","We will meet... again"]
            return random.choice(feedback)
