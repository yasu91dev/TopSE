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
    def __init__(self, fileName, fileType):
        self.fileName = fileName
        self.fileType = fileType    # f:ファイル, d:ディレクトリ
        if fileType == "d":
            self.fileList = {}

    def getFileName(self):
        return self.fileName

    def getFileType(self):
        return self.fileType

    def searchFile(self, filePath):
        splitFilePath = filePath.split("/")
        fileName = splitFilePath[1]
        if fileName in self.fileList.keys():
            if self.fileList[fileName].getFileType() == "d":
                return self.fileList[fileName].searchFile("/" + "/".join(splitFilePath[2:]))
            else:
                return self.fileList[fileName] #ファイルが見つかった
        else:
            return None #ファイルが見つからなかった
    
    def searchDirectory(self, filePath):
        splitFilePath = filePath.split("/")
        fileName = splitFilePath[1]
        if splitFilePath[-1] in self.fileList.keys():
            return self.fileList[splitFilePath[-1]]
        elif fileName in self.fileList.keys():
            if self.fileList[fileName].getFileType() == "d":
                return self.fileList[fileName].searchDirectory("/" + "/".join(splitFilePath[2:]))
            else:
                return None #ファイルだった
        else:
            return None #ファイルが見つからなかった

    def addFile(self, filePath, fileType):
        splitFilePath = filePath.split("/")
        fileName = splitFilePath[1]
        if fileName in self.fileList.keys():
            if self.fileList[fileName].getFileType() == "d":
                return self.fileList[fileName].addFile("/" + "/".join(splitFilePath[2:]), fileType)
            else:
                return False
        else:
            self.fileList[fileName] = File(fileName, fileType)
            return True
    
    def showFiles(self, filePath):
        if filePath == "/":
            findFile = self.fileList
        else:
            findFile = self.searchDirectory(filePath)
        fileList = []

        for i in findFile.fileList.values():
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
        self.fs = File("/", "d")
        self.wd = "/"   # Workind Directory(./)
    
    def runShell(self):
        istr = InputString()
        
        while True:
            print("name@MACHINE " + self.wd)
            istr.getInput()
            cmd = istr.getCmd()
            
            if cmd == "echo":
                print(istr.getConcatedArg())
            
            elif cmd == "touch":
                i = 1
                while i < istr.getArgNum():
                    if(istr.getArg(i)[0:2] == ".."):
                        print("..")
                    elif(istr.getArg(i)[0] == "."):
                        filePath = istr.getArg(i)
                        if self.wd == "/":
                            filePath = filePath.replace(".", "", 1)
                        else:
                            filePath = filePath.replace(".", self.wd, 1)
                    elif(not "/" in istr.getArg(i)):
                        if self.wd == "/":
                            filePath = self.wd + istr.getArg(i)
                        else:
                            filePath = self.wd + "/" + istr.getArg(i)
                    else:
                        filePath = istr.getArg(i)

                    self.fs.addFile(filePath, "f")
                    i += 1

            elif cmd == "ls":
                filePath = self.wd
                self.fs.showFiles(filePath)
                pass

            elif cmd == "mkdir":
                i = 1
                while i < istr.getArgNum():
                    if(istr.getArg(i)[0:2] == ".."):
                        print("..")
                    elif(istr.getArg(i)[0] == "."):
                        filePath = istr.getArg(i)
                        if self.wd == "/":
                            filePath = filePath.replace(".", "", 1)
                        else:
                            filePath = filePath.replace(".", self.wd, 1)
                    elif(not "/" in istr.getArg(i)):
                        if self.wd == "/":
                            filePath = self.wd + istr.getArg(i)
                        else:
                            filePath = self.wd + "/" + istr.getArg(i)
                    else:
                        filePath = istr.getArg(i)

                    if(not self.fs.searchFile(filePath)):
                        self.fs.addFile(filePath, "d")
                    else:
                        print("mkdir: cannot create directory ‘" + istr.getArg(i) + "’: File exists")
                    i += 1

            elif cmd == "cd":
                if istr.getArgNum() > 2:
                    print("cd: too many aruguments")
                elif istr.getArgNum() == 1:
                    # ルートディレクトリに戻る
                    self.wd = "/"
                else:
                    i = 1
                    if(istr.getArg(i)[0:2] == ".."):
                        print("..")
                    elif(istr.getArg(i)[0] == "."):
                        filePath = istr.getArg(i)
                        if self.wd == "/":
                            filePath = filePath.replace(".", "", 1)
                        else:
                            filePath = filePath.replace(".", self.wd, 1)
                    elif(not "/" in istr.getArg(i)):
                        if self.wd == "/":
                            filePath = self.wd + istr.getArg(i)
                        else:
                            filePath = self.wd + "/" + istr.getArg(i)
                    else:
                        filePath = istr.getArg(i)
                    
                    findFile = self.fs.searchDirectory(filePath)
                    if not findFile:
                        print("cd: " + istr.getArg(1) + ": No such file or directory")
                    elif findFile.getFileType == "f":
                        print("cd: " + istr.getArg(1) + ": Not a directory")
                    else:
                        self.wd = filePath

            elif cmd == "pwd":
                print(self.wd)

            elif cmd == "exit":
                break
            
            else:
                print(cmd + ": command not found")

            print("")
        
        return


if __name__ == "__main__":
    mysh = MyShell()
    mysh.runShell()
