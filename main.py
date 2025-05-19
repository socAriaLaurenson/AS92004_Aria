"""
Te Reo Māori Quiz
By Aria Laurenson
11DGT
"""

import random

#set up variables
questions = ["kia ora ", "haere rā ", "ae ", "Haratau ", "whero ", "kākāriki ", "Poutūterangi ", "Paengawhāwhā ", "mā ", "pango "]

answers = ["hello", "goodbye", "yes", "may", "red", "green", "march", "april", "white", "black"]

prompt = "What is the English translation of ..."
score = 0
chances = 3
MIN = 5
MAX = 10
################

#ask for users name and introduce them to the game
print("Hi there!")
user_name = input("Welcome to the Te Reo Māori Quiz. Please enter your name: ")
print("Hello", user_name)
print("This is a game to test your Te Reo Māori Vocabulary.")

#ask for their input on whether or not they would like to play
asking = False
while asking == False:
  try:
    start_game = input("Would you like to play (y/n)?: ")
    print("You answered", start_game)
    #making the code more robust so it accepts more answers 
    start_game = start_game.lower()
    start_game = start_game[0]
        
    if start_game == "y":
      print("Great! Let's play...")
      asking = True
        
    elif start_game == "n":
      print("See you later!")
      exit()
        
    else:
      print("Invalid input. Please enter yes or no.")
    
  except IndexError:
    print("Invalid input. Please enter yes or no.")  

#explain how the game works
print("Now I'll explain how the game works...")
print("I will ask you to translate an Te Reo Māori word to English")
print("And you will type in your answer!")
print("You have 3 chances to answer right")
print("We will tell you your score along the way, and at the end give you a % of the questions you got right!")

#ask how many questions the player wants (5-10) + make it unbreakable using try/except
no_questions_ans = False
while no_questions_ans == False:
  try: 
    no_questions = int(input("How many questions would you like (5-10): "))
    if MIN <= no_questions <= MAX:
      print("You answered", no_questions)
      no_questions_ans = True
        
    else:
      print("Invalid Input. Please enter a number from 5 - 10")
    
  except ValueError:
    print("Invalid input. Please enter a number. e.g 6")

# RANDOMIZE AND SELECT QUESTIONS + MATCHING ANSWERS
#make the questions and answers strings match with each other
qa_pairs = list(zip(questions, answers))
#shuffle the pairs
random.shuffle(qa_pairs)
#select the number of questions the user has asked for 
selected_pairs = qa_pairs[:no_questions]
selected_questions, selected_answers = zip(*selected_pairs)

# display selected questions and answers in a loop
for i in range(no_questions):
  #so it goes through the correct number of questions
  question = selected_questions[i]
  correct_answer = selected_answers[i]
  #so user_attempts and the chance variable can determine if they have anymore tries at the question
  user_attempts = 0
  got_it_right = False
  
  #use a loop so that while your number of attemps is smaller than chances, you can answer the question
  while user_attempts < chances:
    #add in variables and question
    user_answer = input("\n" + prompt + " " + question + "?").strip()
    print("you answered " + user_answer)
    
    #determine if the answer is correct (matching the answer variable) 
    if user_answer.lower() == correct_answer.lower():
      print("Ka pai! That is correct.")
      # add one to there score
      score += 1
      got_it_right = True
      break
    
    else:
      user_attempts += 1
      if user_attempts < chances:
        print("Try again! You have " + str(chances - user_attempts) + "chances left")
        
      else:
        print("Sorry, the correct answer was: " + correct_answer)
        
print("\n---Quiz Complete---")
print(user_name+ ", you got " + str(score) + " out of " +str(no_questions) + " correct.")
percentage = (score / no_questions) * 100
print("That's " + str(round(percentage, 1)) + " % correct!")

if percentage >= 50:
  print("Great job, You passed!")
  
else:
  print("You might need to work on this a bit...")
         
         
