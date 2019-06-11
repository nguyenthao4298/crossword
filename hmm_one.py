import librosa
import hmmlearn.hmm as hmm
import numpy as np
import pickle

def get_mfcc(filename):
  data, fs = librosa.load(filename, sr=None)
  mfcc = librosa.feature.mfcc(data, fs, hop_length=128, n_fft=1024)
  return mfcc.T


all_mfcc = [get_mfcc('five_{}.wav'.format(i))for i in range(1,15)]

model_five = hmm.GaussianHMM(n_components=30, n_iter=200, verbose=True)
# print(model_up)
# print([mfcc.shape for mfcc in all_mfcc])

model_five.fit(X=np.vstack(all_mfcc), lengths=[mfcc.shape[0] for mfcc in all_mfcc])
filename = 'five.sav'
pickle.dump(model_five, open(filename, 'wb'))
