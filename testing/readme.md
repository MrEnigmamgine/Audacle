These files are artifacts created from trying to find a viable pipeline for the various features I want to include in the project.

## Whisper
OpenAI's whisper was the technology that inspired me to undertake this project in the first place.  It includes several pretrained models of various sizes, all of which seem sufficient toward accomplishing my goals.  I plan on using the smallest model available for the bulk of the transcription tasks and only bumping up the model size if the error rate causes me problems.

## Pyannote
One of the main problems I would like to solve with Whisper is that Whisper's transcription produces one wall of text with no seperation of speakers.  This makes the resulting text difficult to parse for a human.  One method I found that might be helpful in solving that is to utilize speaker diarization and using those timestamps to break the resulting text into something more resembling of a script.

However, after several days of attempting to get Pyannote to run in docker and being unsuccessful, I feel as though the dependencies for using Pyannote are too difficult to work around and not something I want to manage in the future.  I will be avoiding Pyannote unless I can't find an alternative.

## Speechbrain / Torchaudio
I am dissapointed that torchaudio is not included in the official Pytorch image.