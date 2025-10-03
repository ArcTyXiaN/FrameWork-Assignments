import pandas as pd

# Path to the full dataset
infile = "data/metadata.csv"
outfile = "data/sample_metadata.csv"

# Read only first 5000 rows for testing
df = pd.read_csv(infile, nrows=100)
df.to_csv(outfile, index=False)

print("Sample saved to", outfile, "with", len(df), "rows")
