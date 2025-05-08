"""
Te Reo Maori Quiz
By Aria Laurenson
11DGT
"""

import random

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
user_name = input("Welcome to the Te Reo Maori Quiz. Please enter your name: ")
print("Hello", user_name)
print("This is a game to test your Te Reo Maori Vocabulary.")

#ask for their input on whether or not they would like to play
asking = False
while not asking:
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
print("I will ask you to translate an English word to Te Reo Maori")
print("And you will type in your answer!")
print("You have 3 chances to answer right")
print("We will tell you your score along the way, and at the end give you a % of the questions you got right!")

#ask how many questions the player wants (5-10) + make it unbreakable using try/except
no_questions_ans = False
while not no_questions_ans:
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
  question = selected_questions[i]
  correct_answer = selected_answers[i]
  #so user_atempts and the chance variable can determin if they have anymore tries at the question
  user_atempts = 0
  got_it_right = False
  
  
  while user_attempts < chances:
    user_answer = input(prompt, question"? ").strip()
    
    if user_answer.lower() == correct_answer.lower():
      print("Ka pai! That is correct.")
      score += 1
      got_it_right = True
      break
