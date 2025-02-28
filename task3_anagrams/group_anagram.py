from abc import ABC, abstractmethod

# Strategy Interface
class AnagramGroupingStrategy(ABC):
    """Abstract base class for different anagram grouping strategies."""
    
    @staticmethod
    @abstractmethod
    def group_anagrams(strs: list):
        pass

class SortingAnagramStrategy(AnagramGroupingStrategy):
    """Groups anagrams by sorting each word and using it as a key."""

    @staticmethod
    def group_anagrams(strs: list):
        
        hash_map = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))  
            hash_map.setdefault(sorted_str, []).append(str)
        
        return [group_list for group_list in hash_map.values()]

class FrequencyAnagramStrategy(AnagramGroupingStrategy):
    """Groups anagrams by counting character occurrences and using a tuple as a key."""

    @staticmethod
    def group_anagrams(strs: list):
        
        hash_map = {}

        for str in strs:
            frequency_count = [0]*26

            for char in str:
                frequency_count[ord(char)-ord('a')] += 1

            hash_map.setdefault(tuple(frequency_count),[]).append(str)
        return [group_list for group_list in hash_map.values()]
    
class AnagramGrouping:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.strategy = None
        return cls._instance
    
    def add_strategy(self, strategy: AnagramGroupingStrategy):
        if not isinstance(strategy, AnagramGroupingStrategy):
            raise TypeError("Error: Invalid strategy type")
        self.strategy = strategy  # Correctly setting the strategy instance

    

    def group_anagrams(self,strs : list):
        if self.strategy is None:
            raise ValueError("error : Strategy type is not set")
        return self.strategy.group_anagrams(strs)
    
if __name__=="__main__":

    # strs = list(input("strs : ").split())
    strs = ["eat","tea","tan","ate","nat","bat"]

    anagram=AnagramGrouping()
    anagram.add_strategy(FrequencyAnagramStrategy())

    print(anagram.group_anagrams(strs))



