from data import question_data, more_questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
# for item in more_questions:
    question = Question(item["text"], item["answer"])
    # question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}")
