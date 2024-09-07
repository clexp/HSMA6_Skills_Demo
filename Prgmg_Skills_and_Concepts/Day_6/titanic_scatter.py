import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
path = "/Users/clexp/Sync/hsma/day_5/h6_1f_python_part_2/1f_python_programming_part_2/titanic_dataset.csv"

df = pd.read_csv(path, index_col="PassengerId")


fig_1, ax = plt.subplots()

ax.hist(df[["Age"]], 50)
ax.set_title('Histogram')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
fig_1.show()
input(" ok?")
fig_1.savefig("titanic_scatter.jpg")
