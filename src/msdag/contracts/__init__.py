"""Shared contracts every plugin imports. Bump API_VERSION on change."""

from msdag.contracts.backend import SynthesisBackend, PLUGIN_META
from msdag.contracts.types import Utterance, SpeakerProfile, RenderJob

__all__ = [
    "SynthesisBackend",
    "PLUGIN_META",
    "Utterance",
    "SpeakerProfile",
    "RenderJob",
]