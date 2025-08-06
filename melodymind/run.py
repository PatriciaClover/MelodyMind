import argparse
from melodymind import generate_melody

def main():
    parser = argparse.ArgumentParser(description="🎼 MelodyMind: AI-Powered Melody Generator")
    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Describe the mood, genre, or feeling (e.g., 'melancholy piano piece')"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.mid",
        help="Filename for the output MIDI file (default: output.mid)"
    )

    args = parser.parse_args()

    print("🎶 Starting MelodyMind...")
    generate_melody(prompt=args.prompt, output_path=args.output)
    print("✅ Done! Open the file in your DAW or MIDI viewer to listen.")

if __name__ == "__main__":
    main()
