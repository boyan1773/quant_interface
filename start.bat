@echo off

cd %cd%\quant
start chrome --kiosk 127.0.0.1:8000
py manage.py runserver
pause