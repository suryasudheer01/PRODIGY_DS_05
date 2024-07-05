import pandas as pd

# Loading the dataset dataset 
df = pd.read_csv("C:/Users/hp/Desktop/accidents.csv")

# Display first few rows to understand the structure
print(df.head())

# Checking for missing values
print(df.isnull().sum())

# Handling missing or inconsistent data 
df=df.dropna(how="any")  
df

import matplotlib.pyplot as plt
import seaborn as sns

#  Visualize distribution of day of accident
sns.countplot(x='Day_of_Week', data=df)
plt.title('Distribution of Accident day')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

#Visualizing distribution of lighting condition
sns.countplot(x='Light_Conditions', data=df)
plt.title('Distribution of light conditions')
plt.xlabel('condition')
plt.ylabel('Count')
plt.show()

# Example: Summary statistics
summary_stats = df.describe()
print(summary_stats)

# Histogram of the number of casualties
sns.histplot(df['Number_of_Casualties'], bins=30)
plt.title('Distribution of Number of Casualties')
plt.show()


# Histogram of the number of vehicles involved
sns.histplot(df['Number_of_Vehicles'], bins=30)
plt.title('Distribution of Number of vehicles involved')
plt.show()


# Aggregate data to get counts of each accident severity
vehicletype_counts = df['Vehicle_Type'].value_counts()

# Plotting the pie chart of type of vehicle
plt.figure(figsize=(8, 8))
plt.pie(vehicletype_counts, labels=vehicletype_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of vehicle type')
plt.show()

##Time of accidents


df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')

# Extract the hour from the time column
df['hour'] = df['Time'].dt.hour

# Count the number of accidents per hour
accidents_per_hour = df['hour'].value_counts().sort_index()

# Plot the data
plt.figure(figsize=(10, 6))
sns.barplot(x=accidents_per_hour.index, y=accidents_per_hour.values, palette='viridis')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.title('Number of Accidents by Hour of the Day')
plt.xticks(range(24))  # Ensure x-axis shows all hours from 0 to 23
plt.show()
        



