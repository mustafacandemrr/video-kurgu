#!/usr/bin/env bash
# Araçların kurulu olduğunu ve çalıştığını kontrol eder
ok(){ echo "✅ $1: $2"; }; bad(){ echo "❌ $1: kurulu değil"; }
command -v ffmpeg >/dev/null && ok FFmpeg "$(ffmpeg -version | head -1 | cut -d' ' -f3)" || bad FFmpeg
command -v yt-dlp >/dev/null && ok yt-dlp "$(yt-dlp --version)" || bad yt-dlp
command -v whisper >/dev/null && ok Whisper "$(python3 -c 'import whisper;print(whisper.__version__)')" || bad Whisper
command -v hyperframes >/dev/null && ok HyperFrames "$(hyperframes --version)" || bad HyperFrames
command -v node >/dev/null && ok Node.js "$(node -v)" || bad Node.js
