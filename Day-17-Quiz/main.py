from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

list_question = []

for index in question_data:
    new_question = Question(index["question"], index["correct_answer"])
    list_question.append(new_question)

quiz = QuizBrain(list_question)

while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score is {quiz.score}")
