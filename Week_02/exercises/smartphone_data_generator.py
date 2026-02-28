# Smartphone Data Simulation
#
# Aufgabe: Erstelle einen realistischen Datensatz mit 1000 Smartphones
# mit folgenden Variablen und exportiere ihn in eine Excel-Datei

# %% 1. Import Libraries
import os
import random
import platform
import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

print(f"Current working directory: {os.getcwd()}")

# %% 2. Define Realistic Smartphone Data
# Smartphone manufacturers and their models
smartphone_brands = {
    'Apple': ['iPhone 15 Pro Max', 'iPhone 15 Pro', 'iPhone 15', 'iPhone 14 Pro', 'iPhone 14', 'iPhone SE'],
    'Samsung': ['Galaxy S24 Ultra', 'Galaxy S24+', 'Galaxy S24', 'Galaxy S23', 'Galaxy A54', 'Galaxy A34'],
    'Google': ['Pixel 8 Pro', 'Pixel 8', 'Pixel 7a', 'Pixel 7 Pro', 'Pixel 7'],
    'Xiaomi': ['13 Pro', '13', '12T Pro', 'Redmi Note 13', 'Redmi Note 12', 'POCO X5'],
    'OnePlus': ['11 Pro', '11', 'Nord 3', 'Nord CE 3', '10T'],
    'Huawei': ['P60 Pro', 'P60', 'Mate 50 Pro', 'Nova 11', 'Nova 10'],
    'Oppo': ['Find X6 Pro', 'Find X5', 'Reno 10 Pro', 'Reno 10', 'A78'],
    'Sony': ['Xperia 1 V', 'Xperia 5 V', 'Xperia 10 V']
}

print(f"Anzahl Marken: {len(smartphone_brands)}")
print(f"Marken: {', '.join(smartphone_brands.keys())}")

# %% 3. Define Parameter Ranges
# Price ranges for different brand segments (in EUR)
price_ranges = {
    'Apple': (799, 1599),
    'Samsung': (249, 1499),
    'Google': (449, 1099),
    'Xiaomi': (199, 899),
    'OnePlus': (349, 899),
    'Huawei': (299, 1199),
    'Oppo': (249, 999),
    'Sony': (699, 1399)
}

# Camera resolution ranges (megapixels)
camera_ranges = {
    'Apple': (12, 48),
    'Samsung': (12, 200),
    'Google': (12, 50),
    'Xiaomi': (48, 200),
    'OnePlus': (48, 108),
    'Huawei': (50, 200),
    'Oppo': (48, 108),
    'Sony': (12, 48)
}

# Battery life ranges (hours of screen time)
battery_ranges = {
    'Apple': (15, 29),
    'Samsung': (18, 30),
    'Google': (20, 28),
    'Xiaomi': (20, 35),
    'OnePlus': (18, 28),
    'Huawei': (20, 30),
    'Oppo': (18, 28),
    'Sony': (16, 26)
}

# Storage sizes (GB)
storage_options = [64, 128, 256, 512, 1024]

# Screen sizes (inches)
screen_sizes = [5.4, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8]

print("✓ Datenparameter definiert")

# %% 4. Generate the Dataset
print("Generiere Smartphone-Datensatz mit 1000 Einträgen...\n")

# Empty lists to store the data
make_list = []
model_list = []
price_list = []
camera_resolution_list = []
battery_life_hours_list = []
storage_size_list = []
screen_size_list = []

# Generate 1000 smartphone entries
for i in range(1000):
    # Select random brand
    make = random.choice(list(smartphone_brands.keys()))
    make_list.append(make)

    # Select random model from that brand
    model = random.choice(smartphone_brands[make])
    model_list.append(model)

    # Generate price based on brand (normal distribution within range)
    price_min, price_max = price_ranges[make]
    price_mean = (price_min + price_max) / 2
    price_std = (price_max - price_min) / 4
    price = np.clip(np.random.normal(price_mean, price_std), price_min, price_max)
    price_list.append(round(price, 2))

    # Generate camera resolution based on brand
    cam_min, cam_max = camera_ranges[make]
    camera_resolution = random.randint(cam_min, cam_max)
    camera_resolution_list.append(camera_resolution)

    # Generate battery life based on brand
    bat_min, bat_max = battery_ranges[make]
    battery_life = random.randint(bat_min, bat_max)
    battery_life_hours_list.append(battery_life)

    # Select random storage size (higher prices correlate with higher storage)
    if price > 1000:
        storage = random.choice([256, 512, 1024])
    elif price > 600:
        storage = random.choice([128, 256, 512])
    else:
        storage = random.choice([64, 128, 256])
    storage_size_list.append(storage)

    # Select random screen size
    screen_size = random.choice(screen_sizes)
    screen_size_list.append(screen_size)

print(f"✓ {len(make_list)} Smartphone-Einträge generiert")

# %% 5. Create DataFrame
# Create DataFrame
df = pd.DataFrame({
    'make': make_list,
    'model': model_list,
    'price': price_list,
    'camera_resolution': camera_resolution_list,
    'battery_life_hours': battery_life_hours_list,
    'storage_size': storage_size_list,
    'screen_size': screen_size_list
})

