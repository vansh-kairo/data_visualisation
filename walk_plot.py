import matplotlib.pyplot as plt
from random_walk import randomwalk

rw= randomwalk()
rw.walk()

plt.style.use('classic')
fig, ax=plt.subplots()
plot_color=range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,s=10,c=plot_color,cmap=plt.cm.Blues,edgecolors='none')
ax.scatter(0,0,s=100,c='green',edgecolors='none')
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)

ax.set_aspect('equal')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()

    