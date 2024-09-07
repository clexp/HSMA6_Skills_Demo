import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [3,7,2,1,4,8,1,2,3,12]

fig_1, ax = plt.subplots()

ax.set_xlabel('Time')
ax.set_ylabel('Number of patients')

ax.plot(x,y)
fig_1.show()
input(" ok?")
