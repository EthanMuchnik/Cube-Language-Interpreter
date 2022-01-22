# Cube
Cube is an esoteric programming language made to emulate a 3D cube via a 2D text editor interface. The only files that can run Cube code end with extensions ".cube" and ".dewy".

## Example
The following text file represents a simple example of Cube code:

```
2  ....
   .  .
   .);.
..........
.( .v .1 .
.  .  .1 .
..........
   .>a.
   .  .
   ....
   .  .
   .  .
   ....   
```

## Features

- 2D representation of 3D coding interface.
- Code intuitively represents an unfolded cube
- Input/Output Functionality
- Is primarily run from two Stacks(Operation Stack and Char Stack)
- Special Functionality When Crossing Between Sides(Marked By Periods)
- One of the few languages that can be run from more than one extension(.cube and .dewy)
- Exclusively Coded in Python Meaning Source Code is Relatively Easy To Understand

## Building

Requirements:
- python version (>=3.0)

Supported Systems:
- Windows 10/11
- GNU/Linux(Tested on Ubuntu 20.04)

Install Cube and Run Cube File

```
$ git clone https://github.com/EthanMuchnik/Cube-Language-Interpreter.git
$ cd Cube-Language-Interpreter/src
$ python3 CodeRunner.py
```
Then enter your .cube or .dewy file name when prompted

## Documentation:

Check out the documentation folder going through each of the files in order.

## Credits

Ethan Muchnik - Implemented All Interpreter Code and Wrote Original Language Specification

Cynthia Wang - Wrote Original Language Specification

Almutwakel Hassan - Wrote Original Language Specification

Specification was developed in the Esoteric Programming Class in CMU.
