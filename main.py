import pyttsx3
import PyPDF2
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from typing import List, Union, Optional



# ============================================================
# TTS ENGINE INITIALIZATION
# ============================================================

def init_engine(rate: int = 150, volume: float = 1.0, voice: Optional[str] = None):
    """Initialize and configure the text-to-speech engine with validated settings."""
    engine = pyttsx3.init()

    # Validate & clamp
    rate = max(60, min(rate, 450))
    volume = max(0.0, min(volume, 1.0))

    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    if voice:
        try:
            engine.setProperty("voice", voice)
        except Exception:
            print(f"[!] Invalid voice '{voice}', using default.")

    return engine



# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_text_from_pdf(pdf_source: Union[str, bytes]) -> List[str]:
    """
    Accepts either a file path or raw PDF bytes.
    Returns: List of cleaned page text strings.
    """
    try:
        if isinstance(pdf_source, str):
            with open(pdf_source, "rb") as f:
                reader = PyPDF2.PdfReader(f)
        else:
            reader = PyPDF2.PdfReader(BytesIO(pdf_source))

        pages = []
        for page in reader.pages:
            raw = page.extract_text() or ""
            cleaned = " ".join(raw.split())
            pages.append(cleaned)

        if not pages:
            print("[!] PDF contains no text.")
        return pages

    except FileNotFoundError:
        print(f"[!] PDF not found: {pdf_source}")
    except Exception as e:
        print(f"[!] PDF extraction error: {e}")

    return []



# ============================================================
# AUDIO GENERATION
# ============================================================

def save_audio(
    text: str,
    filename: str,
    rate: int = 150,
    volume: float = 1.0,
    voice: Optional[str] = None
) -> bool:
    """Convert text → speech and save as an audio file."""
    if not text.strip():
        print("[!] Cannot generate audio from empty text.")
        return False

    try:
        engine = init_engine(rate, volume, voice)
        engine.save_to_file(text, filename)
        engine.runAndWait()
        engine.stop()
        print(f"[✓] Audio saved: {filename}")
        return True
    except Exception as e:
        print(f"[!] Failed to save audio: {e}")
        return False



# ============================================================
# MAIN PDF → AUDIO
# ============================================================

def read_pdf_and_speak(
    pdf_path: str = "book.pdf",
    output_filename: str = "story.mp3",
    rate: int = 150,
    volume: float = 1.0,
    voice: Optional[str] = None,
):
    pages = extract_text_from_pdf(pdf_path)
    if not pages:
        return

    combined = " ".join(pages)
    print(f"[i] Pages extracted: {len(pages)}")
    print("[i] Sample:", combined[:200], "...")

    save_audio(combined, output_filename, rate, volume, voice)



def split_audio_by_page(
    pdf_path: str = "book.pdf",
    output_prefix: str = "page_",
    rate: int = 150,
    volume: float = 1.0,
    voice: Optional[str] = None,
):
    pages = extract_text_from_pdf(pdf_path)
    if not pages:
        return

    for i, page_text in enumerate(pages, start=1):
        filename = f"{output_prefix}{i}.mp3"
        save_audio(page_text, filename, rate, volume, voice)



# ============================================================
# PAGE SELECTION UTILITIES
# ============================================================

def parse_page_selection(selection: Union[str, List[int], None], total: int) -> List[int]:
    """Parses page selections like '1-4,7' or [1, 3] into a validated list."""
    if selection is None:
        return list(range(1, total + 1))

    if isinstance(selection, list):
        return sorted({p for p in selection if 1 <= p <= total})

    selected = []
    try:
        for token in selection.split(","):
            token = token.strip()
            if "-" in token:
                start, end = map(int, token.split("-"))
                for p in range(start, end + 1):
                    if 1 <= p <= total:
                        selected.append(p)
            else:
                p = int(token)
                if 1 <= p <= total:
                    selected.append(p)
    except ValueError:
        print("[!] Invalid page selection syntax.")
        return []

    return sorted(set(selected))



def read_specific_pages(
    pdf_path: str = "book.pdf",
    pages_to_read: Union[str, List[int], None] = None,
    output_filename: str = "selected.mp3",
    rate: int = 150,
    volume: float = 1.0,
    voice: Optional[str] = None,
):
    pages = extract_text_from_pdf(pdf_path)
    if not pages:
        return

    total = len(pages)
    chosen = parse_page_selection(pages_to_read, total)

    if not chosen:
        print("[!] No valid pages selected.")
        return

    combined = " ".join(pages[p - 1] for p in chosen)
    save_audio(combined, output_filename, rate, volume, voice)



# ============================================================
# MEMORY-BASED PDF READING
# ============================================================

def read_pdf_from_memory(
    pdf_bytes: bytes,
    output_filename: str = "memory_audio.mp3",
    rate: int = 150,
    volume: float = 1.0,
    voice: Optional[str] = None,
):
    pages = extract_text_from_pdf(pdf_bytes)
    if not pages:
        return

    combined = " ".join(pages)
    save_audio(combined, output_filename, rate, volume, voice)



# ============================================================
# AUDIO PLAYBACK
# ============================================================

def play_audio_file(audio_path: str):
    """Play an audio file using pydub."""
    try:
        audio = AudioSegment.from_file(audio_path)
        play(audio)
        print(f"[▶] Playing: {audio_path}")
    except FileNotFoundError:
        print(f"[!] Audio not found: {audio_path}")
    except Exception as e:
        print(f"[!] Playback error: {e}")



# ============================================================
# PDF UTILITIES
# ============================================================

def convert_pdf_to_text(pdf_path: str = "book.pdf", output_text_file: str = "output.txt"):
    pages = extract_text_from_pdf(pdf_path)
    if not pages:
        return

    try:
        with open(output_text_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(pages))
        print(f"[✓] Extracted text saved to: {output_text_file}")
    except Exception as e:
        print("[!] Could not save text:", e)



def get_pdf_metadata(pdf_path: str = "book.pdf"):
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            meta = reader.metadata or {}

        if not meta:
            print("[i] PDF contains no metadata.")
            return

        print("\n--- PDF Metadata ---")
        for key, value in meta.items():
            print(f"{key}: {value}")

    except FileNotFoundError:
        print(f"[!] File not found: {pdf_path}")
    except Exception as e:
        print("[!] Metadata error:", e)



# ============================================================
# VOICE INFORMATION
# ============================================================

def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")

    print("\n--- Available Voices ---")
    for i, v in enumerate(voices):
        print(f"[{i}] {v.name}  —  {v.id}")

    engine.stop()


def get_speech_engine_info():
    engine = pyttsx3.init()
    print("Speech Engine:", engine.getProperty("engine"))
    engine.stop()
