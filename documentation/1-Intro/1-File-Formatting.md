# General Overview

Below I will explain the purpose of Cube and the General Features at Hand. Throughout this document I will explain what each of the individual characters mean in the context of this language

## What is Cube?

Cube is an Esoteric Programming Language that simulates a 3D coding experience via a 2D text file. The only files types that can host Cube code are .cube and .dewy files.

## Breakdown of Typical Cube File

### General Outline

```
6      ........
       .      .
       .      .
       . Back .
       .      .
       .      .
...................... 
.      .      .      . 
.      .      .      . 
. Left .  Top .Right . 
.      .      .      . 
.      .      .      . 
...................... 
       .      .
       .      .
       .Front .
       .      .
       .      .
       ........
       .      .
       .      .
       .Bottom.
       .      .
       .      .
       ........
```

Every Single cube File contains 6 squares that are a certain size by a certain size arranged in this way with periods seperating them. The size of these squares is dependent on the number in the very top left of the proram that most be between 1 and 9 inclusive. The words in each of the boxes are not actually present in cube code and are simply comments to illustrate which side is which.

### The Cursor

```
2  ....
   .  .
   .  .
..........
.  .  .) .
.  .  .  .
..........
   .( .
   .  .
   ....
   .  .
   .  .
   ....
```

The above image will illustrate to very important concepts in cube. THe code is format around and invisible cursor that is always at a certain point in this cube structure. It always starts at the "(" and the program ends when the ")" is reached. Although the end can be approached from any direction. The program always begins with a "direction" heading out of the "(" which is right. When the cursor spawns at the "(" it is turns 0. So every single turn the program moves one space in the direction it is assigned and thus one move is completed. Every move the cursor analyzes the square that its on to see if this is where it should terminate or if there is another special character that gives it insructions. It is also important to note that the directions are always relative to a direct view of that specific side which means that going "right" on the right side is actually going up for example.

This now brings us to the second important takeway which is exactly how sides between the cube are traversed. The code above is a completely legal progam because of how the folding of cubes actually happens. If you are not familiar with how cubes fold watch the following video. [Cube Folding](https://www.youtube.com/watch?v=QCufFrithLU). Assuming you understand how the cube folds together, there are no jumps in Cube through empty space and every move goes to an adjacent position.

Of course cube is so much more than just going from one parenthesis to the next using geometry. There is functionality to change direction, pick up characters and operations, and even enter for loops. This is all possible by additional characters which we will go into one group at a time. Read the following documents for he relevant documentation.
