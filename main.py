import pyttsx3, PyPDF2

# insert name of your pdf
pdfreader = PyPDF2.PdfReader("book.pdf")
speaker = pyttsx3.init()

for page in pdfreader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)
# name mp3 file whatever you would like
speaker.save_to_file(clean_text, "story.mp3")
speaker.runAndWait()

speaker.stop()
