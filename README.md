# python-pdf-audio

## Prerequisites

Some IDE might be helpful e.g.: [VS Code](https://code.visualstudio.com/download), [PyCharm](https://www.jetbrains.com/de-de/pycharm/download/), [google it](https://www.google.com/search?q=python+editors) or search yourself with your favorite search engine.

You need espeak, ffmpeg, pipenv and vorbis-tools installed on your Computer.

### MacOS

```bash
brew install espeak ffmpeg pipenv vorbis-tools
```

### Ubuntu

```bash
sudo apt install espeak ffmpeg vorbis-tools
pip install pipenv
```

## Install

```bash
export PIPENV_VENV_IN_PROJECT=1
pipenv install pyttsx3 PyPDF2
```

### Run from shell

```bash
pipenv shell
python main.py
```

### Check environment

```bash
pipenv --venv
```

pip cache purge

## Weblinks

* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [pyttsx3](https://pypi.org/project/pyttsx3/)
* [Automating My Life with Python: The Ultimate Guide | Code With Me](https://youtu.be/LXsdt6RMNfY)