import matplotlib.pyplot as plt
x =  range(-1000,1000)
y =[i**3 for i in x]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x,y,s=1,color = (0.4,0.8,0.9))   # color is in RGB format
#To define a color, pass the color argument a tuple
#with three float values (one each for red, green, and blue, in
# that order), using values between 0 and 1
ax.set_title("cubes_function",fontsize = 50)
ax.set_xlabel('values',fontsize = 15)
ax.set_ylabel('cubes_value',fontsize = 15)

ax.tick_params(labelsize = 14)

plt.show()