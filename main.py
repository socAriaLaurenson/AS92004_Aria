""" 
Te Reo Maori Quiz
By Aria Laurenson
11DGT
"""

#set up variables
questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]
answers = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
prompt = "What is Te Reo Maori for ..."
score = 0
chances = 3

#ask for users name and introduce them to the game
print("Hi there!")
user_name = input("Welcome to the Te Reo Maori Quiz. Please enter your name:")
print("Hello", user_name)
print("This is a game to test your Te Reo Maori Vocabularly.")

#using conditionals to determine what happens after they enter an input answering the start_game question
start_game_answer = False
while start_game_answer == False:
  try:
    start_game = input("Would you like to play? (y/n): ")
    start_game = start_game[0]
    start_game = start_game.lower()

    if start_game == "y":
      print("Great! Let's get started.")
      start_game_answer == True

    elif start_game == "n":
      print("See you later!")
      quit()
  
    else:
      print("Input Error, please answer yes or no")
    
    except
