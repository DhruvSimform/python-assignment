import unittest
from valid_parentheses import GenrateParentheses

class TestGenrateParentheses(unittest.TestCase):

    def test_generate_valid_parentheses(self):
        
        self.assertEqual(GenrateParentheses.genrate_parentheses(0), [])
        self.assertEqual(GenrateParentheses.genrate_parentheses(1), ["()"])
        self.assertEqual(GenrateParentheses.genrate_parentheses(2), ["(())", "()()"])
        self.assertEqual(GenrateParentheses.genrate_parentheses(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
    
    def test_generate_invalid_input(self):
        with self.assertRaises(ValueError):
            GenrateParentheses.genrate_parentheses(-1)

if __name__ == "__main__":
    unittest.main()