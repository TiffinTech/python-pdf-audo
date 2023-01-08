# python-pdf-audio

## Prerequisites

Some IDE might be helpfull e.g.: VS Code or PyCharm.

You need espeak, ffmpeg, pipenv and vorbis-tools installed on your Computer.

### MscOS

```bash
brew install espeak ffmpeg pipenv vorbis-tools
```

## Install

```bash
export PIPENV_VENV_IN_PROJECT=1
pipenv install pyttsx3 PyPDF2
```

### Run from shell

```bash
source .venv/bin/activate
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