import collections
import time
import re
import csv
import matplotlib.pyplot as plt
import numpy as np
import eloTrials as e

PRED1=e.func1()

plt.plot(PRED1,label="Elo Algorithm")
plt.xlabel("MATCH NUMBER")
plt.ylabel("PREDICTION RATE")
plt.legend()
plt.title("NBA Regular Season 2018-19")
plt.show()