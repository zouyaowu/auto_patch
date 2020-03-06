@echo off
setlocal enabledelayedexpansion


set local_path=%~dp0
echo !local_path!
if exist venv (
	!local_path!\venv\Scripts\pip3.exe freeze>!local_path!\requirements.txt
) else (echo not venv && pause && exit)
exit
