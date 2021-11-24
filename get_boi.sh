#!/bin/bash

python3 get_boi.py >boi_src.txt

rm -rf boi_pics_full/*.png
mkdir boi_pics_full
cd boi_pics_full
cat ../boi_src.txt | while read f; do curl "${f}" -O; done;

