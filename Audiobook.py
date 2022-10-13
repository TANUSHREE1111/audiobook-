import pyttsx3
import PyPDF2

book= open('Oop.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(1)
txt = page.extractText()
speaker.say(txt)
speaker.runAndWait()


