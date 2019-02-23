
import csv
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import time

import parameters
from scipy.io import wavfile
from scipy import signal
import numpy as np

"""Plots
Time in MS Vs Amplitude in DB of a input wav signal
"""

import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.io import wavfile
from scipy.fftpack import fft


import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


from scipy.io import wavfile
from scipy import signal
import numpy as np

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('try.wav')

frequencies, times, spectrogram = signal.spectrogram(samples[1:100], sample_rate)

#plt.pcolormesh(times, frequencies, spectrogram)
#plt.imshow(spectrogram)
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.show()