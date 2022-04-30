#! /bin/bash

git clone https://github.com/SwinTransformer/Swin-Transformer-Object-Detection
cd Swin-Transformer-Object-Detection
python3 -m pip install -r requirements/build.txt
pip install -v -e .

cd ..
python3 script.py