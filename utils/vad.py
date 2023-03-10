import os
import torch


torch.set_num_threads(1)

class VAD():
    """Wrapper class to ease the making and using of the silero-vad model."""
    def __init__(self, force_reload=False):
        ## Silero VAD Model
        vad_model, utils =    torch.hub.load(repo_or_dir='snakers4/silero-vad',
                                    model='silero_vad',
                                    force_reload=force_reload,
                                    onnx=False)

        self._model = vad_model
        self.utils = utils

    
    def get_speech_timestamps(self, audio):
        vad_segments = self.utils[0](audio, self._model)
        return vad_segments