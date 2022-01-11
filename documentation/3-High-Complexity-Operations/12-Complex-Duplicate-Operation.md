# More Complex Duplicate Operation 

Although the normal duplicate operation is sufficient for duplicating the top element in a stack, it does not provide any functionality for duplicating an element that is not at the top of a stack. That is precisely what the Complex Duplicate Operator is for.

## Complex Duplicate Characters 

"ln.n" $ -> Duplicate the nth value of the chosen stack where n is the top value of the "LetNum" stack

"ln.n" must be a number or else there will be an error

The chosen stack is chosen via the "!" operation

## Examples 

With each example will come the state of both stacks at each turn using the following format along with the program output. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -  
Program Output:  

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.

### Example 1

2  ....
   . 2.
   . 3.
..........
. (.1^.  .
.  .  .  .
..........
   .  .
   . ).
   ....
   . ;.
   . $.
   ....

Turn: 0  
LetNum Stack:  
Operation Stack:   
Program Output:  

Turn: 1  
LetNum Stack: 1  
Operation Stack:   
Program Output:  

Turn: 2  
LetNum Stack: 1  
Operation Stack:   
Program Output:  

Turn: 3  
LetNum Stack: 1, 3  
Operation Stack:   
Program Output:  

Turn: 4  
LetNum Stack: 1, 3, 2  
Operation Stack:   
Program Output:  

Turn: 5  
LetNum Stack: 1, 3, 1  
Operation Stack:   
Program Output:  

Turn: 6  
LetNum Stack: 1  
Operation Stack:   
Program Output: 3  

Turn: 7  
LetNum Stack:  
Operation Stack:   
Program Output: 3  




