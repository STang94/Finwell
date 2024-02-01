import pandas as pd
import math
from schedule import every, repeat, run_pending
import time
import time
from datetime import datetime, timedelta
from sms import send_sms

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

@repeat(every(1).minutes)
def job():
    print("doing job")
    # Read the CSV file into a DataFrame
    df = pd.read_csv('goldfish_positions2.csv')

    # Convert 'timestamp' column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Calculate the distance between consecutive points
    df['distance'] = df.apply(lambda row: math.sqrt((row['x2'] - row['x1'])**2 + (row['y2'] - row['y1'])**2), axis=1)
    mean_dist = df['distance'].mean()

    # Get the current time
    current_time = datetime.now()

    # Filter data from the past hour
    past_hour_data = df[df['timestamp'] > current_time - timedelta(hours=1)]

    # Calculate the mean distance for the past hour
    dist_past_hour = past_hour_data['distance'].mean()
    # Compare the mean distance of the past hour with the overall mean distance


        

    sort_y1=df.sort_values("y1",ascending=True)["y1"]
    sort_y2=df.sort_values("y2",ascending=True)["y2"]
    mean_y1=sort_y1.mean()
    mean_y2=sort_y2.mean()
    mean_hauteur=(mean_y1+mean_y2)/2

    bottom=mean_hauteur*0.3
    # Add a new column to the DataFrame based on the condition
    past_hour_data['is_below_bottom'] = (past_hour_data['y1'] + past_hour_data['y2']) / 2 < bottom

    # Display the DataFrame with the added column
    true_count = past_hour_data['is_below_bottom'].sum()
    print(dist_past_hour)
    print(true_count)
    if dist_past_hour < mean_dist *0.3 :
        send_sms("Your fish is in bad condition")
        sleep_mode = True
    if true_count > len(past_hour_data)*0.5:
        send_sms("the fish is at the bottom for a long time")
    if sleep_mode :
        time.sleep(100000)
    



while True:
    run_pending()
    time.sleep(1)

