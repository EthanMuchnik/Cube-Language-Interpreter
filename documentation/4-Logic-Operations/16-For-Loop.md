# For-Loop 

The For-Loop is the last logical operation in this language. It works similarly to for-loops in other languages with its own unique twists. The character and the general logic will be gone over below.

## For Loop Character:

"ln.n" : -> n represents the amount of iterations of the for-loops which is the top value of the "LetNum Stack". Turn left if in for-loop. Otherwise, go straight

Cube has a unique take on for-loops. In order to get in a for-loop you should first bump into a colon. That program will ID that colon at its location. So until you've gone through the colon n times you will turn left. When you have gone through it the n times, the next time you will simply go forward.

Cube is unique as the way to "break" out of the for-loop is to simply make it so you never return to the : character. However if you go to another ":" in the middle of that for-loop the new ":" will be treated as a nested for-loop. 

This may seem a bit complex though an example below should help out a bit.

## Examples

### Example 1

```
5     .......
      .     .
      .     .
      .     .
      .     .
      .     .
...................
.(v> >.    v.     .
. 1   . v <".     .
.    ". + ^<.     .
. 4  ^.2:   .     .
. >^  . "   .     .
...................
      .     .
      . 1   .
      . ;   .
      . )   .
      .     .
      .......
      .     .
      .     .
      .     .
      .     .
      .     .
      .......
```
The output Here is 9.

As an exercise try to see how the answer was obtained
