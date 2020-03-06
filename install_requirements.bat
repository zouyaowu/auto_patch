@echo off
setlocal enabledelayedexpansion

set local_path=%~dp0
echo !local_path!
if not exist venv (
	echo  *** not exist venv, start to create
	call :create_venv
)
echo  *** start to install requirements
@echo.
!local_path!\venv\Scripts\pip3.exe install -r !local_path!\requirements.txt
@echo.
echo 安装结束，按任意键退出
pause>nul
exit



:create_venv
set local_path=%~dp0
python --version>nul
if %errorlevel% NEQ 0 (echo 无法启动python&&pause&&exit)
:loop
start "" /min /wait python -m venv venv
if %errorlevel% NEQ 0 (
    echo "没有安装 venv模块,启动安装"
    start "" /min /wait python !local_path!get-pip.py
    start "" /wait pip.exe install venv
	goto :loop
)
start "" /min exit .\venv\Scripts\activate.bat
if %errorlevel%==0 (
	echo 安装python虚拟环境成功
	REM 返回调用的地方
	goto :eof
) else (
	echo 安装失败
	pause
	exit
)
