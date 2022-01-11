# Swap Operations

This operation essentially takes to elements in the chosen stack and swaps their position. The specifics of this operation will be discussed below in the following sections.

## Swap Character

"ln.n ln.n" @ -> Swap the nth and mth number where n and m are the two two values in the "LetNum Stack"

This functionality will let you swap any two elements in any of the stacks as long as they are actually inside of the respective stacks.

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
   . 1.
   . 2.
..........
.(1.2^.  .
.  .  .  .
..........
   .  .
   . ).
   ....
   . ;.
   . @.
   ....
```

Turn: 0  
LetNum Stack:   
Operation Stack:  
Program Output:  

Turn: 1  
LetNum Stack: 1  
Operation Stack:  
Program Output: 

Turn: 2  
LetNum Stack: 1, 2  
Operation Stack:  
Program Output: 

Turn: 3  
LetNum Stack: 1, 2  
Operation Stack:  
Program Output: 

Turn: 4  
LetNum Stack: 1, 2, 2  
Operation Stack:  
Program Output: 

Turn: 5  
LetNum Stack: 1, 2, 2, 1    
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


