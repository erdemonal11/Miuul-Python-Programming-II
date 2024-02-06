# CASE STUDY II:

import seaborn as sns

# List Comprehension


# Task I:


df = sns.load_dataset("car_crashes")
df.columns = ["NUM_" + col.upper() for col in df.columns]
print(df.columns)

# Task II:

df.columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
print(df.columns)

# Task III:

og_list = ["abbrev", "no_previous"]
cols = [col for col in df.columns if col not in og_list]
new_df = df[cols]
new_df.head()

# Pandas

# Task I:

dft = sns.load_dataset("titanic")

# Task II:

female = dft[dft["sex"] == "female"]["sex"].count()
male = dft[dft["sex"] == "male"]["sex"].count()

print("Female passenger number:", female)
print("Male passenger number:", male)

# dft["sex"].value_counts() same answer

# Task III:

dft.nunique()

# Task IV:

dft["pclass"].unique()

# Task V:

total = ["pclass", "parch"]
dft[total].nunique()

# Task VI:

dft["embarked"].dtype
dft["embarked"] = dft["embarked"].astype("category")
dft["embarked"].dtype

# Task VII:

print(dft[dft["embarked"] == "C"])

# Task VIII:

print(dft[dft["embarked"] != "S"])

# Task IX

youngfemale = dft[(dft["age"] < 30) & (dft["sex"] == "female")]

print(youngfemale)

# Task X:

fareolder = dft[(dft["fare"] > 500) | (dft["age"] > 70)]

print(fareolder)

# Task XI:

dft.isnull().sum()

# Task XII:

dft.drop("who", axis=1, inplace=True)

# Task XIII:

deck = dft["deck"].mode()[0]
dft["deck"].fillna(deck, inplace=True)

# Task XIV:

age_median = dft["age"].median()
dft["age"].fillna(age_median, inplace=True)

# Task XV:

stats = dft.groupby(["pclass", "sex"])["survived"].agg(["sum", "count", "mean"])
print(stats)


# Task XVI:

def flag_function(age):
    if age < 30:
        return 1
    else:
        return 0


dft['age_flag'] = dft['age'].apply(lambda x: flag_function(x))

# Task XVII:

tips = sns.load_dataset("tips")

# Task XVIII:

time_total_bill = tips.groupby('time')['total_bill'].agg(['sum', 'min', 'max', 'mean'])
print(time_total_bill)

# Task XIX:

day_time_total_bill = tips.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean'])
print(day_time_total_bill)

# Task XX:

lunch_female = tips[(tips['time'] == 'Lunch') & (tips['sex'] == 'Female')].groupby('day')[['total_bill', 'tip']].agg(
    ['sum', 'min', 'max', 'mean'])
print(lunch_female)

# Task XXI:

filtered_order = tips.loc[(tips['size'] < 3) & (tips['total_bill'] > 10)]
filtered_order_mean = filtered_order['total_bill'].mean()
print(filtered_order_mean)

# Task XXII:

tips['total_bill_tip_sum'] = tips['total_bill'] + tips['tip']

# Task XXIII:

top_30 = tips.sort_values(by='total_bill_tip_sum', ascending=False).head(30).reset_index(drop=True)
print(top_30)
