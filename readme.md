Audacle, the audio oracle.

The goal of this project is to process audio files and generate a searchable corpus of text aimed at answering the question "Didn't we talk about this a few weeks ago?"

To accomplish this I plan to incorporate the following technologies
- AI transcription (Turning the audio into text)
    - Should include timestamps so that it's easy to find the conversation in the audio file
- Speaker Diarization  (Identifying which speaker is speaking)
- NLP Summarization (Summarizing the text)


Tools I plan to use
- Docker : for easy deployment and isolated dev environment
- Whisper / WhisperX : Audio transcription
- 