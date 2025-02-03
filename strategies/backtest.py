import os
import pandas as pd

# Get the absolute path to data/sample_data.csv
file_path = os.path.join(os.path.dirname(__file__), "../data/sample_data.csv")

# Load data
data = pd.read_csv(file_path)
