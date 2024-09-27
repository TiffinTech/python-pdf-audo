"""Module providing RegEx"""
import re
import pyttsx4
from PyPDF2 import PdfReader

def read_pdf():
    """Function parse file"""
    pdf = PdfReader('book.pdf')
    return ' '.join([re.sub(r'\s+', ' ', page.extract_text().strip()) for page in pdf.pages])

def save_audio():
    """Function save file to ogg"""
    speaker.save_to_file(STRIPPED_TEXT, 'book.ogg')
    speaker.runAndWait()
    speaker.stop()

def speak():
    """Function read out"""
    speaker.say(STRIPPED_TEXT)
    speaker.runAndWait()
    speaker.stop()

def change_voice(gender='VoiceGenderFemale'):
    """Function change voice"""
    for voice in speaker.getProperty('voices'):
        #print(voice.languages)
        #print(voice.gender)
        if ENGLISH in voice.languages and gender == voice.gender:
            speaker.setProperty('voice', voice.id)
            return True
    raise RuntimeError(f"Language '{ENGLISH}' for gender '{gender}' not found")

speaker = pyttsx4.init()
STRIPPED_TEXT = read_pdf()
ENGLISH = b'\x02en-gb'
DEUTSCH = b'\x05de'

if __name__ == '__main__':
    #print(stripped_text)
    change_voice('male')
    speaker.setProperty('rate', 160)
    speak()
    save_audio()
