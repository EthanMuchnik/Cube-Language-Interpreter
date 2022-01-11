# Multiple stacks

The following section covers one of the most important parts of Cube that make Cube the language it is: its two stacks. I will first give the high level explanation of the two stacks which may be a bit confusing but I promise it will make more sense as I get to the examples. 

## The Two stacks

In Cube there are two stacks(First in Last Out) from which certain elements, represented by a character in the cube frame, go. It is important to note that not all the characters go into one of these stacks. For instance, all of the ones we covered so far never enter the stack system.

However, it is a different story for characters like letters, numbers, and simple operations like "+", "-", "*","/", "%". If found in the confines of the cube borders by the cursor, these characters will go into one of the following respective stacks.

### LetNum Stack

Lets first go over the first stack which we will dub the "LetNum Stack". As the name suggests, it takes in any numbers or letters. Since the cursor can only point to one character at a time, words that are more than one letter or numbers greater than 9,or negative numbers can not be directly inputted into the stack. It is important to note that "v" is not able to be inputed as the interpreter only interprets "v" as the "Going Down" character.

It is also important to note that a space can be added by writing "~".

### Operation Stack

The second stack is the "Operation Stack" which only picks up "+", "-", "*","/", "%". It is important to note that what determines which stack will pick up either character is determined by what the character actually is. The "LetNum Stack" should never pick up "*" and the "Operation Stack" should never pick up "%". 

## Extra Information

As mentioned before, these are FILO stacks which means that in essence the things inputted to the stack pile up on each other and only the top character can be taken out. We will go over the ways you can take out characters in later files.

It is also important to note that the contents of the stacks get deleted when the cursor is over ")" and the program concludes. There is nothing ouputted.

## Examples

With each example will come the state of both stacks at each turn using the following format. The "top" of the stack is the rightmost character as shown below.

Turn: 0
LetNum Stack: a, b
Operation Stack: +, -

In this example "b" would be at the top of the "LetNum Stack" and "-" would be at the top of the "Operation Stack".

### Example 1

```
2  ....
   .  .
   .  .
..........
.  .  .) .
.  .  .+ .
..........
   .(a.
   .  .
   ....
   .  .
   .  .
   ....
```

Turn 0:  
LetNum Stack:  
Operation Stack:

Turn 1:  
LetNum Stack: a  
Operation Stack:

Turn 2:  
LetNum Stack: a  
Operation Stack:

Turn 3:  
LetNum Stack: a  
Operation Stack: +

Turn 4:  
LetNum Stack:   
Operation Stack:

### Example 2

```
2  ....
   .  .
   .*).
..........
. ^.-3.< .
.  .  .p .
..........
   .(u.
   .  .
   ....
   .  .
   .  .
   ....
```

Turn 0:  
LetNum Stack:  
Operation Stack:

Turn 1:  
LetNum Stack: u  
Operation Stack:

Turn 2:  
LetNum Stack: u, p  
Operation Stack:

Turn 3:  
LetNum Stack: u, p  
Operation Stack:

Turn 4:  
LetNum Stack: u, p, 3  
Operation Stack:

Turn 5:  
LetNum Stack: u, p, 3  
Operation Stack: -

Turn 6:  
LetNum Stack: u, p, 3  
Operation Stack: -

Turn 7:  
LetNum Stack: u, p, 3  
Operation Stack: -, *

Turn 8:  
LetNum Stack:  
Operation Stack:  

