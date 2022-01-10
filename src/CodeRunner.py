import enum
import FormatChecker
import FileReader

#Position For Cursor
class Position:
    def __init__(self):
        self.xCord = -1
        self.yCord = -1

# Class To Keep Track of For Loops
class ForLoop:

    # xCord -> int to keep track of x Coordinate for loop symbol ":"
    # yCord -> int to keep track of y Coordinate for loop symbol ":"
    # iteration -> int to keep track of iterations in for loop
    def __init__(self,xCord,yCord,iteration):
        self.xCord = xCord
        self.yCord = yCord
        self.iteration = iteration

#Keeps Track of Code Matrix and Characters On It
class Runner:

    #inMat -> 2D list list of input text file
    #size -> size of each square of the cube
    def __init__(self,inMat, size):
        self.inMat = inMat
        self.modMat = [] #Modified Matrix for all future operations/code
        self.size = size

        self.aStack = [] #Stack containing all numbers/letters
        self.opStack = [] #Stack containing all operations (+,-,*,/,%)

        self.pos = Position() #Keeps track of the position of the cursor
        self.aStackSelect = True #When True, aStack is selected. False means opStack is selected
        self.doOps = False #Determines if the top operation gets applied when border between sides is crossed

        self.forLoops = [] #Keeps track of all forloops

    #Function To Initialize modMat from inMat
    def initModMat(self):
        for z in range(6):
            self.modMat.append([])
            for y in range(self.size):
                self.modMat[z].append([])
                for x in range(self.size):
                    self.modMat[z][y].append("")

        for row in range(self.size):
            for col in range(self.size):
                self.modMat[0][row][col] = self.inMat[row+1][col+(self.size + 1)+1]

        for row in range(self.size):
            for col in range(self.size):
                self.modMat[1][row][col] = self.inMat[row+(self.size+1)+1][col+1]

        for row in range(self.size):
            for col in range(self.size):
                self.modMat[2][row][col] = self.inMat[row+(self.size+1)+1][col+(self.size+1)+1]
        
        for row in range(self.size):

            for col in range(self.size):
                self.modMat[3][row][col] = self.inMat[row+(self.size+1)+1][col+(self.size+1)*2+1]
    
        for row in range(self.size):
            for col in range(self.size):
                self.modMat[4][row][col] = self.inMat[row+(self.size+1)*2+1][col+(self.size+1)+1]

        for row in range(self.size):
            for col in range(self.size):
                self.modMat[5][row][col] = self.inMat[row+(self.size+1)*3+1][col+(self.size+1)+1]
    
    #Function that starts the code runner
    def startRunner(self):
        self.runnerSetupSide()
        self.runnerSetupDirection()
        self.moveLoop()

    #Function that finds finds location of ( and corresponding cords and side
    def runnerSetupSide(self):
        self.initModMat()

        for side in range(6):
            for row in range(self.size):
                for col in range(self.size):
                    if self.modMat[side][row][col] == '(':
                        self.side = self.Sides(side)
                        self.pos.xCord = col
                        self.pos.yCord = row
                        return

    #Function that finds initial directions

    def runnerSetupDirection(self):
        if self.side == self.Sides.back:
            self.direction = self.Directions.left
        else:
            self.direction = self.Directions.right
        


    #Function responsible for doing cursor moves and
    #interpreting the chars that cursor goes on.
    #It only finishes once toContinue becomes false
    def moveLoop(self):
        toContinue = True

        while toContinue:
            self.nextPos()
            toContinue = self.interpChar()

        print("Program has ended")

    #Function Determines the next position given Direction and current position.
    #Also determines if it is necessary to switch sides
    def nextPos(self):
        if self.direction == self.Directions.down:
            if self.inBounds(self.pos.yCord+1):
                self.pos.yCord+=1
            else:
                self.switchSides()
        elif self.direction == self.Directions.left:
            if self.inBounds(int(self.pos.xCord-1)):
                self.pos.xCord-=1
            else:
                self.switchSides()
        elif self.direction == self.Directions.right:
            if self.inBounds(int(self.pos.xCord+1)):
                self.pos.xCord+=1
            else:
                self.switchSides()
        elif self.direction == self.Directions.up:
            if self.inBounds(int(self.pos.yCord-1)):
                self.pos.yCord-=1
            else:
                self.switchSides()

    #Determines if the new position is in bounds of the side that the previous position was on
    # cord -> int representing either current yCord or xCord
    def inBounds(self, cord):
        if cord>=self.size or cord < 0:
            return False
        else:
            return True

    #Function responsible for switching sides and changing relevant variables
    def switchSides(self):
        if self.side == self.Sides.bottom:
            if self.direction == self.Directions.up:
                self.direction = self.Directions.up
                self.side = self.Sides.front
                self.pos.yCord = self.size -1

            elif self.direction == self.Directions.left:
                self.direction = self.Directions.right
                self.pos.yCord = self.size -1 - self.pos.yCord
                self.side = self.Sides.left

            elif self.direction == self.Directions.right:
                self.direction = self.Directions.left
                self.pos.yCord = self.size -1 - self.pos.yCord
                self.side = self.Sides.right

            elif self.direction == self.Directions.down:
                self.direction = self.Directions.down
                self.side = self.Sides.back
                self.pos.yCord = 0

        elif self.side == self.Sides.left:
            if self.direction == self.Directions.up:
                self.direction = self.Directions.right
                self.side = self.Sides.back
                self.pos.yCord = self.pos.xCord
                self.pos.xCord = 0

            elif self.direction == self.Directions.left:
                self.direction = self.Directions.right
                self.side = self.Sides.bottom
                self.pos.xCord = self.size - 1

            elif self.direction == self.Directions.right:
                self.direction = self.Directions.right
                self.side = self.Sides.top
                self.pos.xCord = 0

            elif self.direction == self.Directions.down:
                self.direction = self.Directions.right
                self.side = self.Sides.front
                self.pos.yCord = self.size -1 - self.pos.xCord
                self.pos.xCord = 0 

        elif self.side == self.Sides.top:
            if self.direction == self.Directions.up:
                self.direction = self.Directions.up
                self.side = self.Sides.back
                self.pos.yCord = self.size -1

            elif self.direction == self.Directions.left:
                self.direction = self.Directions.left
                self.side = self.Sides.left
                self.pos.xCord = self.size -1

            elif self.direction == self.Directions.right:
                self.direction = self.Directions.right
                self.side = self.Sides.right
                self.pos.xCord = 0

            elif self.direction == self.Directions.down:
                self.direction = self.Directions.down
                self.side = self.Sides.front
                self.pos.yCord = 0

        elif self.side == self.Sides.right:
            if self.direction == self.Directions.up:
                self.direction = self.Directions.left
                self.side = self.Sides.back
                self.pos.yCord = self.size -1 - self.pos.xCord
                self.pos.xCord = self.size -1

            elif self.direction == self.Directions.left:
                self.direction = self.Directions.left
                self.side = self.Sides.top
                self.pos.xCord = self.size - 1

            elif self.direction == self.Directions.right:
                self.direction = self.Directions.left
                self.side = self.Sides.bottom
                self.pos.xCord = self.size - 1

            elif self.direction == self.Directions.down:
                self.direction = self.Directions.left
                self.side = self.Sides.front
                self.pos.yCord = self.pos.xCord
                self.pos.xCord = self.size -1

        elif self.side == self.Sides.front:
            if self.direction == self.Directions.up:
                self.direction = self.Directions.up
                self.side = self.Sides.top
                self.pos.yCord = self.size -1

            elif self.direction == self.Directions.left:
                self.direction = self.Directions.up
                self.side = self.Sides.left
                self.pos.xCord = self.size - self.pos.yCord -1
                self.pos.yCord = 0

            elif self.direction == self.Directions.right:
                self.direction = self.Directions.up
                self.side = self.Sides.right
                self.pos.xCord = self.pos.yCord
                self.pos.yCord = self.size -1

            elif self.direction == self.Directions.down:
                self.direction = self.Directions.down
                self.side = self.Sides.bottom
                self.pos.yCord = 0

        elif self.side == self.Sides.back:
            if self.direction == self.Directions.up:
                self.direction = self.Directions.up
                self.side = self.Sides.bottom 
                self.pos.yCord = self.size -1

            elif self.direction == self.Directions.left:
                self.direction = self.Directions.down
                self.side = self.Sides.left
                self.pos.xCord = self.pos.yCord
                self.pos.yCord = self.size -1

            elif self.direction == self.Directions.right:
                self.direction = self.Directions.down
                self.side = self.Sides.right
                self.pos.xCord = self.size - self.pos.yCord -1
                self.pos.yCord = 0
                
            elif self.direction == self.Directions.down:
                self.direction = self.Directions.down
                self.side = self.Sides.top
                self.pos.yCord = 0

        self.simpleOps()

    #This function implements simple operations int the program(only +,-,*,/,%)
    def simpleOps(self):
        if(self.doOps):
            self.checkListSize(1,"op")
            op = self.opStack.pop()
            
            self.checkListSize(2,"a")
            self.checkNumber(self.aStack[len(self.aStack) -2])
            self.checkNumber(self.aStack[len(self.aStack) -1])
            opTop = int(self.aStack.pop())
            opBottom = int(self.aStack.pop())
            
            
            if(op== '*'):
                self.aStack.append(str(opTop*opBottom))
            elif(op== '/'):
                if opBottom == 0:
                    print("Can't Divide by 0")
                else:
                    self.aStack.append(str(opTop/opBottom))
            elif(op== '+'):
                self.aStack.append(str(opTop+opBottom))
            elif(op== '-'):
                self.aStack.append(str(opTop-opBottom))
            elif(op== '%'):
                if opBottom == 0:
                    print("Can't Modula by 0")
                else:
                    self.aStack.append(str(opTop%opBottom))
        else:
            pass

    # Interprets char at current position and applies relevant operation
    def interpChar(self):
        charAtPos = self.modMat[self.side.value][self.pos.yCord][self.pos.xCord]
        toCont = True

        #Do nothing if space
        if charAtPos == ' ':
            pass
        
        #Make Direction right if ">"
        elif(charAtPos == '>'):
            self.direction = self.Directions.right

        #Make Direction left if "<"
        elif(charAtPos == '<'):
            self.direction = self.Directions.left

        #Make direction up if "^"
        elif(charAtPos == '^'):
            self.direction = self.Directions.up

        #Make direction down if "v"
        elif(charAtPos == 'v'):
            self.direction = self.Directions.down

        #Clear stacks and end program if ")"
        elif(charAtPos == ')'):
            self.aStack = []
            self.opStack = []
            toCont = False

        #Load all Letters(not v) onto aStack
        elif(ord(charAtPos)>64 and ord(charAtPos)<123 and charAtPos != 'v'):
            self.aStack.append(charAtPos)
        
        #Load all numbers onto aStack
        elif(ord(charAtPos)>47 and ord(charAtPos)<58):
            self.aStack.append(charAtPos)
        
        #Load space onto aStack
        elif(charAtPos == '~'):
            self.aStack.append(' ')

        #Load relevant simple operation onto opStack
        elif(charAtPos == '%' or charAtPos == '*' or charAtPos == '/' or charAtPos == '+' or charAtPos == '-'):
            self.opStack.append(charAtPos)

        #Toggle aStackSelect - the variable responsible for which stack was selected
        elif(charAtPos == '!'):
            self.aStackSelect =  not self.aStackSelect
        
        #Toggle doOps - the variable responsible for if simple operation completed when cross sides
        elif(charAtPos == '"'):
            self.doOps =  not self.doOps

        #Convert number to corresponding ascii value
        elif(charAtPos == '='):
            self.checkListSize(1,"a")
            self.checkNumber(self.aStack[len(self.aStack) -1])
            self.aStack[len(self.aStack)-1] = chr(int(self.aStack[len(self.aStack)-1]))

        #Duplicate top value of certain stack depending on aStackSelect
        elif(charAtPos == '#'):
            if(self.aStackSelect):
                self.checkListSize(1,"a")
                self.aStack.append(self.aStack[len(self.aStack)-1])
            else:
                self.checkListSize(1,"op")
                self.opStack.append(self.aStack[len(self.opStack)-1])
        
        #Pop top value of certain stack depending on aStackSelect
        elif(charAtPos == '&'):
            if(self.aStackSelect):
                self.checkListSize(1,"a")
                self.aStack.pop()
            else:
                self.checkListSize(1,"op")
                self.opStack.pop()

        #Duplicate the nth value from a certain stack where n comes from the top value of aStack
        elif(charAtPos == '$'):
            self.checkListSize(1,"a")
            self.checkNumber(self.aStack[len(self.aStack) -1])
            eleNum = int(self.aStack.pop())
            if(self.aStackSelect):
                self.checkListSize(eleNum,"a")
                self.aStack.append(self.aStack[len(self.aStack) - eleNum])
            else:
                self.checkListSize(eleNum,"op")
                self.opStack.append(self.opStack[len(self.opStack) - eleNum])

        #Swap the nth and mth value in a certain set where an n and m coming from the top two values of aStack
        elif(charAtPos == '@'):
            self.checkListSize(2,"a")
            self.checkNumber(self.aStack[len(self.aStack) -2])
            self.checkNumber(self.aStack[len(self.aStack) -1])
            eleNum1 = int(self.aStack.pop())
            eleNum2 = int(self.aStack.pop())
            if(self.aStackSelect):
                self.checkListSize(max(eleNum1,eleNum2),"a")
                aSwap1 = self.aStack[(len(self.aStack) - eleNum1)]
                aSwap2 = self.aStack[(len(self.aStack) - eleNum2)]
                aTemp = aSwap1
                
                aSwap1 = aSwap2
                aSwap2 = aTemp
                self.aStack[(len(self.aStack) - eleNum1)] = aSwap1
                self.aStack[(len(self.aStack) - eleNum2)] = aSwap2

            else:
                self.checkListSize(max(eleNum1,eleNum2),"op")
                opSwap1 = self.opStack[len(self.aStack) - eleNum1]
                opSwap2 = self.opStack[(len(self.aStack) - eleNum2)]
                opTemp = opSwap1

                opSwap1 = opSwap2
                opSwap2 = opTemp

                self.opStack[len(self.aStack) - eleNum1] = opSwap1 
                self.opStack[(len(self.aStack) - eleNum2)] = opSwap2

        #If statement using top two elements on aStack
        # - equal -> Continue going in current direction
        # - Top element less than Bottom -> turn right
        # - Top element greater than Bottom -> turn left
        elif(charAtPos == '?'):
            self.checkListSize(2,"a")
            self.checkNumber(self.aStack[len(self.aStack) -2])
            self.checkNumber(self.aStack[len(self.aStack) -1])
            ifTop = int(self.aStack.pop())
            ifBottom = int(self.aStack.pop())
            
            if(ifTop-ifBottom > 0):
                self.direction = self.Directions((self.direction.value + 1)%4) 
            elif(ifTop-ifBottom < 0):
                self.direction = self.Directions((self.direction.value - 1)%4)
            elif(ifTop-ifBottom == 0):
                pass
        
        # Creates for loop if it doesnt exist, otherwise does another iteration through it
        # - Supports Nested for loops through a stack
        elif(charAtPos == ':'):
            existingForLoops = [f for f in self.forLoops if f.xCord == self.pos.xCord and f.yCord == self.pos.yCord]
            if len(existingForLoops)==1:
                if(existingForLoops[0].iteration >0):
                    self.direction = self.Directions((self.direction.value - 1)%4)
                    existingForLoops[0].iteration -=1
                else:
                    self.forLoops.pop()
            else:
                self.checkListSize(1,"a")
                self.forLoops.append(ForLoop(self.pos.xCord,self.pos.yCord,int(self.aStack.pop())))
                self.direction = self.Directions((self.direction.value - 1)%4)
                self.forLoops[len(self.forLoops)-1].iteration -=1

        #Input taken in and parsed character by character
        elif(charAtPos == ','):
            cubInput = input("Input Needed")
            for c in cubInput:
                self.aStack.append(c)
        
        #Everything Up until the nth element of the stack is popped and printed from top of stack to bottom
        elif(charAtPos == ';'):
            self.checkListSize(1,"a")
            self.checkNumber(self.aStack[len(self.aStack) -1])
            numToPop = int(self.aStack.pop())
            self.checkListSize(numToPop,"a")
            for i in range(numToPop):
                print(self.aStack.pop(), end = "")
            print("")
        
        #Clears aStack and opStack
        elif(charAtPos == '`'):
            self.aStack = []
            self.opStack = []

        #Prints Hello World
        elif(charAtPos== '|'):
            print("Hello World")
        

        return toCont

    #Checks if List Length is Sufficient For Operation
    # - num->ammount of list elmennts needed
    # - stack->stack this operation pertains to
    def checkListSize(self,num,stack):
        if stack == "a":
            if len(self.aStack) < num:
                print(f"\nChar Stack Length is Insufficient ")
                print(f"Pos: (Side = {self.side.name}, xCord = {self.pos.xCord}, yCord = {self.pos.yCord})")
                print(f"current Char Stack: {self.aStack}")
                print(f"current Operation Stack: {self.opStack}")
                quit()
            else:
                pass

        elif stack == "op":
            if len(self.opStack) < num:
                print(f"\nOperation Stack Length is Insufficient ")
                print(f"Pos: (Side = {self.side.name}, xCord = {self.pos.xCord}, yCord = {self.pos.yCord})")
                print(f"current Char Stack: {self.aStack}")
                print(f"current Operation Stack: {self.opStack}")
                quit()
            else:
                pass
    
    #Checks if a character is a letter
    def checkLetter(self, theChar):
        for char in range(len(theChar)):
            if ord(theChar[char])>64 and ord(theChar[char])<123 and theChar[char] != 'v':
                pass
            else:
                print(f"'{theChar[char]}' is a number when you needed a letter")
                quit();

    def checkNumber(self, theChar):
        for char in range(len(theChar)):
            if ord(theChar[char])>47 and ord(theChar[char])<58:
                pass
            else:
                print(f"'{theChar[char]}' is a letter when you needed a number")
                quit();

    
    #Prints the Modified Matrix
    def printMod(self):
        print(self.modMat)
        print("\n")
    
    #Function that is not yet implemented with the purpose of printing
    #the matrix in a way that would make it more easy to debug
    def fancyPrint(self):
        pass

    #Enums representing different sides of cube
    class Sides(enum.Enum):
        back = 0
        left = 1
        top = 2
        right = 3
        front = 4
        bottom = 5
    
    #Enums representing different directions
    class Directions(enum.Enum):
        up = 0
        left = 1
        down = 2
        right = 3
    
    side = Sides.left
    direction = Directions.right

def main():
    fileName = input("Give the Cube File Name ")
    readFile = FileReader.FileReader(fileName)
    myMatrix = readFile.read()

    inter = FormatChecker.Interp(myMatrix)
    inter.Correct_Format()

    runner = Runner(myMatrix,inter.size)
    runner.startRunner()

if __name__ == "__main__": main()        