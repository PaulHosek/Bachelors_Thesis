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
LR_path = join(script_dir, 'files/Learning_rates_data.csv')
all_est_ez_path = join(script_dir, 'all_easy_estimates_V2.csv')
all_est_diff_path = join(script_dir, 'all_difficult_estimates_V2.csv')

with open(LR_path) as file:
    learning_rates = pd.read_csv(file, sep=',', index_col="Index")


def which_third(some_list, your_number):
    if float(your_number) > (np.quantile(some_list, (2 / 3))):
        return 3
    elif float(your_number) > np.quantile(some_list, (1 / 3)):
        return 2
    else:
        return 1

# easy data
with open(all_est_ez_path) as ez_file, open(all_est_diff_path) as diff_file:
    easy_data = pd.read_csv(ez_file, sep=',', index_col='Unnamed: 0')
    difficult_data = pd.read_csv(diff_file, sep=',', index_col='Unnamed: 0')



def easy_est_slopes(ez_data, fully_avg=True):
    with open(LR_path) as file:
        learning_rates = pd.read_csv(file, sep=',', index_col="Index")

    # compute "thirds" columns
    learning_rates['ez_third'] = list(map(lambda x: which_third(learning_rates['mu_easy'], x), learning_rates['mu_easy']))
    print('These are the LR means for this list:\n', learning_rates.groupby('ez_third').mean())


    # absolute deviation of estimates from true learning rate over trials
    abs_ez = ez_data.abs()
    abs_dev_ez_dict = {}
    for subject_id in abs_ez.keys():
        ests = abs_ez[str(subject_id)]
        mu_sbj = learning_rates[learning_rates['Subject'] == int(subject_id)]['mu_easy'].iloc[0]
        abs_dev_ez_sbj = mu_sbj - ests
        abs_dev_ez_dict[subject_id] = abs_dev_ez_sbj
    abs_dev_ez = pd.DataFrame().from_dict(abs_dev_ez_dict).abs()

    # now I want the columns that are in lower third in a plot


    subjects_estimates_ez = set(map(int, abs_ez.columns.tolist()))
    # complicated way to remove the same bad subjects as for the main analysis and convert subject-ids to strings
    lower_third_ez_sbjs = list(map(str, (set(learning_rates[learning_rates['ez_third'] == 1]['Subject']).intersection(subjects_estimates_ez))))
    middle_third_ez_sbjs = list(map(str, (set(learning_rates[learning_rates['ez_third'] == 2]['Subject']).intersection(subjects_estimates_ez))))
    upper_third_ez_sbjs = list(map(str, (set(learning_rates[learning_rates['ez_third'] == 3]['Subject']).intersection(subjects_estimates_ez))))



    lower_ez_final = abs_dev_ez[lower_third_ez_sbjs]
    middle_ez_final = abs_dev_ez[middle_third_ez_sbjs]
    upper_ez_final = abs_dev_ez[upper_third_ez_sbjs]

    lower_ez_final['lower_avg'] = lower_ez_final.mean(axis=1)
    middle_ez_final['middle_avg'] = middle_ez_final.mean(axis=1)
    upper_ez_final['upper_avg'] = upper_ez_final.mean(axis=1)

    averages = [lower_ez_final['lower_avg'], middle_ez_final['middle_avg'],upper_ez_final['upper_avg'] ]
    ez_estimation_curves = pd.concat(averages, axis=1)

    if fully_avg:
        return ez_estimation_curves
    else:
        return lower_ez_final, middle_ez_final, upper_ez_final


def difficult_est_slopes(diff_data, fully_avg=True):
    with open(LR_path) as file:
        learning_rates = pd.read_csv(file, sep=',', index_col="Index")

    # compute "thirds" columns
    learning_rates['diff_third'] = list(map(lambda x: which_third(learning_rates['mu_diff'], x), learning_rates['mu_diff']))

    print('These are the LR means for this list:\n', learning_rates.groupby('diff_third').mean())

    # absolute deviation of estimates from true learning rate over trials
    abs_diff = diff_data.abs()
    abs_dev_diff_dict = {}
    for subject_id in abs_diff.keys():
        ests = abs_diff[str(subject_id)]
        mu_sbj = learning_rates[learning_rates['Subject'] == int(subject_id)]['mu_diff'].iloc[0]
        abs_dev_diff_sbj = mu_sbj - ests
        abs_dev_diff_dict[subject_id] = abs_dev_diff_sbj
    abs_dev_diff = pd.DataFrame().from_dict(abs_dev_diff_dict).abs()

    # now I want the columns that are in lower third in a plot

    subjects_estimates_diff = set(map(int, abs_diff.columns.tolist()))
    # complicated way to remove the same bad subjects as for the main analysis and convert subject-ids to strings
    lower_third_diff_sbjs = list(
        map(str, (set(learning_rates[learning_rates['diff_third'] == 1]['Subject']).intersection(subjects_estimates_diff))))
    middle_third_diff_sbjs = list(
        map(str, (set(learning_rates[learning_rates['diff_third'] == 2]['Subject']).intersection(subjects_estimates_diff))))
    upper_third_diff_sbjs = list(
        map(str, (set(learning_rates[learning_rates['diff_third'] == 3]['Subject']).intersection(subjects_estimates_diff))))

    lower_diff_final = abs_dev_diff[lower_third_diff_sbjs]
    middle_diff_final = abs_dev_diff[middle_third_diff_sbjs]
    upper_diff_final = abs_dev_diff[upper_third_diff_sbjs]

    lower_diff_final['lower_avg'] = lower_diff_final.mean(axis=1)
    middle_diff_final['middle_avg'] = middle_diff_final.mean(axis=1)
    upper_diff_final['upper_avg'] = upper_diff_final.mean(axis=1)

    averages = [lower_diff_final['lower_avg'], middle_diff_final['middle_avg'], upper_diff_final['upper_avg']]
    diff_estimation_curves = pd.concat(averages, axis=1)
    if fully_avg:
        return diff_estimation_curves
    else:
        return (lower_diff_final, middle_diff_final, upper_diff_final)


# easy_slopes = easy_est_slopes(ez_data=easy_data, fully_avg=True)
# difficult_slopes = difficult_est_slopes(diff_data=difficult_data, fully_avg=True)
#
# easy_slopes.to_csv('easy_slopes_thirds.csv')
# difficult_slopes.to_csv('difficult_slopes_thirds.csv')

all_slopes_easy_low, all_slopes_easy_mid, all_slopes_easy_upper = easy_est_slopes(ez_data=easy_data, fully_avg=False)
all_slopes_easy_low.to_csv('all_Est_slopes_easy_low_V2.csv')
all_slopes_easy_mid.to_csv('all_Est_slopes_easy_mid_V2.csv')
all_slopes_easy_upper.to_csv('all_Est_slopes_easy_upper_V2.csv')

with open(LR_path) as file:
    learning_rates = pd.read_csv(file, sep=',', index_col="Index")

all_slopes_diff_low,all_slopes_diff_mid,all_slopes_diff_upper = difficult_est_slopes(diff_data=difficult_data, fully_avg=False)
all_slopes_diff_low.to_csv('all_Est_slopes_diff_low_V2.csv')
all_slopes_diff_mid.to_csv('all_Est_slopes_diff_mid_V2.csv')
all_slopes_diff_upper.to_csv('all_Est_slopes_diff_upper_V2.csv')

# want 3 plots for lower, upper and middle third of LR each
# every plot shows both thresholds



