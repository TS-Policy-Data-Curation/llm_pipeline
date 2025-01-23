import pandas as pd

# Path to the Parquet file
parquet_file = "fred.parquet"

# Path to save the CSV file
csv_file = "fred.csv"

# Read the Parquet file
df = pd.read_parquet(parquet_file)

# Save the DataFrame as a CSV file
df.to_csv(csv_file, index=False)

print(f"CSV file saved to {csv_file}")