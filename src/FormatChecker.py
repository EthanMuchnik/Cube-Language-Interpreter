import FileReader 

#This class relates to determining if the provided input file
#is the correct format
class Interp:

    #matrix -> 2D list representing the raw input from text file
    def __init__(self,matrix):
        self.matrix = matrix
        self.size = None #size of each side of the cube
        self.correct =None #boolean to show if correct format was used
    
    #Determines if Correct Format was used
    def Correct_Format(self):
        self.__Cube_Size()
        self.__Outline_Correct()

    #Determines if the size number provided at top left corner is legitamite
    #- Quits if not correct
    def __Cube_Size(self):
        if(int(self.matrix[0][0]) >9 or int(self.matrix[0][0]) < 0):
            print("Size number not located in right place")
            quit()
        else:
            self.size = int(self.matrix[0][0])

    #Determines if the outline is the correct format
    def __Outline_Correct(self):
        for r in range(len(self.matrix)):
            if r == 0 or r == self.size*3+3 or r == self.size*4+4:
                for c in range(self.size+1,self.size*2+3):
                    if self.matrix[r][c]!='.' :
                        print(f"Your formatting is not correct on row {r} and column {c}")
                        quit()

            elif r == self.size*1+1 or r == self.size*2+2:
                for c in range(self.size*3+4):
                    if self.matrix[r][c]!='.':
                        print(f"Your formatting is not correct on row {r} and column {c}")
                        quit()

            elif r>(self.size+1) and r <=(self.size*2 +1):
                if self.matrix[r][0]!= '.' or self.matrix[r][self.size+1]!= '.' or self.matrix[r][self.size*2+2]!='.' or self.matrix[r][self.size*3+3]!='.':
                    print(f"Your formatting is not correct on row {r} and column {c}")
                    quit()

            elif r<=(self.size + (self.size+1)*4):
                if self.matrix[r][self.size+1]!= '.' or self.matrix[r][self.size*2+2]!='.':
                    print(f"Your formatting is not correct on row {r} and column {c}")
                    quit()
                        
        self.correct = True

    #prints the formatted interpretation of the orginal text file
    def i_print(self):
        if self.correct!=True:
            print("You need to run the Correct_Format function")
            return
        for r in self.matrix:
            tempString = " "
            for element in r:
                tempString += element 

            print(tempString)


def main():
    fileName = input("Give the Cube File Name ")
    readFile = FileReader.FileReader(fileName)
    myMatrix = readFile.read()
    readFile.print()

    inter = Interp(myMatrix)
    inter.Correct_Format()
    inter.i_print()

if __name__ == "__main__": main()        