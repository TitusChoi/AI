# Title         : [Python]DataVisualization_tips.py
# Description   : Visualization

import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore') # version warning ignore!

tips = sns.load_dataset("tips")
print(tips.head())

# # 1. histogram graph
# histogram_plot = plt.figure()
# ax = histogram_plot.add_subplot(1,1,1)
# ax.hist(tips['total_bill'], bins = 10)
# ax.set_title('History of Total Bill')
# ax.set_xlabel('Frequency')
# ax.set_ylabel('Total Bill')
# plt.show()

# # 2. scatter plot
# scatter_plot = plt.figure()
# ax = scatter_plot.add_subplot(1,1,1)
# ax.scatter(tips['total_bill'], tips['tip'])
# ax.set_title('Scatterplot of Total Bill vs Tip')
# ax.set_xlabel('Total Bill')
# ax.set_ylabel('Tip')
# plt.show()

# 3. multi-scatter plot
def record_sex(sex) :
    if sex == 'Female':
        return False
    else:
        return True

tips['sex_color'] = tips['sex'].apply(record_sex)
scatter_plot = plt.figure()
ax = scatter_plot.add_subplot(1,1,1)
ax.scatter(
    x = tips['total_bill'],
    y = tips['tip'],
    s = tips['size']*10,        # s = 점의 크기
    c = tips['sex_color'],      # c = 점의 색상
    alpha = 0.5                 # alpha = 투명도
)

ax.set_title('Total Bill vs Tip Colored by Sex and Sized by Size')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
plt.show()