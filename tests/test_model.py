import unittest
from codigo.model import MathModel

class TestMathModel(unittest.TestCase):

    def test_generate_addition_subtraction_question(self):
        model = MathModel(level=2)
        question, correct_answer = model.generate_addition_subtraction_question()

        self.assertTrue('+' in question or '-' in question)
        self.assertIsInstance(correct_answer, int)

    def test_generate_multiplication_question(self):
        model = MathModel(level=3)
        question, correct_answer = model.generate_multiplication_question()
        self.assertIn('x', question)
        self.assertIsInstance(correct_answer, int)

    def test_generate_division_question(self):
        model = MathModel(level=4)
        question, correct_answer = model.generate_division_question()
        self.assertIn('÷', question)
        self.assertIsInstance(correct_answer, int)

if __name__ == '__main__':
    unittest.main()