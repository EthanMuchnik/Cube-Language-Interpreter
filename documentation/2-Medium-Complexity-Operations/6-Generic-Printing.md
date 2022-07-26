# Printing

With the understanding of how to input data into the stacks one may wonder, how would you output this data. This page will show you the operation in charge of printing and the quirks behind using it.

## Printing Character 

First let's go over the format I will present the Character in below. Essentially what the following format means is that the character is "#" but it needs ln  -> LetNum stack and takes a n -> number from it. Without this prerequisite, an error will be thrown. 

"ln.n #" -> Take the top element (n) from "LetNum Stack" and print the top (n) next elements from "LetNum Stack"

## More Detailed Clarification

What this means is that these top values will get printed to the console and will get deleted from the stacks themselves. There is a new line after each print operation is executed

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
   .);.
..........
. (.v .2 .
.  .b .1 .
..........
   .>a.
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
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 2  
LetNum Stack: b  
Operation Stack:  
Program Output:  

Turn: 3  
LetNum Stack:  
Operation Stack:  
Program Output:  

Turn: 4  
LetNum Stack: b, a  
Operation Stack:  
Program Output:  

Turn: 5  
LetNum Stack: b, a  
Operation Stack:  
Program Output:  

Turn: 6  
LetNum Stack: b, a, 1  
Operation Stack:  
Program Output:  

Turn: 7  
LetNum Stack: b, a, 1, 2  
Operation Stack:  
Program Output: a1  

Turn: 8  
LetNum Stack: b  
Operation Stack:  
Program Output: a1  

Turn: 9  
LetNum Stack:  
Operation Stack:  
Program Output: a1  


