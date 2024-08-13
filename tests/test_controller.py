import unittest
from unittest.mock import patch
from code.controller import MathController

class TestMathController(unittest.TestCase):

    @patch('code.view.MathView.get_level', return_value=2)
    @patch('code.view.MathView.get_total_questions', return_value=3)
    @patch('code.view.MathView.show_question', return_value=5)
    @patch('code.view.MathView.show_result')
    @patch('code.view.MathView.show_final_report')
    def test_run(self, mock_show_final_report, mock_show_result, mock_show_question, mock_get_total_questions, mock_get_level):
        controller = MathController()
        controller.run()
        mock_show_final_report.assert_called_once()

if __name__ == '__main__':
    unittest.main()