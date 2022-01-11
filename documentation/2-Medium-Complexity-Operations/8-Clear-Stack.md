# Clearing The Stacks Stack

This operation is for deleting the contents of both stacks mid-program. The operation character will be discussed in the sections below.

## Clearing Stack Character

"`" -> Clears both "LetNum" and "Operation Stack"

When the cursor is on this character, both the "LetNum" and "Operation Stack" get cleared immediately

## Examples

With each example will come the state of both stacks at each turn using the following format along with the program output. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -  
Program Output:  

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.

### Example 1

2  ....
   .v<.
   .`1.
..........
. (. ^.  .
.  .2 .  .
..........
   .1 .
   .; .
   ....
   .) .
   .  .
   ....

Turn: 0  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 2  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 3  
LetNum Stack: 1  
Operation Stack:  
Program Output:  

Turn: 4  
LetNum Stack: 1  
Operation Stack:  
Program Output:  

Turn: 5  
LetNum Stack: 1  
Operation Stack:  
Program Output:  

Turn: 6  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 7  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 8  
LetNum Stack: 2  
Operation Stack:  
Program Output:  

Turn: 9  
LetNum Stack: 2, 1  
Operation Stack:  
Program Output:  

Turn: 10  
LetNum Stack:   
Operation Stack:   
Program Output: 2  

Turn: 11  
LetNum Stack:   
Operation Stack:   
Program Output: 2  