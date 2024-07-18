import pyttsx3
from PyPDF2 import PdfReader
import re

def clean_text(text):
    # Remove newlines and excessive spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove any extra spaces around punctuation
    text = re.sub(r'\s([?.!,;"](?:\s|$))', r'\1', text)
    return text

# Use the correct class PdfReader instead of the deprecated PdfFileReader
pdfreader = PdfReader('book.pdf')
speaker = pyttsx3.init()

full_text = ""

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    if text:  # Check if text is not None
        clean_text = clean_text(text)
        full_text += clean_text + " "
        print(clean_text)

# Save the cleaned text to an MP3 file
speaker.save_to_file(full_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()

