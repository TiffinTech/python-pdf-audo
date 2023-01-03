# Prerequisites

You need espeak, ffmpeg, pipenv installed on your Computer.

Some IDE might be helpfull e.g. VS Code or PyCharm.

## MscOS

```bash
brew install espeak ffmpeg pipenv
```

# Install

```bash
export PIPENV_VENV_IN_PROJECT=1
pipenv install pyttsx3 PyPDF2
```

## Run from shell

```bash
source .venv/bin/activate
```

## Check environment

```bash
pipenv --venv
```

pip cache purge