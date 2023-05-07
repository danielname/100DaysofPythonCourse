class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}. (True/False)?: ").lower()
        self.check_answer(user_answer,self.question_list[self.question_number].answer)
        self.question_number += 1
        print(f"The current score is {self.score}/{self.question_number}. \n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")