import pyttsx3 #import text to speech module using pip install pyttsx3
import PyPDF2 #import pdf reader module using pip install pyPDF2
book = open('file.pdf', 'rb') #enter the book name
pdfReader = PyPDF2.PdfFileReader(book) 
pages = pdfReader.numPages #Calculates the number of pages in this PDF file.
print(pages)

speaker = pyttsx3.init() #object creation
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
