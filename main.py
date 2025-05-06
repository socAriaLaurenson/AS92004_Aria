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
MIN = 5
MAX = 10

#ask for users name and introduce them to the game
print("Hi there!")
user_name = input("Welcome to the Te Reo Maori Quiz. Please enter your name:")
print("Hello", user_name)
print("This is a game to test your Te Reo Maori Vocabularly.")

#ask for there input on wether or not they would like to play
asking = False
while asking == False:
  try:
    start_game = input("Would you like to play (y/n)?: ")
    print("You answered", start_game)
    #making the code more robust so they can accept more answers 
    start_game = start_game.lower()
    start_game = start_game[0]
    
    if start_game == "y":
      print("Great! Let's play...")
      asking = True
  
    elif start_game == "n":
      print("See you later!")
      quit()
   
    else:
      print("Invalid Input. Please enter yes or no")
  
  except IndexError:
    print("Invalid input. Please enter yes or no")  
  
#explain how the game works
print("Now i'll explain how the game works...")
print("I will ask you to translate an enlish word to Te Reo Maori")
print("And you will type in your answer!")
print("You have 3 chances to answer right")
print("We will tell you your score along the way, and at the end give you a % of the questions you got right!")

#ask how many questions the player wants (5-10) + make it unbreakable using try/except

no_questions_ans = False
while no_questions_ans == False:
  try: 
    no_questions = int(input("How many questions would you like (5-10): "))
    if no_questions >= MIN and no_questions <= len(questions):
      print("You answered", no_questions)
      no_questions_ans = True
      
    else:
      print("Invalid Imput. Please enter a number from 5 - 10")
  except ValueError:
    print("Invalid input. Plese enter a number. e.g 6")
      
