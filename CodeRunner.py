import enum
import FormatChecker
import FileReader

class Position:
    def __init__(self):
        self.xCord = -1
        self.yCord = -1

class Runner:
    def __init__(self,inMat, size):
        self.inMat = inMat
        self.modMat = []
        self.size = size

        self.aStack = []
        self.opStack = []
        self.chars = []

        self.pos = Position()
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
                self.modMat[3][row][col] = self.inMat[row+(self.size+1)+1][(col+self.size+1)*2+1]

        for row in range(self.size):
            for col in range(self.size):
                self.modMat[4][row][col] = self.inMat[row+(self.size+1)*2+1][col+(self.size+1)+1]

        for row in range(self.size):
            for col in range(self.size):
                self.modMat[5][row][col] = self.inMat[row+(self.size*3+1)+1][col+(self.size+1)+1]
    
    def startRunner(self):
        self.initModMat()
        for row in range(self.size):
            for col in range(self.size):
                if self.modMat[self.side.value][row][col] == "(":
                    self.pos.xCord = col
                    self.pos.yCord = row
                    return


    def move(self):
        self.nextPos()

    def nextPos(self):
        if self.direction == self.Directions.up:
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
        elif self.direction == self.Directions.down:
            if self.inBounds(int(self.pos.xCord-1)):
                self.pos.yCord-=1
            else:
                self.switchSides()
    
    def inBounds(self, cord):
        if cord>=self.size or cord < 0:
            return False
        else:
            return True


    def switchSides():
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

    def interpChar():
        pass
    
    def printMod(self):
        print(self.modMat)
    
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
        right = 2
        down = 3
    
    side = Sides.back
    direction = Directions.up

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
    runner.move()
    runner.printMod()
    # if len(sys.argv) ==2: readFile.read(sys.argv[1])
    # else: print("Usage:", sys.argv[0], "filename")

    # readFile.checkFormat()

if __name__ == "__main__": main()        
            