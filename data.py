
class Question: 

    QUESTIONS={
        "What is the capital of Finland": "lisabon",
        "Who painted the Mona Lisa": "Leonardo da Vinci",
        "What's a baby rabbit called?": "kittens",
        "Which is the highest grossing Harry Potter film?": "Harry Potter and the Deathly Hallows Part 2'"
    }    
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
   
question=Question()
print(question.get_question())
print(question.get_answer())
