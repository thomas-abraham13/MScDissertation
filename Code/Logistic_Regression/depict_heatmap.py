# File used to depict heat map example
# Execute: python depict_heatmap.py

import seaborn as sns
import matplotlib.pyplot as plt

confusionMatrix = [[37,35],[27,91]]
print(confusionMatrix)

x_axis_labels = ["Win","Loss"] # labels for x-axis
y_axis_labels = ["Win","Loss"] # labels for y-axis

sns.heatmap(confusionMatrix,annot=True,xticklabels=x_axis_labels, yticklabels=y_axis_labels)

plt.show()