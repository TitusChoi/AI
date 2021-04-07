# Title         : DataVisualization_anscombe.py
# Description   : Visualization

import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")
dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']
# plt.plot(dataset_1['x'], dataset_1['y'], '*')
# plt.show()

# subplot
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(dataset_1['x'], dataset_1['y'], 'o')
ax2.plot(dataset_2['x'], dataset_2['y'], 'o')
ax3.plot(dataset_3['x'], dataset_3['y'], 'o')
ax4.plot(dataset_4['x'], dataset_4['y'], 'o')

# subtitle
ax1.set_title("data_1")
ax2.set_title("data_2")
ax3.set_title("data_3")
ax4.set_title("data_4")

fig.suptitle("Anscombe")
fig.tight_layout()
plt.show()