import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv('cleaned.csv')
print(df.head())
print(df.info())

#removing unwanted columns
df.drop('Vehicle_driver_relation',axis=1,inplace=True)

#Cheking for unique values of columns
print(df['Age_band_of_driver'].unique())
print(df['Road_surface_type'].unique())
print(df['Light_conditions'].unique())
print(df['Weather_conditions'].unique())

#Encoding data
from sklearn.preprocessing import LabelEncoder
lbe=LabelEncoder()
df['Road_surface_type']=lbe.fit_transform(df['Road_surface_type'])
df['Light_conditions']=lbe.fit_transform(df['Light_conditions'])
df['Weather_conditions']=lbe.fit_transform(df['Weather_conditions'])
df['Age']=lbe.fit_transform(df['Age_band_of_driver'])
df.drop('Age_band_of_driver',axis=1,inplace=True)

#visualizing realationship between different features

sns.countplot(x='Age', hue='Accident_severity', data=df)
plt.xlabel("Age Group")
plt.ylabel("Accident Count")
plt.title("Accident Severity by Age Group")
plt.legend(title="Severity")
plt.xticks(rotation=45)


sns.countplot(x='Light_conditions', hue='Accident_severity', data=df)
plt.xlabel("Light conditions")
plt.ylabel("Accident Count")
plt.title("Accident Severity by Light conditions")
plt.legend(title="Severity")
plt.xticks(rotation=45)
# plt.show()

plt.figure(figsize=(10,6))
heatmap_data = pd.crosstab(df['Road_surface_type'], df['Accident_severity'])
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='d')
plt.xlabel("Road surface type")
plt.ylabel("Weather Conditions")
plt.title("Heatmap of Accident Severity by Road surface type")
# plt.show()

plt.figure(figsize=(10,6))
heatmap_data = pd.crosstab(df['Weather_conditions'], df['Accident_severity'])
sns.heatmap(heatmap_data, annot=True, cmap='crest', fmt='d')
plt.xlabel("Accident Severity")
plt.ylabel("Weather Conditions")
plt.title("Heatmap of Accident Severity by Weather Conditions")


plt.show()

