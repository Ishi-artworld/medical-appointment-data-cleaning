# ===============================
# TASK 1: DATA CLEANING
# Dataset: Medical Appointment No Shows
# ===============================

import pandas as pd
import numpy as np

# 1️⃣ Load Dataset
df = pd.read_csv("KaggleV2-May-2016.csv")

# If file error comes, use full path:
# df = pd.read_csv(r"C:\Users\YourName\Downloads\KaggleV2-May-2016.csv")

print("Dataset Loaded Successfully!\n")

# 2️⃣ Basic Information
print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nShape of Dataset:", df.shape)

# 3️⃣ Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 4️⃣ Remove Duplicate Rows
duplicates = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# 5️⃣ Clean Column Names
df.columns = df.columns.str.lower().str.replace("-", "_")

# Fix spelling mistake
df.rename(columns={'handcap': 'handicap'}, inplace=True)

# 6️⃣ Standardize Text Columns
df['gender'] = df['gender'].str.lower().str.strip()
df['neighbourhood'] = df['neighbourhood'].str.title()

# 7️⃣ Convert Date Columns to Datetime
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# 8️⃣ Fix Data Types
df['age'] = df['age'].astype(int)

# Remove negative ages if any
df = df[df['age'] >= 0]

# 9️⃣ Standardize No_show Column
df['no_show'] = df['no_show'].str.lower()
df['no_show'] = df['no_show'].replace({'yes': 1, 'no': 0})

# 🔟 Final Check
print("\nAfter Cleaning:")
print(df.info())
print("\nNew Shape:", df.shape)

# 1️⃣1️⃣ Save Cleaned Dataset
df.to_csv("medical_appointment_cleaned.csv", index=False)

print("\n✅ Cleaning Completed Successfully!")
print("Cleaned file saved as: medical_appointment_cleaned.csv")
