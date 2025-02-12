import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load risk data from CSV
data = pd.read_csv('risks.csv')

# Create a pivot table for heatmap
heatmap_data = pd.crosstab(data['Impact'], data['Probability'])

# Plot the risk matrix
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5)

# Add labels and title
plt.title('Risk Assessment Matrix')
plt.xlabel('Probability (1 - Low, 5 - High)')
plt.ylabel('Impact (1 - Low, 5 - High)')

# Save the heatmap as an image
plt.savefig('risk_matrix.png')
plt.show()
