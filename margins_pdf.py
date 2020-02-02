import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter, pdf
import os
import glob

#adding a margin on the sides of the page
margin = 100
bottom = 0
right = True
left = False

def main():
    #finding the file in the same folder
    script_path = os.path.dirname(os.path.abspath( __file__ ))
    a = '/'
    string = a.join([script_path, "*.pdf"])
    pdfs = glob.glob(string)
    #print('pdf count: ', len(pdfs))
    if len(pdfs)==0:
        print("ERROR: There are no pdf files in the location of Python script.")
        return

    file1 = pdfs[0]
    name = file1.replace(script_path + '/', '') #getting the name of the file
    print(name)

    pdfFileObject = open(file1, 'rb') #opening a pdf file
    pdf1 = PdfFileReader(pdfFileObject) # get a pdf viewer object
    writer = PdfFileWriter()
    pages = pdf1.getNumPages()
    print("pages: ", pages)


    for i in range(pages):
        pageObject1 = pdf1.getPage(i)
        #get width and height
        print(pageObject1.mediaBox.getWidth(), pageObject1.mediaBox.getHeight() )
        #pageObject1.createBlankPage(600,800)#(pageObject1.mediaBox.getWidth() + margin, pageObject1.mediaBox.getWidth() + bottom )
        width = pageObject1.mediaBox.getWidth()
        height = pageObject1.mediaBox.getHeight()
        page = writer.addBlankPage(width + margin*right +margin*left, height + bottom)
        page.mergeScaledTranslatedPage( pageObject1, 1, left*margin, bottom)

    #writer.addPage(page)
    with open(script_path + "/margins_" + name , "wb") as out_file:
            writer.write(out_file)
            print("\n SUCCESS: File was created at: \n"+script_path + "/margins_" + name)

    out_file.close()
    pdfFileObject.close()
    return




main()
