import pyttsx3,PyPDF2,os,sys

pdfreader = PyPDF2.PdfReader(open('storia.pdf' , 'rb'))
speaker =pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n',' ')
    #print(clean_text)

speaker.save_to_file(clean_text,'test.mp3')
#os.rename("test.mp3", "joler/Downloads/audible.mp3")
speaker.runAndWait()

speaker.stop()