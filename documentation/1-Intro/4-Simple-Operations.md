# Simple Operations

So now that we know how to load letters, numbers, and simple operations onto the stacks, how does this actually translate to simple operations? In order to unserstand how simple operations first we must go into another major feature of cube which is that operations are only completed when the cursor crosses a side. There is also another operation the condition being done which will be discussed in the (" Key Word) section below.

I will explain the steps involved in the following sections. The stacks will be represented in the fashion below where "2" is the top element of the "LetNum Stack" and "-" is the top element in the "Operation Stack". Think of "popped characters" object as another FILO stack though it simply exists for the easy visualization of the arithmatic operation that is about to happen

LetNum Stack: 3, 2  
Operation Stack: +, -

Popped Characters:

## Steps Involved
So lets use the example above and imagine that we just crossed a side. How do we modify the stacks? This is the original orientation of the stack

LetNum Stack: 3, 2  
Operation Stack: +, -

Popped Characters:

### Popping Neccesary Variables

The first step is to pop two characters from the "LetNum Stack" and one character from the "Operation Stack" as per all simple operations. With the top character from the "LetNum Stack" getting popped first followed by the top character from "Operation Stack" and lastly with the new top chracter of "LetNum Stack" getting popped.

LetNum Stack:  
Operation Stack: +

Popped Characters: 2, -, 3

### Completing the Operations

The next step is propably the most straightforward one. All that happens is that "2 - 3" is completed with the answer beign -1 in this scenario.

LetNum Stack:  
Operation Stack: +

Popped Characters: -1

### Push Onto "LetNum stack"

The last step is to simply push the remaining value to the "LetNum Stack" and delete the Popped Characters stack. And with that the operation is fully complete

LetNum Stack: -1  
Operation Stack: +

## " Key Character

If you went ahead and started trying to do simple operations from the instructions above you wouldn't actually get an output as there is another requirement to doing simple operations other than just crossing a side: the " Key Character. 

Essentially at all times the system is in two states: "Do the Operation" or "Don't do the Operation" with the latter being the default. The only way to change that state is by having a " Character in the cube interface. All this does is toggle the state. The main reason one would use this is if you cross a side and you don't want an operation to happen as you have to few elements in your respective stacks.

## Extra information

### Errors

Certain operation will return an error message such as dividing by 0 so abide by all existing math laws with your operations.

In addition, if the "LetNum Stack" contains letters instead of numbers, another error will be thrown and no sort of conversion from ascii to int will happen. So be careful when writing your code.

## Examples

With Each Example will come the state of both stacks at each turn using the following format. The "top" of the stack is the rightmost character as shown below.

Turn: 0  
LetNum Stack: 2, 1  
Operation Stack: +, -

In this example "b" would be at the top of the LetNum Stack and "-" would be at the top of the operation stack.


### Example 1
```
2  ....
   .  .
   . ".
..........
.  .  .+ .
. ).  .2 .
..........
   .(1.
   .  .
   ....
   .  .
   .  .
   ....
```

Turn: 0  
LetNum Stack:  
Operation Stack:

Turn: 1  
LetNum Stack: 1  
Operation Stack:

Turn: 2  
LetNum Stack: 1, 2  
Operation Stack:

Turn: 3  
LetNum Stack: 1, 2  
Operation Stack: +

Turn: 4  
LetNum Stack: 1, 2  
Operation Stack: +

Turn: 5  
LetNum Stack: 1, 2  
Operation Stack: +

Turn: 6  
LetNum Stack: 3  
Operation Stack:

Turn: 7  
LetNum Stack:  
Operation Stack:

