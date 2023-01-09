import re
import pyttsx3
from PyPDF2 import PdfReader


def read_pdf():
    pdf = PdfReader('book.pdf')
    return ' '.join([re.sub('\s+', ' ', page.extract_text().strip()) for page in pdf.pages])


def save_audio(read_pdf):
    speaker = pyttsx3.init()
    speaker.save_to_file(read_pdf, 'book.ogg')
    speaker.runAndWait()
    speaker.stop()


def speak(read_pdf):
    speaker = pyttsx3.init()
    """ Seems to fail on MacOS """
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say(read_pdf)
    speaker.runAndWait()
    speaker.stop()


if __name__ == '__main__':
    """ Next two lines for debugging purposes """
    # print(read_pdf())
    # speak(read_pdf())
    save_audio(read_pdf())
