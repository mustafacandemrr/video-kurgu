#!/usr/bin/env bash
# Video kurgu araçlarını kurar: FFmpeg, yt-dlp, Whisper, HyperFrames
set -e
if ! command -v ffmpeg >/dev/null; then
  if command -v apt-get >/dev/null; then sudo apt-get update && sudo apt-get install -y ffmpeg
  elif command -v brew >/dev/null; then brew install ffmpeg
  else echo "FFmpeg'i elle kurun: https://ffmpeg.org/download.html"; exit 1; fi
fi
python3 -m pip install -U yt-dlp openai-whisper
# HyperFrames için Node.js 22+ gerekir
npm install -g hyperframes
echo "Kurulum bitti. Kontrol için: ./kontrol.sh"
