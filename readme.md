# Audacle, the audio oracle.

The goal of this project is to process audio files and generate a searchable and summarized corpus of text aimed at answering the question "Didn't we talk about this a few weeks ago?"

Planned stuff

- AI transcription (Turning the audio into text)
    - Should include timestamps so that it's easy to find the conversation in the audio file
- Speaker Diarization or Verification (Identifying which speaker is speaking)
    - Speaker verification might be more effective than speaker diarization.  Diarization relies on clustering models which are unsupervised learning models.  With verification it becomes a supervised learning model by maintaining a list of known voice samples then for each segment asking who's voice is present.  This approach would come with the added benefit of being able to automatically label speakers by name rather than as speaker 1, speaker 2, etc.
- NLP Summarization (Summarizing the text)



Tools I plan to use
- Docker : for easy deployment and isolated dev environment
- Whisper / WhisperX : Audio transcription
- ?

## Developing in docker

I'm using vscode's devcontainer extension.  Learn more at https://code.visualstudio.com/docs/devcontainers/containers

There's a few moving parts to how I have this set up:

1. Dockerfile
    - Uses `pytorch/pytorch:1.13.1-cuda11.6-cudnn8-devel` as the base image because
        1. I'll be using Torch
        2. It has all the prerequisites for gpu-passthrough using docker
    - Installs `git` using apt-get.  Needed to install whisper from github using pip.
    - TODO: Install application requirements using requirements.txt
2. devcontainer.json
    - Uses the previous dockerfile as the base image
    - `"runArgs": ["--gpus=all"]` 
        - Docker doesn't allow access to GPU unless you tell it to when you start up the container, this line tells vscode to include the argument
    - `"postCreateCommand": "pip3 install --user -r .devcontainer/dev-reqs.txt",`
        - Installs packages that I'll use during development (mainly jupyter notebook interface) that I don't think I'll need in a production environmenet
    - Customizations
        - VScode extensions for linting and intellisense for python, as well as jupyter notebook interfaces and some other quality of life extensions.
3. Commands ran manually after launch
    - For now I'm leaving `requirements.txt` out of the dockerfile and installing them manually.  This is so that I can explore different modules and libraries without having to wait for packages that I probably won't be using to install every time I rebuild the container.