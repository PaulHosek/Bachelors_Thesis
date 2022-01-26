from matplotlib.style import use as ms_use
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
ms_use('./apa_plot_style')  # selecting the style sheet


data = pd.read_csv('Mimimal_trials_20%_inpaper.csv', index_col=0)


mu_05 = data['0.5']
mu_10 = data['1.0']
mu_20 = data['2.0']
mu_25 = data['2.5']
x = list(range(1,101)) # trials



y = mu_25
all_vales = list(zip(x, y))






def not_all_NaN(x):
    a, b = x
    if a == nan or b == 'nan':
        return False
    else:
        return True


# regression_data = [i for i in zip(x,y) if None not in i]
# x_new, y_new = map(list, zip(*regression_data))
# a, constant = np.polyfit(np.array(x_new), np.array(y_new), 1)
# plt.plot(np.array(x_new), a * np.array(x_new) + constant)

# plt.figure()
# plt.scatter(x, mu_05, label = 0.5, marker='2')
# plt.scatter(x, mu_10, label = 1.0, marker='v')
# plt.scatter(x, mu_20, label = 2.0, marker='x')
# plt.scatter(x, mu_25, label = 2.5, marker='+')
# plt.ylabel("Least Trials")
# plt.xlabel("Threshold")
# plt.title(f'')
#
# plt.show()

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
# plt.subplots_adjust(wspace=0, hspace=0)
plt.xlim((-5, 110))
plt.ylim((-1, 26))
axs[0, 0].scatter(x,mu_05, s=7, label = '0.5')
axs[0, 0].set_title('0.5')

axs[0, 1].scatter(x,mu_10, s=7, label = '1.0')
axs[0, 1].set_title('1')

axs[1, 0].scatter(x, mu_20, s=7, label = '2.0')
axs[1, 0].set_title('2')

axs[1, 1].scatter(x, mu_25, s=7, label = '2.5')
axs[1, 1].set_title('2.5')


fig.text(0.5, 0.04, 'Threshold', ha='center', va='center', fontweight='bold')
fig.text(0.06, 0.5, 'Least trials needed for ±20% µ', ha='center', va='center', rotation='vertical', fontweight='bold')


plt.show()