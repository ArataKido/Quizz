
from re import I


class QuestionsForQuiz: 
    """
    This class does something but i do not know what it does
    """
    def __init__(self, question, answer) :
        self.question=question
        self.answer=answer
    
    def get_question(self, question):
        pass
    def get_answer(self, answer):
        pass
        

def main():
    """
    This function  gets a questions and answers from the user 

    """
    
    is_on=True
    while is_on:
        print("Welcome player.")
        if input("Do you want to add questions? y/n ").lower()=="y":
            key=input("Print the question ")
            value=input("Print the answer ")
            QUESTIONS.update({key:value})
            if input("Do you want to add more questions? y/n ").lower()=="y":
                key=input("Print the question ")
                value=input("Print the answer ")
                QUESTIONS.update({key:value})
            else:
                imp_question()
                is_on=False
        else:
            imp_question()
            is_on=False        
def imp_question():
    for item in QUESTIONS:
        QuestionsForQuiz(item,QuestionsForQuiz[item])

def imp_answer():
    pass
QUESTIONS={}


if __name__=="__main__":
    main()