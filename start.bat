@echo off

<<<<<<< HEAD
=======
call %cd%\Scripts\activate
>>>>>>> 7ae95e4c65da82c73c62e44da7f7287e67fcec24
cd %cd%\quant
start chrome --kiosk 127.0.0.1:8000
py manage.py runserver
pause