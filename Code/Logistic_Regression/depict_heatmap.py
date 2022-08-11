from array import array
from sklearn import metrics
import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

confusionMatrix = [[37,35],[27,91]]
print(confusionMatrix)

sns.heatmap(confusionMatrix,annot=True)

plt.show()