#!/bin/bash
pip install matplotlib pandas numpy
echo "Physics,Chemistry,Maths" >> MARKOMETER.csv
sleep 5
python markometer.py
