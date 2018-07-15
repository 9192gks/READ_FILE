import PyPDF2

class Test:
    def readTextFile(self, keyword):
        fo = open('test.txt','r')
        lines = fo.readlines()
        for line in lines:
            count = 0
            if keyword in line:
                print(line)
                for word in line.split(" "):
                    if keyword == word:
                        count += 1
                print("Keyword "+keyword+" occurse "+count+ "times in this text file")


#Execution
t = Test()
t.readTextFile("inheritance")

#sample out put like below
#Keyword inheritance occurse 5 times in this text file)
