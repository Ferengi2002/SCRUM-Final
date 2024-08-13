import time
import random
from model import MathModel
from view import MathView

class MathController:
    """Controlador que coordina las operaciones entre el modelo y la vista."""

    def __init__(self):
        self.view = MathView()

    def run(self):
        """Ejecuta el ciclo principal del programa."""
        level = self.view.get_level()
        model = MathModel(level)
        total_questions = self.view.get_total_questions()
        correct_count = 0

        start_time = time.time()

        for _ in range(total_questions):
            if level == 2:
                question, correct_answer = model.generate_addition_subtraction_question()
            elif level == 3:
                question, correct_answer = model.generate_multiplication_question()
            else:
                if random.choice(["multiplication", "division"]) == "multiplication":
                    question, correct_answer = model.generate_multiplication_question()
                else:
                    question, correct_answer = model.generate_division_question()
            
            user_answer = self.view.show_question(question)
            is_correct = user_answer == correct_answer
            self.view.show_result(is_correct, correct_answer)

            if is_correct:
                correct_count += 1

        end_time = time.time()
        total_time = end_time - start_time

        self.view.show_final_report(total_questions, correct_count, total_time)
