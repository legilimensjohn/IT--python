import sounddevice as sd
from scipy.io.wavfile import write
import wavio as mv


#sampling frequency
freq = 44100

#recording duration - you can modify
duration = 5

recording = sd.rec(int(duration * freq),
                   samplerate = freq, channels = 2)

sd.wait()

wv.write("recording1.wa", recording, freq, sampwidth = 2)
