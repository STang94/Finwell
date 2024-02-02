import pandas as pd
import math
from schedule import every, repeat, run_pending
import time
import time
from datetime import datetime, timedelta
from sms import send_sms

def convert_to_yolo_format(x1, y1, x2, y2, image_width, image_height):
    # Calculate center coordinates
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    
    # Calculate width and height
    w = x2 - x1
    h = y2 - y1
    
    # Normalize coordinates and dimensions
    x /= image_width
    y /= image_height
    w /= image_width
    h /= image_height
    
    return x, y, w, h

@repeat(every(1).minutes)
def job():
    print("doing job")
    # Read the CSV file into a DataFrame
    df = pd.read_csv('fish_positions.csv')
    # Convert bounding box coordinates to YOLO style
    df_yolo = df.apply(lambda row: pd.Series(convert_to_yolo_format(row['x1'], row['y1'], row['x2'], row['y2'], 1280, 960)), axis=1)


    # Rename the columns for clarity
    df_yolo.columns = ['x', 'y', 'w', 'h']

    # Concatenate the new DataFrame with the original DataFrame
    df = pd.concat([df, df_yolo], axis=1)
    
    print(df)

    # Convert 'timestamp' column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Calculate the distance between consecutive points
    import numpy as np
    df["x_lag"] = df["x"].shift(1)
    df["y_lag"] = df["y"].shift(1)


    df['distance']= np.sqrt((df['x']-df["x_lag"])**2+(df['y']-df["y_lag"])**2)

    mean_dist = df['distance'].mean()

    # Get the current time
    current_time = datetime.now()

    # Filter data from the past hour
    past_hour_data = df[df['timestamp'] > current_time - timedelta(hours=1)]

    # Calculate the mean distance for the past hour
    dist_past_hour = past_hour_data['distance'].mean()
    # Compare the mean distance of the past hour with the overall mean distance


        

    sort_y=df.sort_values("y",ascending=True)["y"]
    mean_hauteur=sort_y.mean()
    

    bottom=mean_hauteur*0.3
    # Add a new column to the DataFrame based on the condition
    past_hour_data['is_below_bottom'] = past_hour_data['y'] < bottom

    # Display the DataFrame with the added column
    true_count = past_hour_data['is_below_bottom'].sum()
    print(dist_past_hour)
    print(true_count)
    sleep_mode = False
    if dist_past_hour < 10000:#mean_dist *0.3 :
        #send_sms("Your fish is in bad condition")
        sleep_mode = True
        print("distance verification")
    if true_count > 1:#len(past_hour_data)*0.8:
        #send_sms("the fish is at the bottom for a long time")
        print("bottom verification")
    if sleep_mode :
        time.sleep(1)
    



while True:
    run_pending()
    time.sleep(1)

