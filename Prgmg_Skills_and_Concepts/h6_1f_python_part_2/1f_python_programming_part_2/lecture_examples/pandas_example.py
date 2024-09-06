

import pandas as pd

df = pd.read_csv("input_data.csv", index_col="Patient ID")

print(df)

df[["Name", "County"]]

df.loc[90154]

df.loc[[76547,19811]]

df.loc[[76547,19811],
       ["Name", "County"]]

df.loc[df["County"] == "Cornwall"]

df.loc[df["Age"] >= 60]

df.loc[(df["County"] == "Cornwall") & (df["Age"] >= 60)]

df.loc[(df["County"] == "Cornwall") | (df["Age"] >= 60)]

row_to_add = ["Dan","Yes",42,"Cornwall"]
df.loc[12345] = row_to_add

pivot_age_by_county = pd.pivot_table(data=df,
                                     index="County",
                                     values="Age",
                                     aggfunc="mean")

pivot_age_by_county

pivot_age_by_county.loc["Cornwall"]

df[df["County"] == "Cornwall"]["Flu Vaccine"].value_counts()

df_no_names = df.drop(["Name"], axis=1)

df_no_alfred = df.drop([90154])

admissions_data = {'Patient ID':[105,243,105,105,316],
                   'Age':[76,31,76,76,52],
                   'Admissions':[3,1,3,3,2]}

admissions_df = pd.DataFrame(admissions_data)

no_dup_admissions_df = admissions_df.drop_duplicates(keep='last')

admissions_data = {'Patient ID':[105,243,105,105,316],
                   'Age':[76,31,76,76,52],
                   'Admissions':[3,1,3,4,2]}

admissions_df = pd.DataFrame(admissions_data)

no_dup_admissions_df = admissions_df.drop_duplicates(subset=["Admissions"])

df.sort_values(by=["Age", "Patient ID"], inplace=True)

