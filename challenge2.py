#!/usr/bin/python

import random

import requests

base_url = "https://opentdb.com/api.php"

def main():
    print("Welsom!  I'm going to give you some trivia questions.  Ready?")
    print("How many questions do you want?")
    amount = input(">>>")
    print("How difficult do you want the questions?  easy, medium, or hard")
    difficulty = input(">>>")

    trivia = requests.get(base_url + f"?amount={amount}&difficulty={difficulty}").json()

    question = trivia.get('results')[random.randint(0, int(amount) - 1)]["question"]

    print(question)

    correct_answer = trivia.get('results')[random.randint(0, int(amount) - 1)]["correct_answer"]
    incorrect_answers = trivia.get('results')[random.randint(0, int(amount) - 1)]["incorrect_answers"]
    
    #multi_select = incorrect_answers
    #multi_select.append(correct_answer)
    #multi_select = random.shuffle(multi_select)
    
    #print(multi_select)
    #print(f"Available answers: {multi_select}")
    #print("Select your answer:")
    #answer = input(">>>")

    print(f"Correct answer is: {correct_answer}")
    #print(f"Incorrect answers are: {incorrect_answers}")

    


if __name__ == "__main__":
    main()
