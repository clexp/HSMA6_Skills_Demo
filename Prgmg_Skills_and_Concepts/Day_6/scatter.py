
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

a = [87,67,85,45,65,34,43,23,21]
b = [55,44,66,33,55,66,33,77,99]

fig_1, ax = plt.subplots()

ax.set_xlabel('A')
ax.set_ylabel('B')

ax.scatter(a,b)
fig_1.show()
input(" ok?")
fig_1.savefig("scatter.jpg")
