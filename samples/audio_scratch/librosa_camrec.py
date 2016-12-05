# Beat tracking example
from __future__ import print_function
import numpy as np
import librosa
import wave


def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# 1. Get the file path to the included audio example
filename = "in_Data/tmp.wav"

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=44100)


x = nonlin(y)


tmp = librosa.decompose.decompose(x)



