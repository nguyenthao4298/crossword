import os
try:
	os.chdir(os.path.join(os.getcwd(), 'hmm'))
	print(os.getcwd())
except:
	pass

import sounddevice as sd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import librosa
import hmmlearn.hmm as hmm
from math import exp

def record_sound(filename, duration=2, fs=44100, play=False):
    sd.play( np.sin( 2*np.pi*500*np.arange(fs)/fs )  , samplerate=fs, blocking=True)
    sd.play( np.zeros( int(fs*0.2) ), samplerate=fs, blocking=True)
    data = sd.rec(frames=duration*fs, samplerate=fs, channels=1, blocking=True)
    if play:
        sd.play(data, samplerate=fs, blocking=True)
    sf.write(filename, data = data, samplerate=fs)

for i in range(15):
    record_sound("five_{}.wav".format(i+1))


