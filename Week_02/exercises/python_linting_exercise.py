"""
This is a  Python script that demonstrates how to use linting tools
to identify and fix code issues.
The script creates a simple DataFrame using the pandas library
and prints its contents.
"""
# Import libraries
import pandas as pd

# Initialize data of lists
data = pd.DataFrame({ 'Name': ['tom', 'nick', 'krish', 'jack'],
         'Age': [20, 21, 19, 18]})

# Create DataFrame
df = pd.DataFrame(data)
print(type(df))

# Print the output
print(df.head())
