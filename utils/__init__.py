import os, re

from .vad import VAD
from .asr import ASR
from .alignment import Aligner
from . import audio
from . import audacity
from . import prepare

SR = 16_000

def frame_to_srt_timestamp(frame, rate=SR):
    ms, remainder = divmod(frame, SR/1000)
    sec, ms = divmod(ms, 1000)
    min, sec = divmod(sec, 60)
    hr, min = divmod(min, 60)
    return f"{int(hr):02d}:{int(min):02d}:{int(sec):02d},{int(ms):03d}"

def get_discord_name(filename):
    discord_name_pattern = r'.+-(.*)\..+'
    username = re.search(discord_name_pattern, filename).group(1)
    return username


