
################################
# Author: Hui Fang
# Purpose: ST 554 Final Project
# Date: 4/23/2026
################################

import os
import time
import pandas as pd

# directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# full path to stream_input inside the project folder
input_dir = os.path.join(script_dir, "stream_input")

# 1. Ensure the input directory exists
os.makedirs(input_dir, exist_ok=True)

# 2. Clear existing files in the stream_input directory
for f in os.listdir(input_dir):
    path = os.path.join(input_dir, f)
    if os.path.isfile(path):
        os.remove(path)

# 3. Load the full streaming dataset
csv_path = os.path.join(script_dir, "power_streaming_data.csv")
df = pd.read_csv(csv_path)

print("Starting data generation...")

# 4. randomly sample new files
for i in range(20):
    sample = df.sample(n = 5)                               # sample 5 rows
    out_path = os.path.join(input_dir, f"sample_{i}.csv")   # build the full file path for the i‑th sample inside stream_input
    sample.to_csv(out_path, index = False)                  # write the sampled file to input folder
    print(f"Wrote: {out_path}")                             # print the full path of the file that was just created
    time.sleep(10)                                          # pause 10 seconds between outputs

print("Data generation completed")



