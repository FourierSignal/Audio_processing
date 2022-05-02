import wave 
import simpleaudio as sa


wave_read = wave.open(path_to_file, 'rb')
audio_data = wave_read.readframes(wave_read.getnframes())
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()

wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
play_obj = wave_obj.play()
play_obj.wait_done()



#scipy library 
#-------------------------

import scipy.io
from scipy.io import wavfile
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = '1980s-Casio-Piano-C5.wav'
samplerate, data = wavfile.read(path_to_file)
print(type(data))
print(data.size, data.shape[0])

#play nd-array
sd.play(data, 44100)
sd.play(data*2, 44100)

wavefile.write('test1.wav', 44100, data)
wavefile.write('test2.wav', 44100, data*2)

time = np.linspace(0., data.size, data.shape[0])
plt.plot(time, data, label="audio data")

plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()


# soundfile and sounddevice 
#-----------------------------
#play random data
import sounddevice as sd
import soundfile as sf

fs = 44100
data = np.random.uniform(-1, 1, fs)
sd.play(data, fs)

sf.write('new_file.wav', data, 44100)
data, fs = sf.read('new_file.wav', dtype='float32')  
sd.play(data, fs)
status = sd.wait()

#------------------------------------
import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
fs = 44100  # Sample rate
seconds = 3  # Duration of recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file
data, fs = sf.read('output.wav')
sd.play(data*20,fs)
