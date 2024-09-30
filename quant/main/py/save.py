import os
import csv
def save(save):
    title = [["day","stock","price","CDP","NH","AH","NL","AL","time"]]
    file_name = "trade_log.csv"
    f = open(file_name,"a",newline="")
    w = csv.writer(f)
    if os.path.getsize(file_name)==0:
        w.writerows(title)
    w.writerows(save)
    f.close