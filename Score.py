import pandas as pd
import math
import schedule
import time
from datetime import datetime, timedelta
def job():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('generated_data.csv')

    # Calculate the distance between consecutive points
    df['distance'] = df.apply(lambda row: math.sqrt((row['x2'] - row['x1'])**2 + (row['y2'] - row['y1'])**2), axis=1)
    mean_dist = df['distance'].mean()
    # Display the DataFrame with the added 'distance' column
    comparison = False
    

import pandas as pd
import math
from datetime import datetime, timedelta

# Read the CSV file into a DataFrame
df = pd.read_csv('generated_data.csv')

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
print(mean_dist)
print(dist_past_hour)
# Compare the mean distance of the past hour with the overall mean distance
if dist_past_hour > mean_dist * 0.6:
    print("Good condition")
else:
    print("Bad condition")

sort_y1=df.sort_values("y1",ascending=True)["y1"]
sort_y2=df.sort_values("y2",ascending=True)["y2"]
mean_y1=sort_y1.mean()
mean_y2=sort_y2.mean()
mean_hauteur=(mean_y1+mean_y2)/2

bottom=mean_hauteur*0.3
# Add a new column to the DataFrame based on the condition
past_hour_data['is_below_bottom'] = (past_hour_data['y1'] + past_hour_data['y2']) / 2 < bottom

# Display the DataFrame with the added column
print(past_hour_data)
true_count = past_hour_data['is_below_bottom'].sum()
print(true_count)
if true_count < len(past_hour_data)*0.5:
    print("the fish is at the bottom for a long time")
"""
while True:
    schedule.every().hour.at(":00").do(job)
"""
