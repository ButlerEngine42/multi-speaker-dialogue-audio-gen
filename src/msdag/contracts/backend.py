"""The one ABC every synthesis backend must implement."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Protocol

import numpy as np

from msdag.contracts.types import SpeakerProfile, Utterance


class PLUGIN_META(Protocol):
    """Structural contract for plugin metadata. Loader reads these attrs."""

    name: ClassVar[str]
    version: ClassVar[str]
    api_version: ClassVar[str]


class SynthesisBackend(ABC):
    """Turns an Utterance + SpeakerProfile into a float32 mono waveform.

    Implementations MUST be safe to call concurrently from asyncio tasks
    unless they declare ``thread_safe = False``, in which case the host
    serializes calls behind a lock.
    """

    name: ClassVar[str] = "unnamed"
    version: ClassVar[str] = "0.0.0"
    api_version: ClassVar[str] = "1.4"
    thread_safe: ClassVar[bool] = True
    sample_rate: ClassVar[int] = 24000

    @abstractmethod
    async def synthesize(
        self, utterance: Utterance, speaker: SpeakerProfile
    ) -> np.ndarray:
        """Return float32 samples in [-1, 1] at ``self.sample_rate``.

        Raise ``BackendUnavailable`` if the model/voice can't be loaded;
        the host will fall back to the configured fallback backend.
        """

    async def warmup(self) -> None:
        """Optional: preload models so the first render isn't cold."""
        return None

    async def aclose(self) -> None:
        """Optional: release GPU handles, file descriptors, etc."""
        return None


class BackendUnavailable(RuntimeError):
    """Raised when a backend can't serve a request right now."""
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>