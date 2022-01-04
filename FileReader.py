import sys

#This class relates to reading the input from for the cube file path
class FileReader:

    #filename -> string holding the filename and path
    def __init__(self, filename):
        self.fileInput = [] #2D list holding all text in file
        self.filename = filename 

    #Checks if file exists and then reads input into 2D list - fileInput
    def read(self):
        try:
            f = open(self.filename, "r")

        except IOError:
            print("File doesnt exist")
            quit()

        for line in f.readlines():
            smallList = []
            smallList[:0] = line
            self.fileInput.append(smallList)
            
        f.close()
        return self.fileInput
        
    #Prints fileInput
    def print(self):
        print(self.fileInput)
    

def main():
    fileName = input("Give the Cube File Name ")
    readFile = FileReader(fileName)
    readFile.read()
    readFile.print()

if __name__ == "__main__": main()