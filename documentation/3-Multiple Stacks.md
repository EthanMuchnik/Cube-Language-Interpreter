# Multiple stacks

The following section covers one of the most important parts of cube that make cube the language it is: its two stacks. I will first give the high level explanation of the two stacks which may be a bit confusing but I promise it will make more sense as I get to the examples. 

## The Two stacks

In cube there are two stacks(First in Last Out) from which certain inputs, represented by a character in the cube frame, go. It is important to note that not all the characters go into one of these stacks. For instance, all of the ones we covered so far never enter the stack system.

However, it is a different story for characters like letters, numbers, and simple operations like "+", "-", "*","/", "%". If found in the confines of the cube borders by the cursor these characters will go into one of the respective stacks.

### LetNum Stack

Lets first go over the first stack which we will dub the "LetNum Stack". As the name suggests, it takes in any numbers or letters. Since the cursor can only point to one character at a time, words that are more than one letter or numbers greater than 9 can not be directly inputted into the stack. It is important to note that "v" is not able to be inputed as the interpretaor only interprets "v" as the "Going Down" character.

### Operation Stacks

