from tkinter.messagebox import QUESTION


class Question: 

    QUESTIONS={
        "What is the capital of Finland": "lisabon",
        "Who painted the Mona Lisa": "Leonardo da Vinci",
        "What's a baby rabbit called?": "kittens",
        "Which is the highest grossing Harry Potter film?": "Harry Potter and the Deathly Hallows Part 2'"
    }

    def __init__(self, question, answer):        
        self.question = question        
        self.answer = answer

    test=""
