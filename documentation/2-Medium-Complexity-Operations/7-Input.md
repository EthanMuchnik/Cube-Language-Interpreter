# Input

Now that you know how to output data. How do you take in data that was not originally in the cube. Cube has the input operation for that which will be covered in the following sections below.

## Input Chracter

"," -> Input Operation

When the cursor goes over the input operation, it will prompt the user to enter input in the terminal. After the input is entered, the code after the character is run. The input goes into the "LetNum Stack" with the last character of input being at the top of the stack

## Examples

With each example will come the state of both stacks at each turn using the following format along with the program output. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -  
Program Output:  

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.

Also note that when there will be a sample inpute it will be in parenthesis for the immediate turn and not after.

### Example 1

```
2  ....
   .  .
   .  .
..........
.(,.v .  .
.  .- .  .
..........
   .").
   . ;.
   ....
   .1".
   .>^.
   ....
```

Turn: 0  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack: (2,3)  
Operation Stack:   
Program Output:  

Turn: 2  
LetNum Stack: 2,3  
Operation Stack:   
Program Output:  

Turn: 3  
LetNum Stack: 2,3  
Operation Stack: -   
Program Output:  

Turn: 4  
LetNum Stack: 2,3  
Operation Stack: -   
Program Output:  

Turn: 5  
LetNum Stack: 1, 1  
Operation Stack:    
Program Output:  

Turn: 6  
LetNum Stack: 1, 1  
Operation Stack:    
Program Output:  

Turn: 7  
LetNum Stack: 1, 1  
Operation Stack:    
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

