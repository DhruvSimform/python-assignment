class NumberConversion:
    # Mapping of digits (0-9) to their corresponding English word representation
    __dict_number_to_word = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    # Mapping of English word representation to their corresponding digits (0-9)
    __dict_word_to_number = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    @classmethod
    def number_to_word(cls, number: int) -> str:
        """
        Converts a single-digit integer (0-9) into its corresponding English word.

        :param number: An integer between 0 and 9
        :return: The word representation of the number
        :raises ValueError: If the number is not in the valid range (0-9)
        """
        if 0 <= number <= 9:
            return cls.__dict_number_to_word[number]
        else:
            raise ValueError("Error: Not a valid number (must be between 0 and 9).")

    @classmethod    
    def word_to_number(cls,word: str) -> int:
        """
        Converts a english word into its corresponding single-digit integer (0-9)

        :param word: word representation of the number(0-9)
        :return: An interger between 0 and 9
        :raise ValueError: If English word is not valid for (0-9)
        """

        if word in cls.__dict_word_to_number:
            return cls.__dict_word_to_number[word]
        else:
            raise ValueError("Error: Not valid word reprenttation for digit 0-9")
    
    

