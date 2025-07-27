import pandas as pd
import numpy as np

def process_data(df):
  # This function has a deliberate syntax error
  print("Processing data...")
  
  # The 'for' loop is missing a colon ':' at the end
  for index, row in df.iterrows()
    # This line will never be reached because of the error above
    processed_value = row['feature1'] * 2
    
  return df

# Create some sample data
data = {'feature1': [10, 20, 30], 'feature2': [1, 2, 3]}
my_df = pd.DataFrame(data)

# Call the function with the error
process_data(my_df)

