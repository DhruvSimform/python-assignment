class GenrateParentheses:    

    @staticmethod
    def __backtraking(n: int ,current_pair: str,result: list,count_of_open_parentheses: int, count_of_close_parentheses)->None:

        if len(current_pair)== 2*n:
            result.append(current_pair)
            return 
        
        if count_of_open_parentheses<n:
            GenrateParentheses.__backtraking(n, current_pair+"(", result ,count_of_open_parentheses+1 ,count_of_close_parentheses)

        if count_of_close_parentheses<count_of_open_parentheses:
            GenrateParentheses.__backtraking(n, current_pair+")" ,result ,count_of_open_parentheses ,count_of_close_parentheses+1)

    @staticmethod
    def  genrate_parentheses(n:int)->list:
        if n<0:
            raise ValueError("Error : Invalid Input , can't able to genrate parentheses for negative number")
        
        result = []
        GenrateParentheses.__backtraking(n,"",result,0,0)
        return result

    
if __name__=="__main__":
    n = int(input("Enter value of n: "))

    result = GenrateParentheses.genrate_parentheses (n) 

    print(result) 