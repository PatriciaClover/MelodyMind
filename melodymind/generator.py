"""
MelodyMind Generator
--------------------
This module provides functionality to generate a melody based on a text prompt.
"""

import torch
import random
from pathlib import Path
from pretty_midi import PrettyMIDI, Instrument, Note

# Placeholder for a trained model (to be replaced with an actual implementation)
MODEL_PATH = Path(__file__).parent / "model" / "trained_model.pt"

def load_model():
    if MODEL_PATH.exists():
        print(f"Loading model from {MODEL_PATH}")
        # model = torch.load(MODEL_PATH)  # Replace with real model loading
        model = "stub-model"  # Placeholder
        return model
    else:
        raise FileNotFoundError("Trained model not found. Please train or provide a model in melodymind/model/")

def generate_notes_from_prompt(prompt, seed=42):
    """
    Dummy implementation: generate a fixed pattern of notes for demonstration.
    Replace this with AI-based melody generation logic.
    """
    print(f"Generating melody for prompt: '{prompt}'")

    random.seed(seed)
    num_notes = 8
    start_time = 0.0
    duration = 0.5

    notes = []
    for _ in range(num_notes):
        pitch = random.randint(60, 72)  # MIDI pitches for C4 to C5
        velocity = random.randint(80, 100)
        note = Note(
            velocity=velocity,
            pitch=pitch,
            start=start_time,
            end=start_time + duration
        )
        notes.append(note)
        start_time += duration

    return notes

def generate_melody(prompt, output_path="output.mid"):
    """
    Generates a MIDI file based on the given prompt.
    """
    # Load model (currently a placeholder)
    _ = load_model()

    # Generate notes
    notes = generate_notes_from_prompt(prompt)

    # Create PrettyMIDI object
    midi = PrettyMIDI()
    instrument = Instrument(program=0)  # Acoustic Grand Piano
    instrument.notes.extend(notes)
    midi.instruments.append(instrument)

    # Save to file
    midi.write(output_path)
    print(f"Melody saved to {output_path}")
