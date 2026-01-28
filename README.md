# Text-to-Speech Demo

A simple project to test Coqui TTS (Text-to-Speech) capabilities.

## Quick Start

### Option 1: Basic Demo
Run the basic demo with pre-written text:
```bash
python3 simple_tts.py
```

This will generate `demo_output.wav` with sample speech.

### Option 2: Interactive Mode (Recommended!)
Type any text you want and hear it spoken:
```bash
python3 interactive_tts.py
```

This will load the model once, then let you type text interactively. The audio will play automatically!

## Files

- `interactive_tts.py` - Type text and hear it spoken (recommended for testing)
- `simple_tts.py` - Simple one-shot demo with pre-written text
- `demo_output.wav` - Sample output from simple_tts.py
- `output.wav` - Output from interactive mode

## Try Different Voices/Languages

Available models include:
- **Turkish**: `tts_models/tr/common-voice/glow-tts` ✅ (Downloaded, 1.02 GB)
- **English**: `tts_models/en/ljspeech/vits` ✅ (Downloaded, 146 MB)
- Spanish: `tts_models/es/css10/vits`
- French: `tts_models/fr/css10/vits`
- German: `tts_models/de/thorsten/vits`
- Japanese: `tts_models/ja/kokoro/tacotron2-DDC`
- Chinese: `tts_models/zh-CN/baker/tacotron2-DDC-GST`

**Note for Turkish:** Use lowercase text for best results (e.g., "merhaba" instead of "Merhaba")

See all models with:
```bash
tts --list_models
```

## Play the Audio

On macOS:
```bash
afplay demo_output.wav
```

## Requirements

All required packages are already installed (TTS, torch, etc.)