print("✓ DataFrame erstellt")
print(f"\nDataFrame Shape: {df.shape}")

# %% 6. Explore Data Types
# Show data types
print("\nDatentypen:")
print(df.dtypes)
print()

# Verify correct data types
print("Datentyp-Überprüfung:")
print(f"make ist string: {df['make'].dtype == 'object'}")
print(f"model ist string: {df['model'].dtype == 'object'}")
print(f"price ist float: {df['price'].dtype == 'float64'}")
print(f"camera_resolution ist int: {df['camera_resolution'].dtype in ['int64', 'int32']}")
print(f"battery_life_hours ist int: {df['battery_life_hours'].dtype in ['int64', 'int32']}")
print(f"storage_size ist int: {df['storage_size'].dtype in ['int64', 'int32']}")
print(f"screen_size ist float: {df['screen_size'].dtype == 'float64'}")

# %% 7. Display Sample Data
# Show first 10 rows
print("\nErste 10 Zeilen:")
print(df.head(10))

# Show random sample
print("\nZufällige Stichprobe (10 Zeilen):")
print(df.sample(10))

# %% 8. Basic Statistics
# Show basic statistics
print("\nDeskriptive Statistik:")
print(df.describe())

# Value counts for categorical variables
print("\nVerteilung nach Marke:")
print(df['make'].value_counts())
print(f"\nAnzahl verschiedener Modelle: {df['model'].nunique()}")

# Average price by brand
print("\nDurchschnittspreis nach Marke:")
price_by_brand = df.groupby('make')['price'].mean().sort_values(ascending=False)
print(price_by_brand.round(2))

# %% 9. Export to Excel

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('./data/smartphone_data.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object
df.to_excel(writer, sheet_name='Smartphone_Data', startrow=1, header=False, index=False)

# Get the xlsxwriter objects from the dataframe writer object
workbook = writer.book
worksheet = writer.sheets['Smartphone_Data']

# Get the dimensions of the dataframe
(max_row, max_col) = df.shape

# Create a list of column headers, to use in add_table()
column_settings = [{'header': column} for column in df.columns]

# Add the Excel table structure
worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

# Make the columns wider for clarity
worksheet.set_column(0, 0, 15)  # make
worksheet.set_column(1, 1, 25)  # model
worksheet.set_column(2, 2, 12)  # price
worksheet.set_column(3, 3, 20)  # camera_resolution
worksheet.set_column(4, 4, 20)  # battery_life_hours
worksheet.set_column(5, 5, 15)  # storage_size
worksheet.set_column(6, 6, 15)  # screen_size

print("✓ Hauptdaten-Sheet erstellt")

# %% 10. Create Additional Excel Sheets
# Create pivot table for average price by brand
pivot_table = pd.pivot_table(df[['make', 'price']],
                             index=['make'],
                             values=['price'],
                             aggfunc=np.mean)

pivot_table.to_excel(writer,
                    sheet_name='Price_Analysis',
                    startrow=0,
                    header=True,
                    index=True)

# Get worksheet for chart
worksheet2 = writer.sheets['Price_Analysis']

# Create bar chart
chart = workbook.add_chart({'type': 'column'})

# Configure the series
chart.add_series({
    'name':       '=Price_Analysis!$B$1',
    'categories': '=Price_Analysis!$A$2:$A$9',
    'values':     '=Price_Analysis!$B$2:$B$9',
})

# Add a chart title and axis labels
chart.set_title({'name': 'Durchschnittspreis nach Marke'})
chart.set_x_axis({'name': 'Marke'})
chart.set_y_axis({'name': 'Durchschnittspreis (EUR)'})

# Set an Excel chart style
chart.set_style(11)

# Insert the chart into the worksheet
worksheet2.insert_chart('D2', chart, {'x_offset': 25, 'y_offset': 10})

# Make columns wider
worksheet2.set_column(0, 1, 20)

print("✓ Preisanalyse-Sheet mit Diagramm erstellt")

# Create summary statistics sheet
summary_stats = df.describe()
summary_stats.to_excel(writer, sheet_name='Summary_Statistics')

# Get worksheet for summary
worksheet3 = writer.sheets['Summary_Statistics']
worksheet3.set_column(0, len(df.columns), 20)

print("✓ Zusammenfassende Statistik-Sheet erstellt")

# Close the Pandas Excel writer and output the Excel file
writer.close()

print(f"\n✅ Excel-Datei erfolgreich erstellt: ./data/smartphone_data.xlsx")
print(f"\nDie Excel-Datei enthält folgende Sheets:")
print("  1. Smartphone_Data - Hauptdatensatz mit 1000 Smartphones")
print("  2. Price_Analysis - Preisanalyse nach Marke mit Diagramm")
print("  3. Summary_Statistics - Deskriptive Statistik")

# %% 11. System Information
# Footer information
print('\n-----------------------------------')
print(os.name.upper())
print(platform.system(), '|', platform.release())
print('Datetime:', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
from platform import python_version
print('Python Version:', python_version())
print('Pandas Version:', pd.__version__)
print('NumPy Version:', np.__version__)
print('-----------------------------------')

print("\n✅ Aufgabe erfolgreich abgeschlossen!")

