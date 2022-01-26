import pandas as pd
from os.path import dirname, join

script_dir = dirname(__file__)
pop_path = join(script_dir, 'Transformed_BT3.csv')
with open(pop_path) as file:
    data = pd.read_csv(file, sep=';', index_col="Index", dtype={'correct': 'float64'})

# remove empty tailing columns that excel creates
data.dropna(axis=1, how='all', inplace=True)

all_easy = pd.DataFrame()
all_difficult = pd.DataFrame()

for subject in set(data['Subject']):

    # select that subject's data and add trials for first list
    sub_df = data[data['Subject'] == subject][['Subject', 'Created', 'correct']].dropna()
    sub_df = sub_df.reset_index()[['Subject', 'correct']]
    sub_df['Trials'] = sub_df.index + 1
    sub_df = sub_df[['correct', "Trials"]]

    # split df at point of completion
    first = pd.DataFrame()
    second = pd.DataFrame()
    completed = False
    for i, v in sub_df.iterrows():
        current_row = sub_df.iloc[[i]]
        correct_val = current_row['correct'].array[0]

        # after the first 1 change to the second dataframe
        if (completed == False) and (correct_val <= 1):
            first = first.append(current_row)
            if correct_val == 1:
                completed = True
        else:
            second = second.append(current_row)

    # add some columns
    second["Trials"] = second.reset_index().index + 1
    first["Subject"] = subject
    second["Subject"] = subject

    # undo the counterbalancing
    easy_first = True if subject % 2 == 0 else False
    if easy_first:  # if true
        first['Level'] = 'Easy'
        second['Level'] = 'Difficult'
        all_easy = all_easy.append(first)
        all_difficult = all_difficult.append(second)
    else:
        second['Level'] = 'Easy'
        first['Level'] = 'Difficult'
        all_easy = all_easy.append(second)
        all_difficult = all_difficult.append(first)

subjects_all = set(data['Subject'])
demographics = data[['Subject', 'gender', 'age', 'education']].dropna()
# print(demographics)
demographics.to_csv("demographics.csv")

all_difficult = all_difficult.merge(demographics, on='Subject', how='inner')
all_easy = all_easy.merge(demographics, on='Subject', how='inner')

# all_difficult = all_difficult.pivot(index=['Subject', 'Level', 'gender', 'age', 'education'], columns='Trials',
#                                     values=['correct'])
#
# all_easy = all_easy.pivot(index=['Subject', 'Level', 'gender', 'age', 'education'], columns='Trials',
#                           values=['correct'])
print(all_easy)

all_easy.to_csv("FIN_All_easy_trials_rev.csv")
all_difficult.to_csv("FIN_All_difficult_trials_rev.csv")
