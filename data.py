
class Question: 

    def __init__(self, question, answer) :
        self.question=question
        self.answer=answer

    def get_question(self,question):
        question=self.QUESTIONS
        for i in question:
            print(i)

    def get_answer(self, answer):
        answer=self.QUESTIONS
        for i in answer:
            print(answer[i])

def main():
    QUESTIONS={}
     

    is_on=True
    while is_on:
        print("Welcome player.")
        if input("Do you want to add questions? y/n ").lower()=="y":
            key=input("Print the question ")
            value=input("Print the answer ")
            QUESTIONS.update({key:value})
            if input("Do you want to add more questions? y/n ").lower()=="y":
                key_2=input("Print the question ")
                value_2=input("Print the answer ")
                QUESTIONS.update({key_2:value_2})
                print(QUESTIONS)
            else:
                break

        


if __name__=="__main__":
    main()