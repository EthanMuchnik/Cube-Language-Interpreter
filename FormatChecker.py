import FileReader 

class Interp:
    def __init__(self,matrix):
        self.matrix = matrix
        self.size = None
        self.correct =None
    
    def Correct_Format(self):
        self.__Cube_Size()
        self.__Outline_Correct()
        print("Checks completed")

    def __Cube_Size(self):
        if(int(self.matrix[0][0]) >9 or int(self.matrix[0][0]) < 0):
            print("Size number not located in right place")
            quit()
        else:
            self.size = int(self.matrix[0][0])
            # if len(matrix)<(self.size*3+5):
            #     print("Not enough rows")
            #     quit();
            
            # for a in matrix:
            #     for b in matrix[a]:
            #         if b

    def __Outline_Correct(self):
        # row = 0
        count =0
        for r in range(len(self.matrix)):
            if r == 0 or r == self.size*3+3 or r == self.size*4+4:
                for c in range(self.size+1,self.size*2+3):
                    count+=1
                    if self.matrix[r][c]!='.' :
                        print(f"Your formatting is not correct on row {r} and column {c}")
                        quit()
            elif r == self.size*1+1 or r == self.size*2+2:
                for c in range(self.size*3+4):
                    count+=1
                    if self.matrix[r][c]!='.':
                        print(f"Your formatting is not correct on row {r} and column {c}")
                        quit()
            elif r>(self.size+1) and r <=(self.size*2 +1):
                count+=4
                if self.matrix[r][0]!= '.' and self.matrix[r][self.size+1]!= '.' and self.matrix[r][self.size*2+1]!='.' and self.matrix[r][self.size*3+2]!='.':
                    print(f"Your formatting is not correct on row {r} and column {c}")
                    quit()
            elif r<=(self.size + (self.size+1)*4):
                count+=2
                if self.matrix[r][self.size+1]!= '.' and self.matrix[r][self.size*2+1]!='.':
                    print(f"Your formatting is not correct on row {r} and column {c}")
                    quit()
            
            
        print(f"count is {count}")
        self.correct = True
    def i_print(self):
        if self.correct!=True:
            print("You need to run the Correct_Format function")
            return
        for r in self.matrix:
            # if r == 0 or r == self.size*3+3 or r == self.size*4+4:

            # elif r == self.size*1+1 or r == self.size*2+2:
            # elif r>(self.size+1) and r <=(self.size*2 +1):
            # elif r<=(self.size + (self.size+1)*4):
            # print(r)
            tempString = " "
            for element in r:
                tempString += element 
            # tempString.join(r)
            # print(f"printing {r}")
            print(tempString)


def main():
    fileName = input("Give the Cube File Name ")
    readFile = FileReader.FileReader(fileName)
    myMatrix = readFile.read()
    readFile.print()

    inter = Interp(myMatrix)
    inter.Correct_Format()
    inter.i_print()
    # if len(sys.argv) ==2: readFile.read(sys.argv[1])
    # else: print("Usage:", sys.argv[0], "filename")

    # readFile.checkFormat()

if __name__ == "__main__": main()        

        

