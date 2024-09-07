import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
path = "Day_6/meds_used_per_day.csv"
Run_1 = []
Run_2 = []
Run_3 = []

with open(path,'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        Run_1.append(row[0])
        Run_2.append(row[1])
        Run_3.append(row[2])

time = [ i for i in range(len(Run_1)) ]

fig_1, ax = plt.subplots()

ax.set_title('Meds per day')
ax.set_xlabel('Day')
ax.set_ylabel('Count of medications')
ax.legend()

ax.plot(time, Run_1, color="blue", linestyle="-", label="Run 1")
ax.plot(time, Run_2, color="red", linestyle=":", label="Run 2")
ax.plot(time, Run_3, color="green", linestyle="--", label="Run 3")
fig_1.show()
fig_1.savefig("meds_per_day.jpg")
input(" ok?")

