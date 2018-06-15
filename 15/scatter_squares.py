import matplotlib.pyplot as plt

# y_values = [1,4,8,16,25]
# x_values = [1,2,3,4,5]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40,edgecolors='none',c=y_values,cmap=plt.cm.Blues)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)


plt.show()