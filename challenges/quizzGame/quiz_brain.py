# TODO: checking answer
# TODO: check if end of quiz

class QuizBrain:
    """Logic of the game."""
    def __init__(self, question_list):
        """Initializing attributes"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if there is another question left to ask or False if not."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Asks for the user answer on the given question and calls the check_answer method."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1           # To start printing Q.1 instad of Q.0
        user_answer = input(f"\nQ.{self.question_number}: {current_question.ask} - (True / False): ").lower()
        self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks and prints whether the user's answer is correct or not
        and also prints out the user's score out of a possible question.
        """
        if user_answer == correct_answer.lower():
            print("That's correct!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"The correct answer was: '{correct_answer}'")
        print(f"Your current score is: {self.score}/{self.question_number}")
