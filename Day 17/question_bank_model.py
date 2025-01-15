from question_model import Question

class QuestionBank:

    def __init__(self, question_data):
        self.question_data = question_data
        self.question_bank = []

        # self.create_question_bank()

    def create_question_bank(self):
        for item in self.question_data:
            new_question = Question(item["question"], item["correct_answer"])
            self.question_bank.append(new_question)
        return self.question_bank
