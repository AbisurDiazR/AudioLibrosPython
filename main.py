import pyttsx3 # importamo la librebria pyttsx3
import PyPDF2 # importamos la libraria pypdf para leer pdfs

book = open('triveza.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init() # inicializamos el speaker

for pageNumber in range(1,pages):    
    page = pdfReader.getPage(pageNumber)    
    text = page.extractText()    
    speaker.say(text) # llamamos la función sey de python
    speaker.runAndWait()