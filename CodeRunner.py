import enum
import FormatChecker
import FileReader

class Position:
    def __init__(self):
        self.xCord = -1
        self.yCord = -1

class ForLoop:
    def __init__(self,xCord,yCord,iteration):
        self.xCord = xCord
        self.yCord = yCord
        self.iteration = iteration

class Runner:
    def __init__(self,inMat, size):
        self.inMat = inMat
        self.modMat = []
        self.size = size

        self.aStack = []
        self.opStack = []
        self.chars = []

        self.pos = Position()
        self.aStackSelect = True
        self.doOps = True
        self.forLoops = []
        # self.side = 
        # self.direction = Directions

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
    
    def startRunner(self):
        self.runnerSetup()
        self.printMod()
        self.moveLoop()

    def runnerSetup(self):
        self.initModMat()
        for row in range(self.size):
            for col in range(self.size):
                if self.modMat[self.side.value][row][col] == '(':
                    self.pos.xCord = col
                    self.pos.yCord = row
                    # print("init col is" + str(col))
                    # print("init row is" + str(row))
                    return
        #         print("did find")
        # print("havent found it")


    def moveLoop(self):
        toContinue = True
        while toContinue:
            self.nextPos()
            toContinue = self.interpChar()
            print(f"aStack Print: {self.aStack}")
            print(f"opStack Print: {self.opStack}")
            # print(self.direction)
            # print(self.side)
            # print("toContinue is " + str(toContinue) + "\n")

        print("Program has ended")

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
    
    def inBounds(self, cord):
        if cord>=self.size or cord < 0:
            return False
        else:
            return True


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

    def simpleOps(self):
        if(self.doOps):
            opTop = int(self.aStack.pop())
            opBottom = int(self.aStack.pop())
            
            if(self.opStack):
                op = self.opStack.pop()
                if(op== '*'):
                    self.aStack.append(opTop*opBottom)
                elif(op== '/'):
                    self.aStack.append(opTop/opBottom)
                elif(op== '+'):
                    self.aStack.append(opTop+opBottom)
                elif(op== '-'):
                    self.aStack.append(opTop-opBottom)
                elif(op== '%'):
                    self.aStack.append(opTop%opBottom)
        else:
            pass
        



    def interpChar(self):
        charAtPos = self.modMat[self.side.value][self.pos.yCord][self.pos.xCord]
        # print("char at position is " + charAtPos)
        # print("char at position is " + str(self.pos.yCord))
        # print("char at position is " + str(self.pos.xCord))
        toCont = True
        if charAtPos == ' ':
            pass
        elif(charAtPos == '>'):
            self.direction = self.Directions.right
            # print("dir changed to right")
        elif(charAtPos == '<'):
            self.direction = self.Directions.left
            # print("dir changed to left")
        elif(charAtPos == '^'):
            self.direction = self.Directions.up
            # print("dir changed to up")
        elif(charAtPos == 'v'):
            self.direction = self.Directions.down
            # print("dir changed to down")
        elif(charAtPos == ')'):
            self.aStack = []
            self.opStack = []
            toCont = False

        elif(ord(charAtPos)>64 and ord(charAtPos)<123 and charAtPos != 'v'):
            self.aStack.append(charAtPos)
        
        elif(ord(charAtPos)>47 and ord(charAtPos)<58):
            self.aStack.append(charAtPos)
        
        elif(charAtPos == '~'):
            self.aStack.append(' ')

        elif(charAtPos == '%' or charAtPos == '*' or charAtPos == '/' or charAtPos == '+' or charAtPos == '-'):
            self.opStack.append(charAtPos)

        elif(charAtPos == '!'):
            self.aStackSelect =  not self.aStackSelect
        
        elif(charAtPos == '"'):
            self.doOps =  not self.doOps

        elif(charAtPos == '='):
            self.aStack[len(self.aStack)-1] = chr(int(self.aStack[len(self.aStack)-1]))

        elif(charAtPos == '#'):
            if(self.aStackSelect):
                self.aStack.append(self.aStack[len(self.aStack)-1])
            else:
                self.opStack.append(self.aStack[len(self.opStack)-1])
        elif(charAtPos == '&'):
            if(self.aStackSelect):
                self.aStack.pop()
            else:
                self.opStack.pop()
        elif(charAtPos == '$'):
            eleNum = int(self.aStack.pop())
            if(self.aStackSelect):
                self.aStack.append(self.aStack[len(self.aStack) - eleNum])
            else:
                self.opStack.append(self.opStack[len(self.opStack) - eleNum])
        elif(charAtPos == '@'):
            eleNum1 = int(self.aStack.pop())
            eleNum2 = int(self.aStack.pop())
            if(self.aStackSelect):
                aSwap1 = self.aStack[(len(self.aStack) - eleNum1)]
                aSwap2 = self.aStack[(len(self.aStack) - eleNum2)]
                aTemp = aSwap1
                
                aSwap1 = aSwap2
                aSwap2 = aTemp
                self.aStack[(len(self.aStack) - eleNum1)] = aSwap1
                self.aStack[(len(self.aStack) - eleNum2)] = aSwap2

            else:
                opSwap1 = self.opStack[len(self.aStack) - eleNum1]
                opSwap2 = self.opStack[(len(self.aStack) - eleNum2)]
                opTemp = opSwap1

                opSwap1 = opSwap2
                opSwap2 = opTemp

                self.opStack[len(self.aStack) - eleNum1] = opSwap1 
                self.opStack[(len(self.aStack) - eleNum2)] = opSwap2

        
        elif(charAtPos == '?'):
            ifTop = int(self.aStack.pop())
            ifBottom = int(self.aStack.pop())
            
            if(ifTop-ifBottom > 0):
                self.direction = self.Directions((self.direction.value + 1)%4) 
            elif(ifTop-ifBottom < 0):
                self.direction = self.Directions((self.direction.value - 1)%4)
            elif(ifTop-ifBottom == 0):
                pass
        
        elif(charAtPos == ':'):
            existingForLoops = [f for f in self.forLoops if f.xCord == self.pos.xCord and f.yCord == self.pos.yCord]
            if len(existingForLoops)==1:
                print("for loop already exists")
                if(existingForLoops[0].iteration >0):
                    self.direction = self.Directions((self.direction.value - 1)%4)
                    existingForLoops[0].iteration -=1
                else:
                    self.forLoops.pop()
            else:
                print("made new for loop")
                self.forLoops.append(ForLoop(self.pos.xCord,self.pos.yCord,int(self.aStack.pop())))
                self.direction = self.Directions((self.direction.value - 1)%4)
                self.forLoops[len(self.forLoops)-1].iteration -=1
        
        elif(charAtPos == ','):
            cubInput = input("Input Needed")
            for c in cubInput:
                self.aStack.append(c)
        
        elif(charAtPos == ';'):
            numToPop = int(self.aStack.pop())
            for i in range(numToPop):
                print(self.aStack.pop(), end = "")
            print("")
        
        elif(charAtPos == '`'):
            self.aStack = []
            self.opStack = []

        elif(charAtPos== '|'):
            print("Hello World")
        
            




        
            


                

        return toCont
    
    def printMod(self):
        print(self.modMat)
        print("\n")
    
    def fancyPrint(self):
        pass

    class Sides(enum.Enum):
        back = 0
        left = 1
        top = 2
        right = 3
        front = 4
        bottom = 5
    
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
    readFile.print()

    inter = FormatChecker.Interp(myMatrix)
    inter.Correct_Format()
    inter.i_print()

    runner = Runner(myMatrix,inter.size)
    runner.startRunner()
    # if len(sys.argv) ==2: readFile.read(sys.argv[1])
    # else: print("Usage:", sys.argv[0], "filename")

    # readFile.checkFormat()

if __name__ == "__main__": main()        
            