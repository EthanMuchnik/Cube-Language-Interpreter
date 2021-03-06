# Popping Stacks

The next operation is the pop operation which essentially just deletes a certain value in the selected stack. In the sections below that is the operation we will be explaining.  

## Popping Character

"ln.n" & -> Pop the nth value of the selected stack where n is the top value of the "LetNum Stack"

## Examples

With each example will come the state of both stacks at each turn using the following format along with the program output. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -  
Program Output:  

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.

### Example 1

```
2  ....
   . 2.
   . 1.
..........
.(2.1^.  .
.  .  .  .
..........
   .  .
   . ).
   ....
   . ;.
   . &.
   ....
```

Turn: 0  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack: 2  
Operation Stack:  
Program Output: 

Turn: 2  
LetNum Stack: 2, 1  
Operation Stack:  
Program Output: 

Turn: 3  
LetNum Stack: 2, 1  
Operation Stack:  
Program Output: 

Turn: 4  
LetNum Stack: 2, 1, 1  
Operation Stack:  
Program Output: 

Turn: 5  
LetNum Stack: 2, 1, 1, 2  
Operation Stack:  
Program Output: 

Turn: 6  
LetNum Stack: 2, 1  
Operation Stack:  
Program Output: 

Turn: 7  
LetNum Stack:   
Operation Stack:  
Program Output: 2

Turn: 8  
LetNum Stack:   
Operation Stack:  
Program Output: 2