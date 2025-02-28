import unittest
from group_anagram import (
    AnagramGrouping, 
    SortingAnagramStrategy, 
    FrequencyAnagramStrategy, 
)

class TestAnagramGrouping(unittest.TestCase):
    
    def setUp(self):
        self.anagram_grouping = AnagramGrouping()
        self.strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.expected_result = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    
    def test_sorting_strategy(self):
        self.anagram_grouping.add_strategy(SortingAnagramStrategy())
        result = self.anagram_grouping.group_anagrams(self.strs)
        self.assertCountEqual(result, self.expected_result)
    
    def test_frequency_strategy(self):
        self.anagram_grouping.add_strategy(FrequencyAnagramStrategy())
        result = self.anagram_grouping.group_anagrams(self.strs)
        self.assertCountEqual(result, self.expected_result)
    
    def test_invalid_strategy(self):
        with self.assertRaises(TypeError):
            self.anagram_grouping.add_strategy("invalid_strategy")
    
    def test_strategy_not_set(self):
        self.anagram_grouping.strategy = None
        with self.assertRaises(ValueError):
            self.anagram_grouping.group_anagrams(self.strs)
    
if __name__ == "__main__":
    unittest.main()
