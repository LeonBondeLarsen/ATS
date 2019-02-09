#!/bin/zsh

# Force audio output to 3.5mm jack
amixer cset name='PCM Playback Route' 1
amixer set PCM 0dB
