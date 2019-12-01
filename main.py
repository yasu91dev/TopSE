class InputString:
    def __init__(self):
        self.inStream = ""

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


class File:
    def __init__(self, fileName, fileType, filePath):
        self.fileName = fileName
        self.fileType = fileType    # f:File, d:Directory
        self.filePath = filePath

    def getFileName(self):
        return self.fileName

    def getFileType(self):
        return self.fileType
    
    def getFilePath(self):
        return self.filePath


class FileSystem:
    def __init__(self):
        self.fileList = []

    def searchFile(self, fileName):
        if( len(self.fileList) == 0 ):
            return False
        else:
            for n in self.fileList:
                if(n.getFileName() == fileName):
                    return True
                else:
                    return False
    
    def addFile(self, fileName, fileType, filePath):
        if "/" in fileName:    # ファイルシステムで使用不可能な文字がfileNameに含まれている場合
            print("")
        else:
            file = File(fileName, fileType, filePath)
            self.fileList.append(file)
        return

    def showFiles(self):
        fileList = []

        for i in self.fileList:
            if i.getFileType() == "d":
                fileList.append(i.getFileName() + "/")
            else:
                fileList.append(i.getFileName())

        if(len(fileList) != 0):
            sortList = sorted(fileList)
            print("  ".join(sortList))
        
        return


class MyShell:
    def __init__(self):
        self.fs = FileSystem()
        self.wd = "/"   # Workind Directory
    
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
                        self.fs.addFile(istr.getArg(i), "f", self.wd)
                    i += 1

            elif cmd == "ls":
                self.fs.showFiles()

            elif cmd == "mkdir":
                i = 1
                while i < istr.getArgNum():
                    if(self.fs.searchFile(istr.getArg(i)) == False):
                        self.fs.addFile(istr.getArg(i), "d", self.wd)
                    i += 1

            elif cmd == "cd":
                pass

            elif cmd == "exit":
                break
            
            else:
                print(cmd + ": command not found")

            print("")


if __name__ == "__main__":
    mysh = MyShell()
    mysh.runShell()
