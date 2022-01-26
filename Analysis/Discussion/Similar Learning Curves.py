import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

from matplotlib.style import use as ms_use
ms_use('./apa_plot_style')  # selecting the style sheet

def f_mcm(mu_est, P, b):
    return 1 - stats.poisson.cdf(b, mu_est * P)


trials = 20
threshold = 3

P_global = np.arange(1, trials + 1, 1)


fig, axs = plt.subplots(1, 3, sharex=True, sharey=True, tight_layout=True,  figsize=(12,4))

# low plot
axs[0].scatter(P_global, f_mcm(mu_est=0.2, b=threshold, P=P_global), alpha=1, color='darkgrey')
axs[0].scatter(P_global, f_mcm(mu_est=0.3, b=threshold, P=P_global), alpha=1, marker='+', color='black')

# mid plot
axs[1].scatter(P_global, f_mcm(mu_est=1, b=threshold, P=P_global), alpha=1, color='darkgrey')
axs[1].scatter(P_global, f_mcm(mu_est=1.1, b=threshold, P=P_global), alpha=1, marker='+', color='black')

# upper plot
axs[2].scatter(P_global, f_mcm(mu_est=2, b=threshold, P=P_global), alpha=1, color='darkgrey')
axs[2].scatter(P_global, f_mcm(mu_est=2.1, b=threshold, P=P_global), alpha=1, marker='+', color='black')


axs[2].legend(labels=['µ', 'µ+0.1'], title='', loc='lower right')
axs[0].set_ylabel('         ')  # add whitespace on the left
axs[0].set_title('µ = 0.1', fontsize='12')
axs[1].set_title('µ = 1', fontsize='12')
axs[2].set_title('µ = 2', fontsize='12')
for i in range(3):
    axs[i].set_xlim([0, len(P_global)+0.5])
    axs[i].set_ylim([-0.1, 1.1])
    axs[i].set_aspect(aspect=15, adjustable='box', )
    axs[i].set_xlabel('  ')
    axs[i].xaxis.set_major_locator(MaxNLocator(integer=True))
fig.text(0.5, 0.02, 'Trials', ha='center', va='center', fontweight='bold', fontsize='12')
fig.text(0.02, 0.5, 'Proportion Correct', ha='center', va='center', rotation='vertical', fontweight='bold', fontsize='12')

plt.show()
