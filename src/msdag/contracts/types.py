"""Core dataclasses shared across the host and every plugin boundary."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True, frozen=True)
class SpeakerProfile:
    """A named voice the script can route lines to."""

    speaker_id: str
    display_name: str
    backend: str
    voice_ref: str
    language: str = "en-US"
    pitch_shift: float = 0.0
    rate: float = 1.0
    pan: float = 0.0  # -1.0 left .. 1.0 right


@dataclass(slots=True, frozen=True)
class Utterance:
    """One line of dialogue, already attributed to a speaker."""

    index: int
    speaker_id: str
    text: str
    emotion: str = "neutral"
    pause_after_ms: int = 0


@dataclass(slots=True)
class RenderJob:
    """A full render request handed to the timeline assembler."""

    script_name: str
    utterances: list[Utterance]
    speakers: dict[str, SpeakerProfile]
    output_dir: Path
    sample_rate: int = 48000
    format: str = "wav"
    metadata: dict[str, str] = field(default_factory=dict)