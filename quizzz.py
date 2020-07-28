import requests
import json
import random
import html
url = "https://opentdb.com/api.php?amount=1"

score_correct = 0
score_incorrect = 0
endgame = True
while endgame:
    r = requests.get(url)
    if(r.status_code != 200):
        print("Error occured")
        endgame = False
    else:
        vaild_answer = False
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)
        print()
        print(html.unescape(question))
        for answer in answers:
            print(str(answer_number)+" - "+html.unescape(answer))
            answer_number += 1
        while not vaild_answer:
            try:
                user_answer = (input("Type number of correct answer: "))
                if int(user_answer) in [1, 2, 3, 4]:
                    vaild_answer = True
                else:
                    print("Invalid Answer\n")
            except:
                print("Invalid Answer\n")
        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongratulation you answered correctly")
            score_correct += 1
        else:
            print("\nSorry "+html.unescape(user_answer) +
                  " is not correct answer.Correct answer is "+html.unescape(correct_answer))
            score_incorrect += 1

        print("\n******************************************")
        print("Your Score is: ")
        print("incorrect answers "+str(score_incorrect))
        print("Correct answers "+str(score_correct))
        print("******************************************")
        check = input(
            "\npress 'q' or 'quit' to quit or press enter to play again: ")
        if check.lower() in ['q', 'quit']:
            endgame = False

print("\nThanks for playing")
