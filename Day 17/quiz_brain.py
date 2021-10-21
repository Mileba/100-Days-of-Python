#
class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} Answer (True/False):").lower()
        # print(f"The Correct answer is {current_question.answer}")
        self.question_number += 1
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, answer):
        if user_answer == answer.lower():
            self.score += 1
            print(f"You got it correctly {self.score}/{self.question_number }")
        else:
            print(f"You got it wrongly {self.score}/{self.question_number}")
        print(f"The correct answer is : {answer}")
        print("\n")

