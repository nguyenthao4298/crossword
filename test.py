import librosa
import hmmlearn.hmm as hmm
import numpy as np
import pickle
import sounddevice as sd
import soundfile as sf
def get_mfcc(filename):
  data, fs = librosa.load(filename, sr=None)
  mfcc = librosa.feature.mfcc(data, fs, hop_length=128, n_fft=1024)
  return mfcc.T


def record_sound(filename, duration=2, fs=44100, play=False):
  print('Recording...')
  sd.play(np.sin(2*np.pi*500*np.arange(fs)/fs), samplerate=fs, blocking=True)
  sd.play(np.zeros(int(fs*0.2)), samplerate=fs, blocking=True)
  data = sd.rec(frames=duration*fs, samplerate=fs, channels=1, blocking=True)
  if play:
      sd.play(data, samplerate=fs, blocking=True)
  sf.write(filename, data=data, samplerate=fs)
  print('Done...')

choose = ['mot','hai','ba','bon','nam']
filename = ['one.sav','two.sav','three.sav','four.sav','five.sav']
loaded_model = [pickle.load(open(model, 'rb')) for model in filename]
record_sound('input.wav',1)
result = [loaded_model[i].score(get_mfcc('input.wav')) for i in range(len(loaded_model))]
print(choose[result.index(max(result))])
