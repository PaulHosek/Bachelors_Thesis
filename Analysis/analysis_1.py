import pandas as pd
from os.path import dirname, join
import numpy as np
from scipy import stats, special
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# OUT: FAT & All estimates for both levels


script_dir = dirname(__file__)
LR_path = join(script_dir, 'files/Learning_rates_data.csv')
with open(LR_path) as file:
    learning_rates = pd.read_csv(file, sep=',', index_col="Index")


def first_idx_in_margin_V2(all_estimates, mu, margin = 0.2):
    upper_bound = mu * (1 + margin)
    lower_bound = mu * (1 - margin)
    try:
        return all_estimates.index(next((t for t in all_estimates if (t < upper_bound) and t > lower_bound), None))
    except ValueError:
        return None


def est_single(mu: float, b: int, y: list, out='list', margin=0.2):
    """
    :param trials:
    :param mu:
    :param b:
    :param out: 'list' or 'margin'
    :param margin: within x%
    :return: list or trial that was in ± 20 %
    """

    all_est = []
    for i in range(1, len(y) + 1):
        nr_trials_used = i
        this_y = y[:nr_trials_used]
        this_x = np.arange(1, len(this_y) + 1, 1)

        def LL(params, data):  # note this function depends on "this_x" and "this_y"
            (mu_est, sigma) = params
            (this_x, this_y) = data
            residual = this_y - (1- stats.poisson.cdf(b, mu_est * this_x))
            likelihoods = stats.norm.pdf(residual, 0, sigma)
            return -np.sum(np.log(likelihoods))

        output = minimize(LL, x0=(0.9, 0.3), args=[this_x, this_y], method='Nelder-Mead')
        est = output['x']
        all_est.append(est[0])

    lower_bound = mu * (1 + margin)
    upper_bound = mu * (1 - margin)
    if out == 'list':
        return all_est
    else:
        # return index of first item that is within bounds
        return all_est.index(next((t for t in all_est if (t < upper_bound) and t > lower_bound), None))


def all_est_ez(script_dir = dirname(__file__)):
    with open(LR_path) as file:
        learning_rates = pd.read_csv(file, sep=',', index_col="Index")
    all_est_sbjw = dict()
    b = 2.529460986 # threshold easy
    ez_path = join(script_dir, 'files/FIN_All_easy_trials_rev.csv')
    with open(ez_path) as file:
        easy = pd.read_csv(file, sep=',', index_col='Unnamed: 0')
    bad_sbj_ez = [176228, 176780]
    clean_ez = easy[~easy['Subject'].isin(bad_sbj_ez)]
    unique_subjects = set(clean_ez['Subject'].tolist())  # 36 items
    for subject in unique_subjects:
        data_sbj = clean_ez[clean_ez['Subject'] == subject]
        y = data_sbj['correct'].tolist()
        mu_sbj = learning_rates[learning_rates['Subject'] == subject]['mu_easy'].iloc[0]
        estimates_sbj = est_single(mu=mu_sbj, b=b, y=y)
        all_est_sbjw[subject] = pd.Series(estimates_sbj)

    return pd.DataFrame.from_dict(all_est_sbjw)


def all_est_diff(script_dir = dirname(__file__)):
    with open(LR_path) as file:
        learning_rates = pd.read_csv(file, sep=',', index_col="Index")
    all_est_sbjw = dict()
    b = 3.526238298 # threshold difficult
    diff_path = join(script_dir, 'files/FIN_All_difficult_trials_rev.csv')
    with open(diff_path) as file:
        difficult = pd.read_csv(file, sep=',', index_col='Unnamed: 0')
    bad_subjs_dif = [177294] # model fit rejected
    clean_diff = difficult[~difficult['Subject'].isin(bad_subjs_dif)]
    unique_subjects = set(clean_diff['Subject'].tolist())  # 38 items
    for subject in unique_subjects:
        data_sbj = clean_diff[clean_diff['Subject'] == subject]
        y = data_sbj['correct'].tolist()
        mu_sbj = learning_rates[learning_rates['Subject'] == subject]['mu_diff'].iloc[0]
        estimates_sbj = est_single(mu=mu_sbj, b=b, y=y)
        all_est_sbjw[subject] = pd.Series(estimates_sbj)

    return pd.DataFrame.from_dict(all_est_sbjw)



all_est_ez().to_csv("all_easy_estimates_V2.csv")
all_est_diff().to_csv("all_difficult_estimates_V2.csv")

def gen_FAT(level, ests = all_est_ez() ):
    data = []
    with open(LR_path) as file:
        learning_rates = pd.read_csv(file, sep=',', index_col="Index")
    for subject in ests.keys():
        all_est_sbj = ests[subject].tolist()
        mu_sbj = learning_rates[learning_rates['Subject'] == subject][level].iloc[0]
        fist_index_acc_trial = first_idx_in_margin_V2(all_est_sbj,mu=mu_sbj, margin=0.2)
        # if type(fist_index_acc_trial) != None:
        #     first_acc_trial = fist_index_acc_trial +1
        # else:

        first_acc_trial = fist_index_acc_trial +1 if type(fist_index_acc_trial) != type(None) else None
        data.append({'Subject': subject, 'FAT': first_acc_trial,'Level':level})

    some = pd.DataFrame(data)
    return some


easy_FAT = gen_FAT(ests=all_est_ez(), level='mu_easy')
diff_FAT = gen_FAT(ests=all_est_diff(), level='mu_diff')




print(easy_FAT.mean(), 'simple', easy_FAT.std())
print(diff_FAT.mean(), 'complex', diff_FAT.std())
def bootstrap(data, n=1000, func=np.mean):
    """
    Generate `n` bootstrap samples, evaluating `func`
    at each resampling. `bootstrap` returns a function,
    which can be called to obtain confidence intervals
    of interest.
    """
    simulations = list()
    sample_size = len(data)
    xbar_init = np.mean(data)
    for c in range(n):
        itersample = np.random.choice(data, size=sample_size, replace=True)
        simulations.append(func(itersample))
    simulations.sort()
    def ci(p):
        """
        Return 2-sided symmetric confidence interval specified
        by p.
        """
        u_pval = (1+p)/2.
        l_pval = (1-u_pval)
        l_indx = int(np.floor(n*l_pval))
        u_indx = int(np.floor(n*u_pval))
        return(simulations[l_indx],simulations[u_indx])
    return(ci)

for i in range(10):
    boot = bootstrap(data=easy_FAT.FAT.dropna())
    cintervals =  [boot(i) for i in [.95]]

    print(cintervals)

    boot = bootstrap(data=diff_FAT.FAT.dropna())
    cintervals =  [boot(i) for i in [.95]]

    print(cintervals)




both = easy_FAT.merge(diff_FAT, on='Subject', how='outer') # loosing subjects here!
both.to_csv("FAT_both_02_V2.csv")

print('done')



# 2753446

