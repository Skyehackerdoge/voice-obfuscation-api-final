import numpy as np
import librosa
from scipy.signal import butter, lfilter
import random

class VoiceTransformer:

    def __init__(self, sample_rate: int):
        self.sample_rate = sample_rate

    def transform(self, y: np.ndarray):
        """
        Apply controlled transformations.
        Enough to break speaker identity,
        but preserve intelligibility.
        """

        # 1️⃣ Subtle pitch shift (not extreme)
        y = self._controlled_pitch_shift(y)

        # 2️⃣ Micro pitch modulation (breaks voiceprint consistency)
        y = self._micro_pitch_modulation(y)

        # 3️⃣ Slight spectral tilt instead of heavy smoothing
        y = self._spectral_tilt(y)

        # 4️⃣ Normalize output
        y = self._normalize(y)

        return y

    # ------------------------------------------------

    def _controlled_pitch_shift(self, y):
        # Keep it small to preserve clarity
        steps = random.uniform(-1.5, 1.5)
        return librosa.effects.pitch_shift(
            y, sr=self.sample_rate, n_steps=steps
        )

    def _micro_pitch_modulation(self, y):
        """
        Adds very small frequency perturbations
        to break embedding consistency.
        """
        noise = 0.003 * np.random.randn(len(y))
        return y + noise

    def _spectral_tilt(self, y):
        """
        Instead of low-pass filtering (which muffles),
        apply a gentle high-shelf reduction.
        """
        cutoff = 6000  # less aggressive
        nyq = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyq
        b, a = butter(2, normal_cutoff, btype="low", analog=False)
        return lfilter(b, a, y)

    def _normalize(self, y):
        return librosa.util.normalize(y)
