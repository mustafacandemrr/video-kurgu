#!/usr/bin/env bash
# Metni Türkçe seslendirir ve altyazı (.srt) üretir. Karakter sınırı yok.
# Kullanım: ./seslendir.sh hikaye.txt [kadin|erkek] [hiz, örn. +10%]
set -e
[ -f "$1" ] || { echo "Kullanım: ./seslendir.sh hikaye.txt [kadin|erkek] [+10%]"; exit 1; }
ses=tr-TR-EmelNeural; [ "$2" = erkek ] && ses=tr-TR-AhmetNeural
hiz="${3:-+0%}"; ad="${1%.*}"
edge-tts ${HTTPS_PROXY:+--proxy "$HTTPS_PROXY"} --voice "$ses" --rate="$hiz" \
  -f "$1" --write-media "$ad.mp3" --write-subtitles "$ad.srt"
echo "Hazır: $ad.mp3 ve $ad.srt"
