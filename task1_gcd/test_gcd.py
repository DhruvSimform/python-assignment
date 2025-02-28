import unittest
from gcd import NumberToWord, WordToNumber, Conversion, GCD, IterativeEuclideanGCD, RecursiveEuclideanGCD

class TestConversion(unittest.TestCase):

    def setUp(self):
        self.converter = Conversion()
    
    def test_number_to_word(self):
        self.converter.set_strategy(NumberToWord())
        self.assertEqual(self.converter.convert(123), "onetwothree")
        self.assertEqual(self.converter.convert(0), "zero")
        self.assertEqual(self.converter.convert(908), "ninezeroeight")
    
    def test_word_to_number(self):
        self.converter.set_strategy(WordToNumber())
        self.assertEqual(self.converter.convert("onetwothree"), 123)
        self.assertEqual(self.converter.convert("zero"), 0)
        self.assertEqual(self.converter.convert("ninezeroeight"), 908)
    
    def test_invalid_input_number_to_word(self):
        self.converter.set_strategy(NumberToWord())

        with self.assertRaises(TypeError):
                self.assertEqual(self.converter.convert("onetwo"))

    def test_invalid_input_word_to_number(self):
        self.converter.set_strategy(WordToNumber())

        with self.assertRaises(TypeError):
                self.assertEqual(self.converter.convert(123))

class TestGCDStrategies(unittest.TestCase):

    def setUp(self):
        self.gcd_calculator = GCD()

    def test_iterative_gcd(self):
        self.gcd_calculator.set_strategy(IterativeEuclideanGCD())
        self.assertEqual(self.gcd_calculator.find_gcd(48, 18), 6)
        self.assertEqual(self.gcd_calculator.find_gcd(101, 103), 1)
        self.assertEqual(self.gcd_calculator.find_gcd(56, 98), 14)
        
    def test_recursive_gcd(self):
        self.gcd_calculator.set_strategy(RecursiveEuclideanGCD())
        self.assertEqual(self.gcd_calculator.find_gcd(48, 18), 6)
        self.assertEqual(self.gcd_calculator.find_gcd(101, 103), 1)
        self.assertEqual(self.gcd_calculator.find_gcd(56, 98), 14)
        
    def test_gcd_invalid_input(self):
        self.gcd_calculator.set_strategy(RecursiveEuclideanGCD())
        with self.assertRaises(TypeError):
            self.gcd_calculator.find_gcd("ten", 5)
        with self.assertRaises(TypeError):
            self.gcd_calculator.find_gcd(10, "five")
        with self.assertRaises(TypeError):
            self.gcd_calculator.find_gcd("ten", "five")

if __name__ == "__main__":
    unittest.main()
