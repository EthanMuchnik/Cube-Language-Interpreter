import sys

class FileReader:
    def __init__(self, filename):
        self.fileInput = []
        self.filename = filename

    def read(self):
        
        try:
            f = open(self.filename, "r")

        except IOError:
            print("File doesnt exist")
            # f.close()
            quit()

        for line in f.readlines():
            smallList = []
            smallList[:0] = line
            self.fileInput.append(smallList)
            
        f.close()
        return self.fileInput
        

    def print(self):
        print(self.fileInput)
    

def main():
    fileName = input("Give the Cube File Name ")
    readFile = FileReader(fileName)
    readFile.read()
    # if len(sys.argv) ==2: readFile.read(sys.argv[1])
    # else: print("Usage:", sys.argv[0], "filename")

    # readFile.checkFormat()
    readFile.print()

if __name__ == "__main__": main()