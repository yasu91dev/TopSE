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
            self.fileSystem = FileSystem()  # ディレクトリの場合は自身でファイルシステムを持つ

    def getFileName(self):
        return self.fileName

    def getFileType(self):
        return self.fileType


class FileSystem:   # ディレクトリ相当
    def __init__(self):
        self.fileList = []

    def searchFile(self, fileName):
        if( len(self.fileList) == 0 ):
            return None
        else:
            for n in self.fileList:
                if(n.getFileName() == fileName):
                    return n
                else:
                    return None
    
    def addFile(self, fileName, fileType):
        if "/" in fileName:    # ファイルシステムで使用不可能な文字がfileNameに含まれている場合
            print("")
        else:
            file = File(fileName, fileType)
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
        self.fs = File("/", "d")
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
                    if(self.fs.fileSystem.searchFile(istr.getArg(i)) is None):
                        self.fs.fileSystem.addFile(istr.getArg(i), "f")
                    i += 1

            elif cmd == "ls":
                self.fs.fileSystem.showFiles()

            elif cmd == "mkdir":
                i = 1
                while i < istr.getArgNum():
                    if(self.fs.fileSystem.searchFile(istr.getArg(i)) is None ):
                        self.fs.fileSystem.addFile(istr.getArg(i), "d")
                    i += 1

            elif cmd == "cd":
                if istr.getArgNum() > 2:
                    print("cd: too many aruguments")
                elif istr.getArgNum() == 1:
                    # ルートディレクトリに戻る
                    print("T.B.D")
                else:
                    # たぶん考え方がこれじゃダメなんだと思われる。インタスタンス内にいるインスタンスを返すことはできない？？
                    directory = self.fs.fileSystem.searchFile(istr.getArg(1))
                    if not directory:
                        if directory.getFileType() == "d":
                            pass
                        else:
                            print("cd: " + istr.getArg(1) + ": Not a directory")
                    else:
                        print("cd: " + istr.getArg(1) + ": No such file or directory")

            elif cmd == "exit":
                break
            
            else:
                print(cmd + ": command not found")

            print("")


if __name__ == "__main__":
    mysh = MyShell()
    mysh.runShell()
