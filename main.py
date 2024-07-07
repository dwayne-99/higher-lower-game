from game_data import data
import random
import os

def clear_screen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a" # returns True
  else:
    return guess == "b" # returns False

score = 0
game_should_continue = True 
account_b = random.choice(data)

while game_should_continue:

  account_a = account_b # temporary variable to hold the previous account
  account_b = random.choice(data) # pick a random account for B
  
  while account_a == account_b:
    account_b = random.choice(data)
  # ensure A and B are different celebrities
  
  print(f"Compare A: {format_data(account_a)}.")
  print("")
  print(f"Against B: {format_data(account_b)}.")
  print("")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  clear_screen()
  
  if is_correct:
    score += 1
    print("")
    print(f"You're right! Current score: {score}")
    print("")
  else:
    game_should_continue = False
    print("")
    print(f"Sorry thats wrong. Final score: {score}")
