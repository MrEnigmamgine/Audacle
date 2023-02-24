import os
import torch.cuda
import numpy as np
import whisper

from typing import Optional, Tuple, Union, TYPE_CHECKING

DEVICE = "cuda" if torch.cuda.is_available() else 'cpu'
models_dir = './models'

# Whisper ASR Model
whisper_dir = os.path.join(models_dir, 'whisper')


class ASR():

    def __init__(self, model_name= 'medium.en'):
        self.model = whisper.load_model(model_name, download_root= whisper_dir, device=DEVICE)

    def transcribe(self, 
                   audio: Union[str, np.ndarray, torch.Tensor],
                   *,
                   verbose: Optional[bool] = None,
                   condition_on_previous_text: bool = False,
                   ):
        results = whisper.transcribe(self.model, audio,
                           verbose=verbose,
                           condition_on_previous_text=condition_on_previous_text
                           )
        return results