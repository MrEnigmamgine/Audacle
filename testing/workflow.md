Goal: Transcribe a recording of a Dungeons and Dragons game.

Deliverables:
- Text document with labeled speakers.


Challenges:
- Processing a single session takes a long time.


Using VAD (Voice Activity Detection) has signficantly improved transcription time.  However, VAD itself can be of a long process itself.

Data Structure:
- Session
    - File
        - Segment
            - Word
            


Workflow
1. Load input data and transform it into monochannel 16khz
2. Perform VAD on input data