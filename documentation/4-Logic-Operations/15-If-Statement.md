# If Statement

Although an If statement is also an operation, due to its logical nature to it and its prevelence in other programming languages in some form, it was put into a seperate folder from the other operations. Of course this language is also very different from many others so the way an if statement gets executed is completely different from previous languages and its numerous quirks will be discussed in the sections below.

## If Statement Character

"ln.n ln.n" ? -> Take top element of "LetNum Stack" and element in "LetNum Stack" below it. Compare them

If the top element is greater than the element below it, turn right.

If the top element is less than the element below it, turn left.

If the top element is equal to the element below it, continue straight.

## Examples

With each example will come the state of both stacks at each turn using the following format along with the program output. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -  
Program Output:  

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.

Also note that when there will be a sample inpute it will be in parenthesis for the immediate turn and not after.

Also, there will be three tracks shown for each possibility in the if statement 

### Example 1

```
3   .....
    . h .
    . i .
    .>^ .
.............
.(,2.?41.;) .
.   .2  .   .
.   .3  .   .
.............
    .-  .
    ."  .
    .   .
    .....
    .1) .
    .;; .
    .)2 .
    .....
```

#### Track 1

Turn: 0  
LetNum Stack:     
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack: (1)   
Operation Stack:  
Program Output:  

Turn: 2  
LetNum Stack: 1, 2   
Operation Stack:  
Program Output:  

Turn: 3  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 4  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 5  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 6  
LetNum Stack: i   
Operation Stack:  
Program Output:

Turn: 7  
LetNum Stack: i, h   
Operation Stack:  
Program Output:  

Turn: 8  
LetNum Stack: i, h, 2   
Operation Stack:  
Program Output:  

Turn: 9  
LetNum Stack:    
Operation Stack:  
Program Output: hi  

Turn: 10  
LetNum Stack:    
Operation Stack:  
Program Output: hi  

#### Track 2

Turn: 0  
LetNum Stack:     
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack: (2)   
Operation Stack:  
Program Output:  

Turn: 2  
LetNum Stack: 2, 2   
Operation Stack:  
Program Output:  

Turn: 3  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 4  
LetNum Stack: 4   
Operation Stack:  
Program Output:  

Turn: 5  
LetNum Stack: 4, 1    
Operation Stack:  
Program Output:  

Turn: 6  
LetNum Stack:     
Operation Stack:  
Program Output: 4  

Turn: 7  
LetNum Stack:     
Operation Stack:  
Program Output: 4  

#### Track 3

Turn: 0  
LetNum Stack: (3)   
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack: 3, 2   
Operation Stack:  
Program Output:  

Turn: 2  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 3  
LetNum Stack: 2   
Operation Stack:  
Program Output:  

Turn: 4  
LetNum Stack: 2, 3   
Operation Stack:  
Program Output:  

Turn: 5  
LetNum Stack: 2, 3   
Operation Stack: -  
Program Output:  

Turn: 6  
LetNum Stack: 2, 3   
Operation Stack: -  
Program Output:  

Turn: 7  
LetNum Stack: 2, 3   
Operation Stack: -  
Program Output:  

Turn: 8  
LetNum Stack: 1, 1   
Operation Stack:   
Program Output:  

Turn: 9  
LetNum Stack:    
Operation Stack:   
Program Output: 1  

Turn: 10  
LetNum Stack:    
Operation Stack:   
Program Output: 1  

