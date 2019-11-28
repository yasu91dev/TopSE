class InputString:
    inStream = ""

    def getInput(self):
        self.inStream = input("$ ")
        return

    def getCmd(self):
        return self.inStream.split()[0]

    def getArgNum(self):
        return len(self.inStream.split())

    def getConcatedArg(self):
        return " ".join(self.inStream.split()[1:])

    def getArg(self, posi):
        return self.inStream.split()[posi]

class FileSystem:
    fileList = []

    def searchFile(self, name):
        if( len(self.fileList) == 0 ):
            return False
        else:
            for n in self.fileList:
                if(n==name): return True
                else:        return False
    
    def addFile(self, filename):
        self.fileList.append(filename)
        return

    def showFiles(self):
        if(len(self.fileList)!=0):
            sortList = sorted(self.fileList)
            print("  ".join(sortList))
        return

class MyShell:
    fs = FileSystem()
    
    def runShell(self):
        istr = InputString()
        
        while True:
            istr.getInput()
            cmd = istr.getCmd()
            
            if cmd == "echo":
                print(istr.getConcatedArg())
            
            elif cmd == "touch":
                i = 1
                while i < istr.getArgNum():
                    if(self.fs.searchFile(istr.getArg(i)) == False):
                        self.fs.addFile(istr.getArg(i))
                    i += 1

            elif cmd == "ls":
                self.fs.showFiles()

            elif cmd == "exit":
                break
            
            else:
                print(cmd + ": command not found")

            print("")

if __name__ == "__main__":
    mysh = MyShell()
    mysh.runShell()
