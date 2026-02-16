""" Duck Typing : it is concept where the type of
an object is determined by its behaviour , not by
its class"""

class InkjetPrinter:
    def printDocument(self, document):
        print("Inkjet printer printing :", document)

class LaserPrinter:
    def printDocument(self, document):
        print("Laser printer printing :", document)

class PDFWritter:
    def printDocument(self, document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.printDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWritter())

main()
