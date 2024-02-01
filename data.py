import csv
import random
from datetime import datetime, timedelta
import time

def generate_random_data(timestamp):
    x1 = random.uniform(0, 400)
    y1 = random.uniform(0, 400)
    x2 = random.uniform(0, 400)
    y2 = random.uniform(0, 400)
    score = random.uniform(0, 1)
    class_label = "goldfish"
    
    return timestamp, x1, y1, x2, y2, score, class_label

def write_to_csv(filename, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Set the start timestamp to two days ago
start_timestamp = datetime.now() - timedelta(days=2)

# Set the number of seconds between data points
seconds_interval = 1

# Calculate the end timestamp (current time)
end_timestamp = datetime.now()

# Generate data every second from start_timestamp to end_timestamp
current_timestamp = start_timestamp
while current_timestamp <= end_timestamp:
    data = generate_random_data(current_timestamp)
    write_to_csv('generated_data.csv', data)
    current_timestamp += timedelta(seconds=seconds_interval)
