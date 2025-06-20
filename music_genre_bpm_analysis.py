import pandas as pd

# Load the dataset
df = pd.read_csv("top10s.csv", encoding='latin1')

# Show first few rows
print(df[['title', 'artist', 'top genre', 'year', "bpm"]].head())

# Get the top 5 genres 
print(df.value_counts('top genre').head(5))

top_5_genres = ['dance pop', 'pop', 'canadian pop', 'boy band', 'barbadian pop']

# Filter our data 
filtered_df = df[df['top genre'].isin(top_5_genres)]

print(filtered_df.groupby('top genre')['bpm'].mean())

# Start visualizing data
import matplotlib.pyplot as plt

# Store the grouped bpm in a variable
avg_bpm = filtered_df.groupby('top genre')['bpm'].mean()

# Begin plotting
plt.figure(figsize=(10, 6))  # Set figure size
avg_bpm.sort_values().plot(kind='barh', color='skyblue')  # Horizontal bar chart

# Add labels and title
plt.xlabel("Average BPM")
plt.ylabel("Top Genre")
plt.title("Average BPM by Top 5 Genres (2010–2019)")

# Show the chart
plt.tight_layout()
plt.show()
