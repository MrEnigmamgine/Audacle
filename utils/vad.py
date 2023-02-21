import os
import torch


torch.set_num_threads(1)
models_dir = './models'


class VAD():
    """Wrapper class to ease the making and using of the silero-vad model."""
    def __init__(self):
        ## Silero VAD Model
        silero_dir = os.path.join(models_dir, 'silero-vad')
        vad_model, utils =    torch.hub.load(repo_or_dir=silero_dir,
                                    source='local',
                                    model='silero_vad',
                                    force_reload=True,
                                    onnx=False)

        self._model = vad_model
        self.utils = utils

    
    def get_speech_timestamps(self, audio):
        vad_segments = self.utils[0](audio, self._model)
        return vad_segments