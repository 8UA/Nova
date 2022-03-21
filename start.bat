@echo off
echo Starting browser...
echo:
:: Not starting with main path because icons get bugged
cd src
python main.py
echo:
PAUSE