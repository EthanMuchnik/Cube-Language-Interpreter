# Duplicate Operation

In cube there are other operations other than add, subtract etc... These operations function in the same way as the simple operations except for two major things.

1. You can choose which stack you modify via the "!" operator

2. These operations don't make their way into a stack. They just do their action and don't really on crossing sides

With that said, I will first introduce the simple duplicate operation in the sections below.

## Duplicate Character 

\# -> Duplicate the top character of the chosen stack

Duplicating means just adding that same character to the top of the stack

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
   .  .
   .  .
..........
.(1.#;.) .
.  .  .  .
..........
   .  .
   .  .
   ....
   .  .
   .  .
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
LetNum Stack: 1, 1   
Operation Stack:   
Program Output:  

Turn: 3  
LetNum Stack:    
Operation Stack:   
Program Output: 1  

Turn: 4  
LetNum Stack:    
Operation Stack:   
Program Output: 1  



