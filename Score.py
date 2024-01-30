import pandas as pd
import math

# Read the CSV file into a DataFrame
df = pd.read_csv('goldfish_positions.csv')

# Calculate the distance between consecutive points
df['distance'] = df.apply(lambda row: math.sqrt((row['x2'] - row['x1'])**2 + (row['y2'] - row['y1'])**2), axis=1)

# Display the DataFrame with the added 'distance' column
print(df)
