from abc import ABC, abstractmethod

#interface for ConversionStrategy
class ConversionStrategy(ABC):
    """Abstract base class for conversion strategies."""
    @abstractmethod
    def convert(self, value):
        pass

class NumberToWord(ConversionStrategy):
    """Converts numbers to words."""

    # Mapping of digits (0-9) to their corresponding English word representation
    __dict_num_to_word = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    @classmethod
    def convert(cls, number: int) -> str:
        """Converts an integer to its word representation."""
        if not isinstance(number, int) or number < 0:      # validation of given input is in integer
            raise TypeError("Error: Input must be a non-negative integer.")
        
        def parse(number_in_words: str, number :str, index :int, length: int):
            """Recursively converts digits to words."""
            if index >= length:     #base condition for when we parse all digit from number
                return number_in_words
            
            digit = int(number[index])
            
            return parse(number_in_words + cls.__dict_num_to_word[digit], number, index + 1, length)  # parse next digit
        
        return parse("", str(number), 0, len(str(number))) # parse all digit of number recursively

class WordToNumber(ConversionStrategy):
    """Converts words to numbers."""

    # Mapping of English word representation to their corresponding digits (0-9)
    __dict_word_to_number = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    @classmethod
    def convert(cls, number_in_words: str) -> int:
        """Converts a word representation of a number to an integer."""

        if not isinstance(number_in_words, str):    #validation of given input is in string
            raise TypeError("Error: Input must be a string.")
        
        def parse(ans, current_str, index, length):
            """Recursively parses words into a number."""
            
            if index >= length:     #base condition for when we parse number_int_words string
                if current_str:     #validation for if user has enter invalid word representation of words       
                    raise ValueError("Error: Invalid word representation.")
                return ans
            
            current_str += number_in_words[index] #append curent index char to current string

            if current_str in cls.__dict_word_to_number: #if current string is valid word representation convert it into integer and reset current string
                return parse(ans + str(cls.__dict_word_to_number[current_str]), "", index + 1, length)
            
            return parse(ans, current_str, index + 1, length) # if current string is not valid representation then increment index
        
        return int(parse("", "", 0, len(number_in_words))) # start parsing all words

class Conversion:
    """Manages conversion strategies (Singleton)."""
    
    __instance = None # for singleton pattern

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.strategy = None

        return cls.__instance


    def set_strategy(self, strategy: ConversionStrategy):
        """Sets the conversion strategy."""
        if not isinstance(strategy, ConversionStrategy): #validate only valid strategy is used
            raise TypeError("Error: Invalid strategy.")
        self.strategy = strategy


    def convert(self, value):
        """Converts a value using the chosen strategy."""
        if not self.strategy: #validate if not strategy is set
            raise ValueError("Error: No strategy set.")
        return self.strategy.convert(value)

class GCDStrategy(ABC):
    """Abstract base class for GCD calculation."""
    @abstractmethod
    def find_gcd(self, num1: int, num2: int) -> int:
        pass


class IterativeEuclideanGCD(GCDStrategy):
    """Finds GCD using iterative Euclidean algorithm."""
    @staticmethod
    def find_gcd(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = num2, num1 % num2
        return num1


class RecursiveEuclideanGCD(GCDStrategy):
    """Finds GCD using recursive Euclidean algorithm."""
    @staticmethod
    def find_gcd(num1: int, num2: int) -> int:
        return num1 if num2 == 0 else RecursiveEuclideanGCD.find_gcd(num2, num1 % num2)

class GCD:
    """Manages GCD strategies (Singleton)."""
    
    __instance = None # for singleton pattern

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.strategy = None

        return cls.__instance
    

    def set_strategy(self, strategy: GCDStrategy):
        """Sets the GCD strategy."""

        if not isinstance(strategy, GCDStrategy): #validate only valid strategy is used
            raise TypeError("Error: Invalid GCD strategy.")
        
        self.strategy = strategy


    def find_gcd(self, num1: int, num2: int) -> int:
        """Finds GCD using the chosen strategy."""

        if not isinstance(num1, int) or not isinstance(num2, int): 
            raise TypeError("Error: Both inputs must be integers.")
        
        if not self.strategy: #validate if not strategy is set
            raise ValueError("Error: No strategy set.")
        
        if num1 < num2:
            num1, num2 = num2, num1

        return self.strategy.find_gcd(num1, num2)
    
if __name__ == "__main__":
    try:
        number1 = input("Number 1: ").strip().lower()
        number2 = input("Number 2: ").strip().lower()

        convertor = Conversion()
        convertor.set_strategy(WordToNumber())
        num1 = convertor.convert(number1)
        num2 = convertor.convert(number2)

        gcd_calculator = GCD()
        gcd_calculator.set_strategy(RecursiveEuclideanGCD())
        ans = gcd_calculator.find_gcd(num1, num2)

        convertor.set_strategy(NumberToWord())
        ans = convertor.convert(ans)

        print(f"Output: {ans}")
    except (TypeError, ValueError) as e:
        print(e)