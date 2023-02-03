from pyannote.audio import Pipeline
from env import hugging_face_token
# from pyannote.audio.pipelines import SpeakerDiarization

print('loading pipeline')
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                    use_auth_token = hugging_face_token)

print('diarizing')
diarization = pipeline("data/db short intro.ogg")
print('diarizing complete')
# for turn, _, speaker in diarization.itertracks(yield_label=True):
#     print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")

