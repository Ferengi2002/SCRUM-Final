import random

class MathModel:
    """Modelo que genera preguntas de matemáticas según el nivel educativo."""

    def __init__(self, level):
        self.level = level

    def generate_addition_subtraction_question(self):
        """Genera una pregunta de suma o resta."""
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-"])
        
        if operation == "+":
            correct_answer = num1 + num2
            return f"{num1} + {num2}", correct_answer
        else:
            # Asegurar que el resultado no sea negativo
            if num1 < num2:
                num1, num2 = num2, num1
            correct_answer = num1 - num2
            return f"{num1} - {num2}", correct_answer

    def generate_multiplication_question(self):
        """Genera una pregunta de multiplicación."""
        if self.level == 3:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        else:
            num1 = random.randint(10, 99)
            num2 = random.randint(1, 9)
        
        correct_answer = num1 * num2
        return f"{num1} x {num2}", correct_answer

    def generate_division_question(self):
        """Genera una pregunta de división exacta."""
        divisor = random.randint(1, 9)
        dividend = divisor * random.randint(1, 9)
        correct_answer = dividend // divisor
        return f"{dividend} ÷ {divisor}", correct_answer
