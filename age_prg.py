import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data into a pandas DataFrame
df = pd.read_csv('epl.csv')

# Slice the dataframe to exclude the first row
df = df.iloc[1:]

# Convert the 'Progression' and 'Unnamed: 2' columns to numeric data types
df['Progression'] = pd.to_numeric(df['Progression'])
df['Unnamed: 2'] = pd.to_numeric(df['Unnamed: 2'])

# Sort the dataframe by the 'Progression' column
df = df.sort_values('Progression')

# Create a scatter plot with progressive carries on the x-axis and age on the y-axis
sns.regplot(x='Progression', y='Unnamed: 2', data=df)

# Add labels to the points
for i, row in df.iterrows():
    plt.text(row['Progression'], row['Unnamed: 2'], row['Unnamed: 0'])

# Add labels to the x-axis and y-axis
plt.xlabel('Progressive Carries')
plt.ylabel('Age')

# Add a title to the plot
plt.title('EPL Teams: Progressive Carries vs Age')

# Show the plot
plt.show()
