import os
import sys
 
import random
 
 
class QuestionsForQuiz:
    def __init__(self, question, answer,):
        self.question_ = question
        self.answer_   = answer
        
        self.correct_  = False
 
    @property
    def correct(self):
        return self.correct_
 
    @property
    def answer(self):
        return self.answer_
 
    @property
    def question(self):
        return self.question_
    
    
 
    def check_answer(self, answer) :
        "This function will check if the answer is correct  "
        answer = answer.lower()
 
        if answer == self.answer_:
            self.correct_ = True
            return True
        else:
            return False
 
class QuestionsGame:
    "This class answers for the game "
    def __init__(self):
        self.qAa = {}
 
    @property
    def array(self):
        return self.qAa
 
    @property
    def questions_and_answers(self):
        if len(self.qAa) == 0:
            return "None\n"
            
        index   = 1
        message = ""
 
        for question, answer  in self.qAa.items():
            message += f"{index}. \nQ: {question}\n"\
                f"A: {answer}\n\n"
 
            index += 1
 
        return message
 
    def add(self, question, answer,) :
        "This function adds question"

        self.qAa[question] = answer.lower()
 
    def clear(self):
        self.qAa.clear()
 
    def game(self):
        if len(self.qAa) == 0:
            return 0
 
        to_shuffle = list(self.qAa.items())
        
        random.shuffle(to_shuffle)
 
        self.qAa = dict(to_shuffle)
 
        for question, answer in self.qAa.items():
            model = QuestionsForQuiz(question, answer)
 
            while not model.correct:
                user_answer = input(f"{question} > ")
                is_correct  = model.check_answer(user_answer)
 
                if not is_correct:
                    print("The answer is not correct")
                else:
                    print("The answer is correct")
 
                print()
 
def main():
    to_print = "Welcome\n"
 
    game = QuestionsGame()
 
    while True:
        action = input(
            f"{to_print}\n"
            "1. Add new question\n"
            "2. Play\n"
            "3. Reset\n"
            "4. List\n"
            "5. Exit\n"
            "> "
        )
 
        print()
 
        if action == "1":
            game.add(
                
                question = input("Question > "),
                answer   = input("Answer   > "),
            )
 
            to_print = "Question added\n"
        
        if action == "2":
            process = game.game()
 
            if process == 0:
                to_print = "The game cannot be started. No questions asked\n"
            else:
                game.clear()
                
                to_print = "You have answered all the questions\n"
        if action == "3":
            game.clear()
        
            to_print = "The list of questions has been cleared\n"
        if action == "4":
            to_print = game.questions_and_answers
        if action == "5":
            sys.exit(0)
 
        os.system("CLS")
 
if __name__ == "__main__":
    main()