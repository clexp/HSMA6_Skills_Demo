import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

time = [1,2,3,4,5,6,7,8,9,10]
patients = [3,7,2,1,4,8,1,2,3,12]
doctors = [2,1,2,2,1,0,1,2,2,3]

fig_1, ax = plt.subplots()

ax.set_xlabel('Time')
ax.set_ylabel('Number of patients')

ax.plot(time, patients, color="blue", linestyle="-")
ax.plot(time, doctors, color="red", linestyle=":")
fig_1.show()
input(" ok?")
