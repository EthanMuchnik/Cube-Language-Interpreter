# Changing Direction

```
2  ....
   .  .
   .  .
..........
.  .  .) .
.  .( .^ .
..........
   . .
   .  .
   ....
   .  .
   .  .
   ....
```

## Direction Changing Characters

There are four characters responsible for changing direction
- ">" -> Turn Right
- "<" -> Turn Left
- "^" -> Turn Up
- "v" -> Turn Down

## What Happens When Characters are hit

Whenever the cursor hits one of these characters its direction automatically changed. So next turn when it moves it will go one step in its new direction. Keep in mind that although the directions are called Up, Down, Right, and Left it's not actually directly indicative of the new direcion as direction is also influenced by side. For example the cursor would be moving right until it crosses over into the right side at which two operations would happen. First, the direction would switch to down as from that side's perspective, right is down. Then the Up character would be read and the direction chages to right or heading towards the end parenthesis.

## Miscellanious

There is one major thig that must be covered which is that "Turn Down" is represented by a "v". This was intentional by the Cube Language Team as we believed that lower case v's were far too overatted as a letter and were essentially just a cheap knockoff of "u". In later sections you will find out how the language system works in cube and how one can overcome the minor inconvenience of v's not existing.