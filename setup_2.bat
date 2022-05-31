@echo off
start /b "" venv\Scripts\activate
venv\Scripts\pip install -r requirements.txt
start /b "" venv\Scripts\deactivate
echo Done. Closed commandline.
echo launch:  curse.bat.
exit /b