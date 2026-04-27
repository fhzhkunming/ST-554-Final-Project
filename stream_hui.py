
################################
# Author: Hui Fang
# Purpose: ST 554 Final Project
# Date: 4/23/2026
################################

import pandas as pd
import time
import os

# print("Current working directory:", os.getcwd())

# 1. Ensure the input directory exists
input_dir = 'stream_input'
if not os.path.exists(input_dir):
    os.makedirs(input_dir)

# 2. Clear existing files in the stream_input directory
for f in os.listdir(input_dir):
    path = os.path.join(input_dir, f)
    if os.path.isfile(path):
        os.remove(path)
    else:
        continue

# 3. Load the full streaming dataset
df = pd.read_csv("https://www4.stat.ncsu.edu/~online/datasets/power_streaming_data.csv")

# 4. wait for Spark to start watching
time.sleep(10)

# 5. randomly sample new files
for i in range(20):
    sample = df.sample(n = 5)                                             # sample 5 rows
    sample.to_csv(f"stream_input/sample_{i}.csv", index = False)         # write the sample file to input folder
    time.sleep(15)                                                        # pause 10 seconds between outputs

print("Starting data generation...")

