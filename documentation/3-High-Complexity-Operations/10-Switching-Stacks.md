# Switching Stacks

By now you should know that cube has two stacks: "The LetNum Stack" and the "Operation Stack". You may have also noticed that all operations until now each operation affects each stack in a certain way. For example, simple operations like addition take the top two characters in the "LetNum Stack" and the top value in the "Operation Stack" and then put back one character into the "LetNum stack". Another example is how the Generic Printing Operation always takes the top characters from the "LetNum Stack" and never from the "Operation Stack".

However, in the future, we will have commands that will modify a certain stack that you select. In Cube, we use a variable to keep track of which stack should be modified by these commands and it is toggled by the character we will go over below.

## Stack Switch Character

"!" -> Switch stack: 

It is important to note that the original stack selected is the "LetNum Stack". 

## Why No Examples?

Examples will not be gone over in this section as switching stacks doesn't change anything unless you use one of the operations we will discuss in the future.