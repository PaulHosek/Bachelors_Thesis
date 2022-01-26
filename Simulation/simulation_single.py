import numpy as np
import math
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from random import randint
import pandas as pd


# LOW LR (1), High LR (2)
# # LOW THRESHOLD (1), High Threshold (1.5) # murre 2014 >1 is elevated, found 1,5 in difficult tasks
# trials = 15
# def LL(params, data):
#     (learning_rate, learning_time, threshold) = params
#     (x, y) = data
#     residual = y - (1-stats.poisson.cdf(mu_t, threshold))
#     likelihoods = stats.norm.pdf(residual, 0, 1)
#     return -np.sum(np.log(likelihoods))

# all_data = {}
# all_lr = {'Low LR':1,'High LR':2}
# all_th = {'Low TH':1,'High TH':1.5}
# for key_th,value_th in all_th.items():
#     threshold = value_th
#     all_estimates_this_trial = []
#     for key_lr,value_lr in all_lr.items(): # TODO implement this
#
#         learning_rate = value_lr
#         learning_time = np.arange(1,16,1) # trials, x axis
#         mu_t = learning_time * learning_rate
#         mcm_function = 1-stats.poisson.cdf(mu_t, threshold)
#
#         all_y = mcm_function + stats.norm.rvs(size=15)
#         y_sofar = []
#         for i in all_y:
#             y_sofar += i # incrementing trial by 1
#             x_sofar = len(y_sofar)
#             #fit model
#             estimate = minimize(LL, x0=[4,4], args=[x_sofar, y_sofar, threshold], method='Nelder-Mead')
#             all_estimates_this_trial.append(estimate['x'])
#
#     all_data[(key_th,key_lr)] =  all_estimates_this_trial
# print(all_data)

# def max_to_1(y):
#     new_y = []
#     for i in y:
#         if i >=1:
#             new_y.append(1)
#             break
#         else:
#             new_y.append(i)
#
#     return new_y


low lr = 0.4, high lr = 1
low b = 1, high b = 3

# TODO should i take 20 trials and orient on modeled learning curve in Murre 2014?
# what values make most sense


# TODO Jaap suggested increaseing Threshold by **2 every run




# def LL(params, data):
#     (mu_est, sigma) = params
#     (x, y) = data
#     residual = y - (1 - stats.poisson.cdf(b, mu_est * this_x))
#     likelihoods = stats.norm.pdf(residual, 0, sigma)
#     return -np.sum(np.log(likelihoods))


def f_mcm(mu_est, P, b):
    return 1 - stats.poisson.cdf(b, mu_est * P)


def sim_single(trials: int, mu: float, b: int, out='list', margin=0.2):
    P = np.arange(1, trials + 1, 1)  # [1,2,3...,n]
    y = stats.poisson.cdf(b, mu * P + stats.norm.rvs(scale=0.5, loc=0, size=trials))
    all_est = []
    for i in range(1, len(y) + 1):
        nr_trials_used = i
        this_y = y[:nr_trials_used]
        this_x = np.arange(1, len(this_y) + 1, 1)

        def LL(params, data):  # note this function depends on "this x"
            (mu_est, sigma) = params
            (this_x, this_y) = data
            residual = this_y - (stats.poisson.cdf(b, mu_est * this_x))
            likelihoods = stats.norm.pdf(residual, 0, sigma)
            return -np.sum(np.log(likelihoods))

        output = minimize(LL, x0=[5, 0.3], args=[this_x, this_y], method='Nelder-Mead')
        est = output['x']
        all_est.append(est[0])

    lower_bound = mu * (1 + margin)
    upper_bound = mu * (1 - margin)
    if out == 'list':
        return all_est
    else:
        # return index of first item that is within bounds
        return all_est.index(next((t for t in all_est if (t < upper_bound) and t > lower_bound), None))


# return index of first accurate estimate if there is one
def first_indx_in_margin(all_estimates):
    try:
        return all_estimates.index(next((t for t in all_estimates if (t < 1.2) and t > 0.8), None))
    except ValueError:
        return None


def single_lr_range_th(learning_rate):
    th_list = []
    for threshold in range(1, 101):
        # all estimates of that b
        all_estimates = sim_single(trials=100, mu=learning_rate, b=threshold, out='list')
        # append only the first inx in 20% criteria
        th_list.append(first_indx_in_margin(all_estimates))
        # returns list of first trial within margin
    return th_list

def all_learing_rates(learning_rates: list):
    trials = 100
    all_data = pd.DataFrame()
    for mu in learning_rates:
        data_mu = single_lr_range_th(learning_rate=mu)
        all_data[mu] = data_mu
        print(data_mu)
        print(mu)
    all_data.to_csv('Mimimal_trials_20%_14_jan.csv')



def plot_all(th_list, mu):
    x = range(1, len(th_list) + 1, 1)
    y = th_list
    all_vales = list(zip(x, y))
    regression_data = list(filter(lambda x: all(i != None for i in x), all_vales))
    x_new, y_new = map(list, zip(*regression_data))

    plt.figure()
    plt.scatter(x, y, color='green')

    a, constant = np.polyfit(np.array(x_new), np.array(y_new), 1)
    plt.plot(np.array(x_new), a * np.array(x_new) + constant)
    plt.ylabel("Trials minimally needed for ±20% from true Learning rate")
    plt.xlabel("Threshold")
    plt.title(f'Learning Rate: {mu}')
    plt.show()



# learning_rates = [0.5, 1, 2, 2.5]
# all_learing_rates(learning_rates=learning_rates)

plt.figure()
# for thresh in range(1,100):

# for lr in [0.2, 0.3, 2, 2.1]:
#     teestset = f_mcm(mu_est=lr, P=15,b=2) # should converge immediately, took out noise
#     # x = range(1, len(teestset) + 1, 1)
#     x = range(15)
#     y = teestset
#     print(lr)
#     plt.plot(x,y)
# plt.legend()
# plt.show()



plt single curve
P_global = np.arange(1, trials + 1, 1)
mcm_thisTh = f_mcm(mu_est=mu, b=threshold, P=P_global)
plt.figure()
plt.scatter(P_global, mcm_thisTh, alpha=0.5)
plt.plot(range(1, len(all_estimates) + 1, 1), all_estimates, color='green')
plt.title(f'Threshold: {threshold}')
plt.axhline(mu, label="True mu", linestyle='--')
plt.axhline(mu * 1.2, label="True mu", linestyle='--')
plt.axhline(mu * 0.8, label="True mu", linestyle='--')
plt.show()