import pandas as pd
from os.path import dirname, join
from matplotlib.style import use as ms_use

import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import seaborn as sns
ms_use('./apa_plot_style')  # selecting the style sheet


script_dir = dirname(__file__)
LR_path = join(script_dir, 'files/Learning_rates_data.csv')  # lr from the yellow sheets
all_est_ez_path = join(script_dir, 'all_easy_estimates_V2.csv')
all_est_diff_path = join(script_dir, 'all_difficult_estimates_V2.csv')

with open(LR_path) as file:
    learning_rates = pd.read_csv(file, sep=',', index_col="Index")



with open(join(script_dir, 'FAT_both_02_V2.csv')) as file:
    FAT_data = pd.read_csv(file, sep=',', index_col="Unnamed: 0", usecols=['FAT_x', 'FAT_y', 'Unnamed: 0']) \
        .rename(columns={"FAT_x": "simple", "FAT_y": "complex"})



# def bootstrap(data, n=1000, func=np.mean):
#     """
#     Generate `n` bootstrap samples, evaluating `func`
#     at each resampling. `bootstrap` returns a function,
#     which can be called to obtain confidence intervals
#     of interest.
#     """
#     simulations = list()
#     sample_size = len(data)
#     xbar_init = np.mean(data)
#     for c in range(n):
#         itersample = np.random.choice(data, size=sample_size, replace=True)
#         simulations.append(func(itersample))
#     simulations.sort()
#     def ci(p):
#         """
#         Return 2-sided symmetric confidence interval specified
#         by p.
#         """
#         u_pval = (1+p)/2.
#         l_pval = (1-u_pval)
#         l_indx = int(np.floor(n*l_pval))
#         u_indx = int(np.floor(n*u_pval))
#         return(simulations[l_indx],simulations[u_indx])
#     return(ci)
#
# boot = bootstrap(data=FAT_data['simple'].dropna())
# cintervals =  [boot(i) for i in [.95]]
#
# print(cintervals)

print(FAT_data)
print(FAT_data.simple.mean(), 'simple', FAT_data.simple.std())
print(FAT_data.complex.mean(), 'complex', FAT_data.complex.std())



plt.figure()
sns.histplot(data=FAT_data['complex'], kde=True, label= 'high')
sns.histplot(data=FAT_data['simple'], kde=True, color='darkgrey', label='low')
plt.legend(title='Threshold')
plt.xlabel('Least trials needed for ±20% µ')
plt.ylabel('Number of Participants')
plt.xlim((1,6))
plt.show()


# fig, axs = plt.subplots(1, 2, figsize=(10,4))
# sns.histplot(data=FAT_data ,ax=axs[0], palette=['grey', 'dimgrey'], kde=True)
# sns.violinplot(data=FAT_data ,ax=axs[1], color='white', inner=None)
# sns.swarmplot(data=FAT_data ,ax=axs[1])
#
# # plt.xlabel('Least trials needed for ±20% µ')
# fig[0].ylabel('Number of Participants')
# # axs[0].set_title('1')
#
#
# fig.text(0.5, 0.04, 'Threshold', ha='center', va='center', fontweight='bold')
# fig.text(0.06, 0.5, 'Least trials needed for ±20% µ', ha='center', va='center', rotation='vertical', fontweight='bold')
#
#
# plt.show()


# print(FAT_data)
# diff = FAT_data['complex'].dropna()
# ez = FAT_data['simple'].dropna()
# ##### !!!!!!! IS STILL ON ± 40 % !!!!!
#
# print(diff)
# fig, axs = plt.subplots()
#
# xticklabels = ['Easy', 'Difficult']
# axs.set_xticks([1, 2])
# axs.set_xticklabels(xticklabels)
#
# axs.violinplot(dataset=[ez,diff], showmeans=True)
# plt.show()

# FAT_data.violinplot(labels=['Easy','Difficult'])
# # plt.scatter()
# plt.show()


# fig, ax = plt.subplots()
# FAT_data.boxplot('difficult_fat', by='difficult_fat')
# plt.show()
