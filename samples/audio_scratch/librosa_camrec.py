# Beat tracking example
from __future__ import print_function
import librosa
import wave

# 1. Get the file path to the included audio example
filename = "in_Data/tmp.wav"

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# tmp = librosa.decompose()



