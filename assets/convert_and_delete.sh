#!/bin/bash
for i in *.wav; do oggenc "$i" -q 6 -o "`basename "$i".wav` .ogg"&&rm "$i" ; done;
