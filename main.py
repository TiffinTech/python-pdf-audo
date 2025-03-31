import pyttsx3
import PyPDF2
import argparse
import os

class PDFToAudioConverter:
    def __init__(self, pdf_path, output_path, voice_id=None, rate=None):
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.voice_id = voice_id
        self.rate = rate
        self.speaker = pyttsx3.init()

    def configure_speaker(self):
        if self.voice_id:
            voices = self.speaker.getProperty('voices')
            self.speaker.setProperty('voice', voices[self.voice_id].id)
        if self.rate:
            self.speaker.setProperty('rate', self.rate)

    def read_pdf(self):
        try:
            with open(self.pdf_path, 'rb') as file:
                pdfreader = PyPDF2.PdfFileReader(file)
                text = ''
                for page_num in range(pdfreader.numPages):
                    page = pdfreader.getPage(page_num)
                    text += page.extractText()
                return text
        except FileNotFoundError:
            print(f"Error: File '{self.pdf_path}' not found.")
            return None

    def convert_to_audio(self, text):
        clean_text = text.strip().replace('\n', ' ')
        self.speaker.save_to_file(clean_text, self.output_path)
        self.speaker.runAndWait()

    def stop_speaker(self):
        self.speaker.stop()

    def convert(self):
        self.configure_speaker()
        text = self.read_pdf()
        if text:
            self.convert_to_audio(text)
        self.stop_speaker()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert PDF to Audio')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('output_path', help='Path to save the output MP3 file')
    parser.add_argument('--voice_id', type=int, help='Voice ID for the speaker', default=None)
    parser.add_argument('--rate', type=int, help='Speech rate', default=None)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    converter = PDFToAudioConverter(args.pdf_path, args.output_path, args.voice_id, args.rate)
    converter.convert()
