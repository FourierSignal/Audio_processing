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

path_to_file = '1980s-Casio-Piano-C5.wav'
samplerate, data = wavfile.read(path_to_file)
wavefile.write('test1.wav', 44100, data)
wavefile.write('test2.wav', 44100, data*2)
sd.play(data, 44100)
sd.play(data*2, 44100)
