
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

students = ['bill','harry', 'anglo','saxon']
score = [55,44,66,33]

fig_1, ax = plt.subplots()

ax.set_xlabel('Student')
ax.set_ylabel('Score')

ax.bar(students,score)
fig_1.show()
input(" ok?")
