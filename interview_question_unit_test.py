import unittest
from interview_question import solution

class TestInterviewQuestion(unittest.TestCase):

    def test_basic(self):
        input = [['one','two',['three', ['four', ['five', 'six', ['seven', ['eight']]]]]],'nine']
        output = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.assertEqual(solution(input), output)

    def test_empty(self):
        input = []
        output = []
        self.assertEqual(solution(input), output)

    def test_finished(self):
        input = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        output = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        self.assertEqual(solution(input), output)

    def test_one(self):
        input = ['one']
        output = ['one']
        self.assertEqual(solution(input), output)


if __name__ == '__main__':
    unittest.main()
