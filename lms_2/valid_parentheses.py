class GenrateParentheses: 
    """Class to generate all valid combinations of n pairs of parentheses."""   

    @staticmethod
    def _backtracking(n: int ,current_pair: str,result: list,count_of_open_parentheses: int, count_of_close_parentheses)->None:
        """Helper function to generate valid parentheses using backtracking."""

        if len(current_pair)== 2*n:
            result.append(current_pair)
            return 
        
        if count_of_open_parentheses<n:
            GenrateParentheses._backtracking(n, current_pair+"(", result ,count_of_open_parentheses+1 ,count_of_close_parentheses)

        if count_of_close_parentheses<count_of_open_parentheses:
            GenrateParentheses._backtracking(n, current_pair+")" ,result ,count_of_open_parentheses ,count_of_close_parentheses+1)

    @staticmethod
    def  genrate_parentheses(n:int)->list:
        """Generates all combinations of valid parentheses for given n."""

        # if n<0: # if n is negative number we can't genrate parentheses for that so display error
        #     raise ValueError("Error : Invalid Input , can't able to genrate parentheses for negative number")
        
        if n<=0 or n>8: # constraine error , input must be in given range
            raise ValueError("Error : Invalid Input , Input must be in given range (1-8)")
        
        # if n==0:
        #     return []
        
        result = [] 
        GenrateParentheses._backtracking(n,"",result,0,0)
        return result

    
if __name__=="__main__":

    try:
        n = int(input("Enter value of n between 1 to 8 : "))
        result = GenrateParentheses.genrate_parentheses (n) 
        print(result)
    except ValueError as e:
        print(e) 