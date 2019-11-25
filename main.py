class InputString:
    inStream = ""

    def getInput(self):
        self.inStream = input("$ ")
        return

    def getCmd(self) -> str:
        return self.inStream.split()[0]

    def getArg(self):
        return " ".join(self.inStream.split()[1:])

class MyShell:
    def runShell(self):
        istr = InputString()
        
        while 1:
            istr.getInput()
            cmd = istr.getCmd()
            
            if cmd == "echo":
                print(istr.getArg())
            
            elif cmd == "exit":
                break
            
            else:
                print(cmd + ": command not found")

            print("")

if __name__ == "__main__":
    mysh = MyShell()
    mysh.runShell()
