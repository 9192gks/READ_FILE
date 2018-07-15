import PyPDF2
class Test:
    def readPDF(self, keyword):
        pdfFileObj = open('test.pdf', 'rb')
        pdfReader = PdfFileReader(pdfFileObj)
        pages = pdfReader.getNumPages()
        count = 0
        for page in range(pages):
            page_obj = pdfReader.getPage(page)
            page_data = page_obj.extractText()
            lines = page_data
            for line in lines:
                if keyword in line:
                    print(line)
                    for word in line.split(" "):
                        if keyword == word:
                            count += 1
        print("Keyword "+keyword+" occurse "+count+ "times in this pdf file")
        pdfFileObj.close()


#Execution
t = Test()
t.readPDF("inheritance")

#sample out put like below
#Keyword inheritance occurse 5 times in this pdf file)
