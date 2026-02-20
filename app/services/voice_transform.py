import numpy as np
import librosa
from scipy.signal import butter, lfilter
import random

class VoiceTransformer:

    def __init__(self, sample_rate: int):
        self.sample_rate = sample_rate

    def transform(self, y: np.ndarray):
        # Apply multiple small distortions.
        # The goal is to preserve clarity but break biometric consistency.
        y = self._random_pitch_shift(y)
        y = self._random_time_stretch(y)
        y = self._spectral_smoothing(y)
        y = self._lowpass_filter(y)
        y = self._normalize(y)
        return y

    def _random_pitch_shift(self, y):
        steps = random.uniform(-3, 3)
        return librosa.effects.pitch_shift(y, sr=self.sample_rate, n_steps=steps)

    def _random_time_stretch(self, y):
        rate = random.uniform(0.9, 1.1)
        return librosa.effects.time_stretch(y, rate=rate)

    def _spectral_smoothing(self, y):
        stft = librosa.stft(y)
        magnitude, phase = np.abs(stft), np.angle(stft)
        smoothed = librosa.decompose.nn_filter(
            magnitude,
            aggregate=np.median,
            metric="cosine"
        )
        return librosa.istft(smoothed * np.exp(1j * phase))

    def _lowpass_filter(self, y):
        cutoff = 4000
        nyq = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyq
        b, a = butter(6, normal_cutoff, btype="low", analog=False)
        return lfilter(b, a, y)

    def _normalize(self, y):
        return librosa.util.normalize(y)
