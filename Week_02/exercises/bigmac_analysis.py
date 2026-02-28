# Libraries
import warnings

import pandas as pd
from tabulate import tabulate

# Ignore warnings
warnings.filterwarnings('ignore')

# Read data to pandas data frame
df = pd.read_csv('./data/BigmacPrice.csv', sep=',')
print("Data loaded successfully!")
print(f"Total rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print("\nFirst few rows:")
print(df.head())
print("\n" + "="*80 + "\n")

# ============================================================================
# Task 3: Check how much the Big Mac prices in Switzerland have changed
#         between 2002 and 2022
# ============================================================================

# Filter data for Switzerland
df_switzerland = df[(df['name'] == 'Switzerland') &
                    ((df['date'] == '2002-04-01') | (df['date'] == '2022-07-01'))]

# Get prices
switzerland_2002 = df_switzerland[df_switzerland['date'] == '2002-04-01']['dollar_price'].values[0]
switzerland_2022 = df_switzerland[df_switzerland['date'] == '2022-07-01']['dollar_price'].values[0]

# Calculate change
switzerland_change = switzerland_2022 - switzerland_2002
switzerland_change_percent = (switzerland_change / switzerland_2002) * 100

print("="*80)
print("TASK 3: Big Mac Price Change in Switzerland (2002-2022)")
print("="*80)
print(f"Price in 2002: ${switzerland_2002:.2f}")
print(f"Price in 2022: ${switzerland_2022:.2f}")
print(f"Absolute change: ${switzerland_change:.2f}")
print(f"Percentage change: {switzerland_change_percent:.2f}%")
print("\n" + "="*80 + "\n")

# ============================================================================
# Task 4: Is the Big Mac price increase between 2002 and 2022 in Switzerland
#         higher compared to the U.S.A.?
# ============================================================================

# Filter data for USA
df_usa = df[(df['name'] == 'United States') &
            ((df['date'] == '2002-04-01') | (df['date'] == '2022-07-01'))]

# Get prices
usa_2002 = df_usa[df_usa['date'] == '2002-04-01']['dollar_price'].values[0]
usa_2022 = df_usa[df_usa['date'] == '2022-07-01']['dollar_price'].values[0]

# Calculate change
usa_change = usa_2022 - usa_2002
usa_change_percent = (usa_change / usa_2002) * 100

print("="*80)
print("TASK 4: Comparison of Big Mac Price Increase (2002-2022)")
print("="*80)

print("\n🇺🇸 USA:")
print(f"  Price in 2002: ${usa_2002:.2f}")
print(f"  Price in 2022: ${usa_2022:.2f}")
print(f"  Absolute change: ${usa_change:.2f}")
print(f"  Percentage change: {usa_change_percent:.2f}%")

print("\n🇨🇭 Switzerland:")
print(f"  Price in 2002: ${switzerland_2002:.2f}")
print(f"  Price in 2022: ${switzerland_2022:.2f}")
print(f"  Absolute change: ${switzerland_change:.2f}")
print(f"  Percentage change: {switzerland_change_percent:.2f}%")

print("\n" + "-"*80)
print("COMPARISON:")
print("-"*80)
if switzerland_change_percent > usa_change_percent:
    difference = switzerland_change_percent - usa_change_percent
    print(f"✓ Switzerland's price increase ({switzerland_change_percent:.2f}%) is HIGHER")
    print(f"  than USA's price increase ({usa_change_percent:.2f}%)")
    print(f"  Difference: {difference:.2f} percentage points")
else:
    difference = usa_change_percent - switzerland_change_percent
    print(f"✗ Switzerland's price increase ({switzerland_change_percent:.2f}%) is LOWER")
    print(f"  than USA's price increase ({usa_change_percent:.2f}%)")
    print(f"  Difference: {difference:.2f} percentage points")

print("\n" + "="*80 + "\n")

# ============================================================================
# Summary Table
# ============================================================================

# Create a nice comparison table
comparison_data = {
    'Country': ['Switzerland', 'United States'],
    'Price 2002 ($)': [switzerland_2002, usa_2002],
    'Price 2022 ($)': [switzerland_2022, usa_2022],
    'Absolute Change ($)': [switzerland_change, usa_change],
    'Change (%)': [f"{switzerland_change_percent:.2f}%", f"{usa_change_percent:.2f}%"]
}

comparison_df = pd.DataFrame(comparison_data)
print("SUMMARY TABLE:")
print("="*80)
print(tabulate(comparison_df, headers='keys', tablefmt='grid', showindex=False))
print("="*80)

# Additional insight
print("\n💡 CONCLUSION:")
print("-"*80)
if switzerland_change_percent > usa_change_percent:
    print("Switzerland experienced a HIGHER price increase than the USA.")
else:
    print("The USA experienced a MUCH HIGHER price increase than Switzerland.")
    print("This indicates stronger inflation for Big Mac prices in the USA")
    print("compared to Switzerland over the 20-year period.")
print("="*80)

