import re
import pyttsx3
from PyPDF2 import PdfReader


def speak_and_save_audio(read_pdf):
    speaker = pyttsx3.init()
    # voices = speaker.getProperty('voices')
    # speaker.setProperty('voice', voices[1].id)
    speaker.say(read_pdf)
    speaker.save_to_file(read_pdf, 'book.ogg')
    speaker.runAndWait()
    speaker.stop()


def read_pdf():
    pdf = PdfReader('book.pdf')
    return ' '.join([re.sub('\s+', ' ', page.extract_text().strip()) for page in pdf.pages])


if __name__ == '__main__':
    #print(read_pdf())
    speak_and_save_audio(read_pdf())