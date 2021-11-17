#!/bin/bash

python3 get_boi.py >> boi_src.txt

cd boi_pics_full
cat ../boi_src.txt | while read f; do curl "${f}" -O; done;

