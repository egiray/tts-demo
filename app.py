#!/usr/bin/env python3
"""
Interactive Multi-language Text-to-Speech
Supports English and Turkish
"""

from TTS.api import TTS
import subprocess
import sys

MODELS = {
    "1": {
        "name": "Multilingual (xtts_v2)",
        "model": "tts_models/multilingual/multi-dataset/xtts_v2",
        "sample": "This is a test of a multilingual model."
    },
    "2": {
        "name": "Multilingual (your_tts)",
        "model": "tts_models/multilingual/multi-dataset/your_tts",
        "sample": "This is a test of a multilingual model."
    },
    "3": {
        "name": "English (ljspeech/vits)",
        "model": "tts_models/en/ljspeech/vits",
        "sample": "Hello! This is a text to speech demonstration."
    },
    "4": {
        "name": "English (vctk/vits)",
        "model": "tts_models/en/vctk/vits",
        "sample": "This is a multi-speaker English model."
    },
    "5": {
        "name": "English (jenny/jenny)",
        "model": "tts_models/en/jenny/jenny",
        "sample": "This is an expressive English model."
    },
    "6": {
        "name": "Spanish (mai/tacotron2-DDC)",
        "model": "tts_models/es/mai/tacotron2-DDC",
        "sample": "Hola, esta es una demostración de texto a voz."
    },
    "7": {
        "name": "French (mai/tacotron2-DDC)",
        "model": "tts_models/fr/mai/tacotron2-DDC",
        "sample": "Bonjour, ceci est une démonstration de la synthèse vocale."
    },
    "8": {
        "name": "German (thorsten/vits)",
        "model": "tts_models/de/thorsten/vits",
        "sample": "Hallo, dies ist eine Demonstration von Text zu Sprache."
    },
    "9": {
        "name": "Japanese (kokoro/tacotron2-DDC)",
        "model": "tts_models/ja/kokoro/tacotron2-DDC",
        "sample": "こんにちは、これはテキスト読み上げのデモンストレーションです。"
    },
    "10": {
        "name": "Chinese (baker/tacotron2-DDC-GST)",
        "model": "tts_models/zh-CN/baker/tacotron2-DDC-GST",
        "sample": "你好，这是一个文字转语音的演示。"
    }
}

def main():
    print("=" * 60)
    print("Multi-language Text-to-Speech")
    print("=" * 60)
    print("\nAvailable models:")
    for code, info in MODELS.items():
        print(f"  {code} - {info['name']}")
        print(f"      Sample: {info['sample']}")

    # Select language
    lang_code = input("\nSelect a model (1-10): ")
    if lang_code not in MODELS:
        print("Invalid model! Defaulting to 1.")
        lang_code = "1"

    lang_info = MODELS[lang_code]
    print(f"\n✓ Selected: {lang_info['name']}")

    # Load model
    print(f"\nLoading {lang_info['name']} TTS model...")
    print("(First time may download the model)")
    tts = TTS(lang_info['model'])
    print("✓ Model loaded!\n")

    # Interactive loop
    while True:
        print("-" * 60)
        text = input(f"Enter text (or 'quit' to exit):\n> ")

        if text.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! / Hoşça kal!")
            break

        if not text.strip():
            print("Please enter some text!")
            continue

        output_file = f"output.wav"
        print(f"\n🎤 Generating speech...")
        tts.tts_to_file(text=text, file_path=output_file)
        print(f"✓ Audio saved to: {output_file}")
        print("🔊 Playing audio...")
        subprocess.run(["afplay", output_file])
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye! / Hoşça kal!")
        sys.exit(0)
