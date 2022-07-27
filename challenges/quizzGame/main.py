"""Quizz Game.
Project for Angela Wu's 100 days of code challenges.
Day # 17
"""
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:          # data.py module
    q = Question(ask=question["text"], answer=question["answer"])  # Returns new 'q' object
    question_bank.append(q)             # populate list with 'q' object

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nYou've completed the quiz!")
print(f"Your final score: {quiz.score} out of {len(question_bank)}")









