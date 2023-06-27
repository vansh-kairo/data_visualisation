import matplotlib.pyplot as plot

input = [1,2,3,4,5,6]
output = [1,4,9,16,25,36]

fig, ax = plot.subplots()
ax.plot(input,output,linewidth = 3)
ax.set_title("squuares_of_numbers",fontsize = 24)
ax.set_xlabel("values",fontsize = 12)
ax.set_ylabel("squares",fontsize = 12)

ax.tick_params(labelsize = 14)

plot.show()
