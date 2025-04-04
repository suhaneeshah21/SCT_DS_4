import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from geopy.geocoders import Nominatim
import plotly.express as px
import folium
df=pd.read_csv("US_Accidents_March23(filtered).csv")
print(df.head())

from geopy.geocoders import Nominatim
import plotly.express as px
import folium

plt.figure(figsize=(10,6))
heatmap_data = pd.crosstab(df['Weather_Condition'], df['Severity'])
sns.heatmap(heatmap_data,cmap='crest', fmt='d')
plt.xlabel("Accident Severity")
plt.ylabel("Weather Conditions")
plt.title("Heatmap of Accident Severity by Weather Conditions")



df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")
df["Hour"] = df["Start_Time"].dt.hour
df["Time_of_Day"] = df["Hour"].apply(lambda x: "Night" if x < 6 or x > 18 else "Day")
plt.figure(figsize=(8, 5))
sns.countplot(x="Time_of_Day", hue="Severity", data=df)
plt.xlabel("Time of Day")
plt.ylabel("Accident Count")
plt.title("Accident Severity by Time of Day")



plt.figure(figsize=(10, 5))
ax=sns.scatterplot(x="Visibility(mi)", y="Severity", data=df, alpha=0.5)
ax.annotate("More severe accidents when visibility is low",
            xy=(2, 3), xytext=(5, 3.5),
            arrowprops=dict(facecolor="red", shrink=0.05),
            fontsize=12, color="red")
plt.xlabel("Visibility (miles)")
plt.ylabel("Accident Severity")
plt.title("Visibility vs. Severity of Accidents")

plt.show(block=False)




state_accidents = df.groupby("State").size().reset_index(name="Accident Count")
fig = px.choropleth(state_accidents,
                    locations="State",
                    locationmode="USA-states",
                    color="Accident Count",
                    color_continuous_scale="Reds",
                    title="Accident Hotspots in the US")
fig.update_layout(geo_scope='usa')
fig.show()

plt.figure(figsize=(12, 6))
sns.countplot(y="Weather_Condition", hue="Severity", data=df,
              order=df["Weather_Condition"].value_counts().index[:10], palette="coolwarm")
plt.xlabel("Count of Accidents")
plt.ylabel("Weather Condition")
plt.title("Accident Severity Distribution by Weather Conditions")
plt.legend(title="Severity")
plt.show()
