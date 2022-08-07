#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo
def make_a_guess(levels):
  print(f"You have {levels} attempts remaining to guess the number.")
  
  thinking_numbers = randint(1,101)
  
  your_guess = int(input("Make a guess: "))
  if your_guess == thinking_numbers:
    print(f"You got it! The answer was {your_guess}.")
  while your_guess != thinking_numbers:
    if your_guess > thinking_numbers:
           print("""Too high Guess again""")
    elif your_guess < thinking_numbers:
            print("""Too low Guess again.""")
    print(f"You have {levels-1} attempts remaining to guess the number")
    
    your_guess = int(input("Make a guess: "))
    if your_guess != thinking_numbers:
         
         
         levels -= 1
         if levels == 1:
           your_guess = thinking_numbers
           print("You've run out of guesses, you lose.")
    else:
      print(f"You got it! The answer was {your_guess}.")  
  

  
print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.Take a guess""")
EASY_MODE = 10
HARD_MODE = 5
levels=input("Choose a difficulty. Type 'easy' or 'hard': ")
if levels =='easy':
  
  make_a_guess(levels=EASY_MODE)
elif levels == 'hard':
   make_a_guess(levels=HARD_MODE)