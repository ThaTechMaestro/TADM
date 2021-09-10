'''

Problem -- Variation of Valid Parenthesis Problem on Leetcode


Questions
How is it related to a compiler
Why should I use a stack to solve this

What does the parentheses in a string are balanced and properly nested?
    Think about it in terms of statically typed languages which makes use
    of curly brackets, the curly brackets have to be balanced 
    and properly nested for the compiler to succesfully perform its function.


---------------------------
Solving the problem

    In solving this my minds compares the first and last parenthesis
    Checks if it matches:
        If it does, it goes inward and checks the next two symbols
    If it does not:
        It returns a statement saying the string is not balanced or valid

    A first Edge case is:
        When you have a null input

    Another naive solution, which is not totally correct I thought off is:
        If the number of parenthesis is even: It is valid
        If the number of parenthesis is odd: It is not valid

        But this input defies it --> )()(

    
    A misinterpretation was thiking the parenthesis has to be totally
    nested like statically typed languages but no, it should just be balanced too
    The example inputs verifies this.

    Two key statements here are "properly nested" and "completely balanced"

    In balancing the parenthesis either in a nested fashion or new parenthesis
        A key thing to look out for is the most recent opening parenthesis, 
        which needs to be closed or balanced

    
    What are the methods present in a stack
        What is pop or peek






    ---------------------------------------
    Time complexities

    Space complexities
    Worst case for valid string:
        O(n/2) -- storing half of the parentheses on the stack  = O(n)
    
    Worst case for invalid string:
        O(n) -- storing all the parentheses on the stack  = O(n)
    

--------------------
Continue From:
    https://www.youtube.com/watch?v=CCyEXcNamC4
    Timestamp: 5:00
    Watch it again and this time implement the solution
    


'''

print("()")