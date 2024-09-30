@echo off

call %cd%\Scripts\activate
cd %cd%\quant\main\py
py get_news_data.py
pause