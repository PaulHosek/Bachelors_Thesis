import pandas as pd
from os.path import dirname, join
from matplotlib.style import use as ms_use

import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import seaborn as sns

from matplotlib.style import use as ms_use

ms_use('./apa_plot_style')  # selecting the style sheet

#  # fully averages
# script_dir = dirname(__file__)
# ez_slopes_path = join(script_dir, 'easy_slopes_thirds.csv')
# diff_slopes_path = join(script_dir, 'difficult_slopes_thirds.csv')
# with open(ez_slopes_path) as file1, open(diff_slopes_path) as file2:
#     easy_slopes_thirds = pd.read_csv(file1, sep=',', index_col="Unnamed: 0")
#     difficult_slopes_thirds = pd.read_csv(file2, sep=',', index_col="Unnamed: 0")
# data_low = pd.concat([easy_slopes_thirds['lower_avg'], difficult_slopes_thirds['lower_avg']], axis=1, )
# data_middle = pd.concat([easy_slopes_thirds['middle_avg'], difficult_slopes_thirds['middle_avg']], axis=1, )
# data_upper = pd.concat([easy_slopes_thirds['upper_avg'], difficult_slopes_thirds['upper_avg']], axis=1, )
#
# fig, axs = plt.subplots(3,1,sharey=True)
# axs[0].plot(data_low)
# axs[1].plot(data_middle)
# axs[2].plot(data_upper)
# plt.show()

# non-fully average


script_dir = dirname(__file__)

# lower
with open(join(script_dir, 'all_Est_slopes_easy_low_V2.csv')) as easy_f, open(join(script_dir,
                                                                                      'all_Est_slopes_diff_low_V2.csv')) as difficult_f:
    low_ez = pd.read_csv(easy_f, sep=',', index_col="Unnamed: 0")
    low_difficult = pd.read_csv(difficult_f, sep=',', index_col="Unnamed: 0")
# middle
with open(join(script_dir, 'all_Est_slopes_easy_mid_V2.csv')) as easy_f, open(join(script_dir,
                                                                                      'all_Est_slopes_diff_mid_V2.csv')) as difficult_f:
    mid_ez = pd.read_csv(easy_f, sep=',', index_col="Unnamed: 0")
    mid_difficult = pd.read_csv(difficult_f, sep=',', index_col="Unnamed: 0")
# upper
with open(join(script_dir, 'all_Est_slopes_easy_upper_V2.csv')) as easy_f, open(join(script_dir,
                                                                                        'all_Est_slopes_diff_upper_V2.csv')) as difficult_f:
    upper_ez = pd.read_csv(easy_f, sep=',', index_col="Unnamed: 0")
    upper_difficult = pd.read_csv(difficult_f, sep=',', index_col="Unnamed: 0")

# print(low_difficult.T.reset_index())
# low_difficult = low_difficult.drop('')

# low_difficult.drop(columns='lower_avg', inplace=True)
# ld_new = low_difficult.T.reset_index().rename(columns={'index':'Subject'})
# ld_new['Subject'] = ld_new['Subject'].astype(str)
# some = ld_new.melt(id_vars='Subject', var_name='Trial', value_name='Estimate')
# some['Subject'] = some['Subject'].astype(str)

# some_new = some.pivot(index='Trial', columns='Subject', values='Estimate')
# print(some_new.columns)
# print(some_new)
def single_line(data, drop_column):
    data.drop(columns=drop_column, inplace=True)
    data_new = data.T.reset_index().rename(columns={'index': 'Subject'})
    data_new['Subject'] = data_new['Subject'].astype(str)
    this_line = data_new.melt(id_vars='Subject', var_name='Trial', value_name='Estimate')
    this_line['Subject'] = this_line['Subject'].astype(str)
    return this_line

l_d = single_line(data=low_difficult, drop_column='lower_avg')
l_e = single_line(data=low_ez, drop_column='lower_avg')

m_d = single_line(data=mid_difficult, drop_column='middle_avg')
m_e = single_line(data=mid_ez, drop_column='middle_avg')

u_d = single_line(data=upper_difficult, drop_column='upper_avg')
u_e = single_line(data=upper_ez, drop_column='upper_avg')


# low plot
fig, axs = plt.subplots(1, 3, sharex=True, sharey=True, tight_layout=True,  figsize=(12,4))



sns.lineplot(data=l_d, x='Trial', y='Estimate', ax=axs[0], alpha=1, color='red')
sns.lineplot(data=l_e, x='Trial', y='Estimate', ax=axs[0], alpha = 1, color='black', linestyle = 'dashed')
# mid plot

sns.lineplot(data=m_d, x='Trial', y='Estimate', ax=axs[1], alpha=1, color='red')
sns.lineplot(data=m_e, x='Trial', y='Estimate', ax=axs[1], alpha = 1, color='black', linestyle = 'dashed')

# upper plot
sns.lineplot(data=u_d, x='Trial', y='Estimate', ax=axs[2], alpha=1, color='red')
sns.lineplot(data=u_e, x='Trial', y='Estimate', ax=axs[2], alpha = 1, color='black', linestyle = 'dashed')

axs[2].legend(labels=['high', 'low'], title='Threshold')
axs[0].set_ylabel('         ')  # add whitespace on the left
axs[0].set_title('lower tercile', fontsize='12')
axs[1].set_title('middle tercile', fontsize='12')
axs[2].set_title('upper tercile', fontsize='12')
for i in range(3):
    axs[i].set_xlim([0,9])
    axs[i].set_ylim([0, 2])
    axs[i].set_aspect(aspect=5, adjustable='box', )
    axs[i].set_xlabel('  ')
fig.text(0.5, 0.04, 'Trials', ha='center', va='center', fontweight='bold', fontsize='12')
fig.text(0.05, 0.5, 'Deviation from µ', ha='center', va='center', rotation='vertical', fontweight='bold', fontsize='12')
fig.canvas.draw()

labels = [item.get_text() for item in axs[0].get_yticklabels()]
labels = [str(int(float(i)*100))+ '%'   for i in labels]
axs[0].set_yticklabels(labels)



plt.show()


# single plots
#
# plt.figure()
# sns.lineplot(data=l_d, x='Trial', y='Estimate')
# sns.lineplot(data=l_e, x='Trial', y='Estimate')
# plt.show()
#
# plt.figure()
# sns.lineplot(data=m_d, x='Trial', y='Estimate')
# sns.lineplot(data=m_e, x='Trial', y='Estimate')
# plt.show()
#
# plt.figure()
# sns.lineplot(data=u_d, x='Trial', y='Estimate')
# sns.lineplot(data=u_e, x='Trial', y='Estimate')
# plt.show()
