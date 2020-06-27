#!/bin/bash

# Run in shell
cd ~/rssds/Projects/m3u-parser
python ~/rssds/Projects/m3u-parser/main.py
cp ~/rssds/Projects/m3u-parser/output/out.m3u ~/ds/video/Scripts/m3uparser/out.m3u
echo "[M3UP]: Moved out.m3u to the video scripts folder"
