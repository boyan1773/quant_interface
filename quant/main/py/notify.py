import requests
def line_notify(msg):
    headers = {
        "Authorization": "Bearer 1bKsy7H12IoBLfBQYV61DEMBwyjWBjTkWUGNK9hrMbI", 
    }
    msg = {'message':msg}
    requests.post("https://notify-api.line.me/api/notify",data=msg,headers=headers)