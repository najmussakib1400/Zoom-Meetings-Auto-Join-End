import webbrowser
import time
import os
import pandas as pd
from datetime import datetime

# Reading the file and zoom path.
df = pd.read_csv('Meeting_Times.csv')
zoom_path = "C:\\Users\\Supto\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['start_times']):
        row = df.loc[df['start_times'] == now]
        m_id = str(row.iloc[0, 1])
        print("Killing Zoom")
        os.system("taskkill /f /im zoom.exe")
        print("Done")
        print("Loading Zoom")
        os.startfile(zoom_path)
        time.sleep(10)
        print("Done")
        print("Opening Meeting Url")
        webbrowser.open(m_id)
        time.sleep(5)
        print("Joined Meeting")
        break
    else:
        print("Waiting For next Meeting")
        time.sleep(30)

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['end_times']):
       row = df.loc[df['end_times'] == now]
       print("Killing Zoom Now")
       os.system("taskkill /f /im zoom.exe")
       print("Ended Meeting")
       os.system('python main.py')
       break
    else:
        print("Waiting for End Meeting Time")
        time.sleep(30)
