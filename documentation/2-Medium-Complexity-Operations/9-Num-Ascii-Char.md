# Converting Num To Ascii Char

This Operator solves a seemingly somewhat major design issue within Cube which is the lack of a "v" character. Although it has been stated earlier that "v" is really nothing more than a rip off "u" there has been functionality added for those insist on including "v". We will discuss the operator in the sections below.

This operator can also be used for any other letter and even symbols like "+"

## Conversion Character

"=" -> An equal sign is all that is needed to conver a number to an ascii value

Examples:

With each example will come the state of both stacks at each turn using the following format along with the program output. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -
Program Output:

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.

Example 1:

2  ....
   .v<.
   . ".
..........
.  .= .  .
.  .1".  .
..........
   .;*.
   .)8.
   ....
   . 9.
   .(^.
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
LetNum Stack: 9
Operation Stack:
Program Output:

Turn: 3  
LetNum Stack: 9, 8
Operation Stack:
Program Output:

Turn: 4  
LetNum Stack: 9, 8
Operation Stack: *
Program Output:

Turn: 5  
LetNum Stack: 9, 8
Operation Stack: *
Program Output:

Turn: 6  
LetNum Stack: 9, 8
Operation Stack: *
Program Output:

Turn: 7  
LetNum Stack: 72
Operation Stack:
Program Output:

Turn: 8  
LetNum Stack: 72
Operation Stack:
Program Output:

Turn: 9  
LetNum Stack: 72
Operation Stack:
Program Output:

Turn: 10  
LetNum Stack: 72
Operation Stack:
Program Output:

Turn: 10  
LetNum Stack: H
Operation Stack:
Program Output:

Turn: 11 
LetNum Stack: H, 1
Operation Stack:
Program Output:

Turn: 12  
LetNum Stack:
Operation Stack:
Program Output: H

Turn: 13  
LetNum Stack:
Operation Stack:
Program Output: H

