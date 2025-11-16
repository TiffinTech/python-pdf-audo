PDF-to-Speech Converter

A lightweight Python utility for converting PDF documents into spoken audio using the pyttsx3 text-to-speech engine. The module supports full-document reading, page-specific extraction, in-memory PDF processing, audio splitting per page, and basic PDF metadata inspection. It is designed to be reliable, extensible, and easy to integrate into larger applications, including audiobook generators, accessibility tools, and content automation workflows.


---

Features

Convert any PDF to an audio file (MP3 or WAV)

Read specific pages using ranges like "1-3,7,10-12"

Split audio by page, generating one file per page

Extract text from a PDF (file or bytes)

Generate audio from raw text

Play audio files directly

Fetch PDF metadata (title, author, creation date, etc.)

List available system voices

Fully customizable speech rate, volume, and voice selection



---

Requirements

Python 3.8+

Install dependencies:

pip install pyttsx3 PyPDF2 pydub

pydub requires FFmpeg for audio playback:

Windows: Download from https://ffmpeg.org

macOS (Homebrew):

brew install ffmpeg

Linux (Debian/Ubuntu):

sudo apt install ffmpeg



---

Usage Overview

Convert an entire PDF to audio

read_pdf_and_speak("book.pdf", "book.mp3")

Split audio by page

split_audio_by_page("book.pdf", output_prefix="page_")

Read only specific pages

read_specific_pages("book.pdf", "1-3,10", "selected.mp3")

Process a PDF from memory

with open("book.pdf", "rb") as f:
    data = f.read()

read_pdf_from_memory(data, "memory_audio.mp3")

Play an audio file

play_audio_file("story.mp3")

Extract text only

convert_pdf_to_text("book.pdf", "output.txt")

View available voices

get_available_voices()


---

Project Structure

pdf_tts/
│
├── TTS engine setup
├── PDF text extraction
├── Audio generation utilities
├── Page-specific reading
├── In-memory PDF processing
├── Audio playback
├── Metadata utilities
└── Voice information helpers

Each section is modular and can be used independently.


---

Notes

Output format depends on the filename extension (e.g., .mp3, .wav).

Text extraction quality depends on the PDF’s internal structure.

Speech output quality varies by the system’s installed voices.



---

License

This project is provided as-is and may be freely used, modified, or integrated into other applications.


---

If you’d like, I can also generate:

✔ A more polished or branded version
✔ A Markdown file with badges and formatting
✔ An installation guide
✔ Examples section with GIFs or screenshots
