import soundfile as sf
import sounddevice as sd

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
sf.write('noisy_rec.wav', fs, myrecording)  # Save as WAV file
data, fs = sf.read('noisy_rec.wav')
sd.play(data*20,fs)
