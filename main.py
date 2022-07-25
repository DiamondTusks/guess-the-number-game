import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  guesses = 10
elif difficulty == "hard":
  guesses = 5
else:
  print("Not an option.")

def play_game():
  random_number = random.randint(1,100)
  attempts = guesses
  for _ in range(attempts):
    print(f"You have {attempts} attempts left.")
    guess = int(input("Pick a number berween 1 and 100: "))
    attempts -= 1
    if attempts == 0:
      print("All attempts used. You lose.")
    else:
      if guess == random_number:
        print("Correct!!! You win!")
      elif guess > random_number:
        print("Too high.") 
      elif guess < random_number:
        print("Too low.") 
      else:
        print("Wrong number") 
    
  
play_game()

