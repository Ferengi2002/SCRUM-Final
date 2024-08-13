import unittest
from unittest.mock import patch
from code.view import MathView


class TestMathView(unittest.TestCase):

    @patch('builtins.input', return_value='2')
    def test_get_level(self, mock_input):
        level = MathView.get_level()
        self.assertEqual(level, 2)

    @patch('builtins.input', return_value='5')
    def test_get_total_questions(self, mock_input):
        total_questions = MathView.get_total_questions()
        self.assertEqual(total_questions, 5)

    @patch('builtins.input', return_value='15')
    def test_show_question(self, mock_input):
        user_answer = MathView.show_question("5 + 10")
        self.assertEqual(user_answer, 15)

if __name__ == '__main__':
    unittest.main()